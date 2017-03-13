import os
import glob
import bs4
import re
import json
import datetime
import uuid
from betrobot.util.common_util import float_safe


def get_text(tag_or_string):
  if isinstance(tag_or_string, bs4.Tag):
    return tag_or_string.get_text(separator=' ', strip=True)
  else:
    return str(tag_or_string)


def remove_colon_and_dash(string):
  if len(string) == 0:
    return ''

  m = re.search('^(.+?)(?:\s*[-:])?$', string)
  return m.group(1)


def get_and_remove_special_word(string):
  m = re.search(r'^(?:((?:УГЛ|ЖК|% владения мячом|удары в створ|фолы|офсайды))\s+)?(.+)$', string)
  return m.groups()


def handle(html_or_file):
  soup = bs4.BeautifulSoup(html_or_file, 'lxml')

  current = soup.contents[0]
  while current is not None:

    if current.name == 'table' and current.get('cellspacing') == '2' and current.get('cellpadding') == '1' and current.get('width') == '100%':
      try:
        for tournament_raw_match_data in handle_tournament_day(current):
          yield tournament_raw_match_data
      except Exception as e:
        print(e)
      current = current.next_sibling
    else:
      current = current.next_element


def handle_tournament_day(tournament_table):
  raw_matches_data = []

  tournament_day_thead = tournament_table.find('thead', recursive=False)
  tournament_name = get_text( tournament_day_thead.find('tr', recursive=False).find('td', recursive=False) )
  # TODO: Фильтровать турниры
  if re.match(r'^Футбол\.', tournament_name) is None:
    return []

  tournament_date_tbody = tournament_table.find('tbody', class_='date', recursive=False)
  tournament_date = get_text( tournament_date_tbody.find('tr', recursive=False).find('td', recursive=False) )

  main_data_tds = tournament_table.find('tbody', class_='chead', recursive=False).find('tr', class_='th', recursive=False).find_all('td', recursive=False)
  main_data_names = [ get_text(main_data_td) for main_data_td in main_data_tds ]

  match_tbodies = tournament_table.find_all('tbody', recursive=False, id='line')
  for match_tbody in match_tbodies:
    match_trs = match_tbody.find_all('tr', recursive=False)
    if len(match_trs) == 0:
      continue

    main_data_tds = match_trs[0].find_all('td', recursive=False)
    main_data = [ (main_data_names[i], get_text(main_data_tds[i])) for i in range(len(main_data_names)) ]
    try:
      (time, home, away, special_word, additional, main_data_bets) = handle_main_data(main_data)
    except Exception:
      print('Bad main data')
      continue

    bets = []
    bets += main_data_bets
    if len(match_trs) >= 2 and 't_comment' not in match_trs[1].find('td', recursive=False).get('class'):
      elements = match_trs[1].find('td', recursive=False).contents
      try:
        bets += handle_bets(elements)
      except Exception as e:
        print(e)

    # TODO: Бывает (как минимум) еще одна строка

    raw_match_data = {
      'tournament': tournament_name,
      'date': tournament_date,
      'time': time,
      'home': home,
      'away': away,
      'special_word': special_word,
      'bets': bets
    }
    raw_matches_data.append(raw_match_data)

  return raw_matches_data


def handle_bets(elements):
  bets = []

  for element in elements:

    try:

      if element.name == 'div':
        if len(element.contents) >= 3 and element.contents[2].name == 'table':
          type_ = remove_colon_and_dash( get_text(element.contents[1]) )
          bets += get_bets_from_table(element.contents[2])
        else:
          bets += get_bets_from_line(element)

      elif element.name == 'table':
        bets += get_bets_from_table(element)

      else:
        continue

    except Exception as e:
      print(e)
      continue

  return bets


def get_bets_from_line(element):
  bets = []

  bet_elements = list(element.descendants)
  type_ = remove_colon_and_dash( get_text( bet_elements[0] ) )

  bet_blocks = []
  bet_block = ['', '', None]
  i = 2  # 0: <b>, 1: <b>.contents[0], 2: <b>.next_sibling
  while i < len(bet_elements):
    current = bet_elements[i]
    if current.name == 'b':
      bet_blocks.append(bet_block)

      bet_block = ['', '', None]
      bet_block[0] = remove_colon_and_dash( get_text(current) )
      (bet_block[2], bet_block[0]) = get_and_remove_special_word(bet_block[0])

      end = current.next_sibling
      while i < len(bet_elements) and bet_elements[i] != end: i += 1

    else:
      if isinstance(current, bs4.element.NavigableString):
        bet_block[1] += ' ' + str(current)
      i += 1

  bet_blocks.append(bet_block)

  for (prefix, bet_str, bet_special_word) in bet_blocks:
    bet_str = bet_str.strip()
    if len(bet_str) == 0:
      continue

    m1 = re.search(r'^(?:-|:)?\s*(?:\(\s*(.+?)\s*\)\s+)?(.+)$', bet_str)
    if m1 is None:
      continue
    handicap = float_safe( re.sub(r'\s*', '', m1.group(1)) ) if m1.group(1) is not None else None
    unhandicaped = m1.group(2)

    for part in re.split(r'\s*;', unhandicaped):
      part = part.strip()
      if len(part) == 0:
        continue

      m2 = re.search(r'^(?:(.+?)(?:\s*[:-])?\s+)?(\S+)$', part)
      if m2 is None:
        continue
      name = m2.group(1) if m2.group(1) is not None else ''

      value = float_safe( m2.group(2) )
      if value is None:
        continue

      bet = [bet_special_word, type_, prefix, name, handicap, value]
      bets.append(bet)

  return bets


def get_bets_from_table(element):
  bets = []

  trs = element.find('tbody', recursive=False).find_all('tr', recursive=False)

  if 'n' in trs[0].find('td', recursive=False).get('class'):
    type_ = remove_colon_and_dash( get_text( trs[0].find('td', recursive=False) ) )
    s = 1
  else:
    type_ = None
    s = 0

  name_tds = trs[s].find_all('td', recursive=False)[1:]
  names = [ get_text(name_td) for name_td in name_tds ]

  for i in range(s+1, len(trs)):
    tds = trs[i].find_all('td', recursive=False)
    if len(tds) == 0:
      continue
    subtype = remove_colon_and_dash( get_text(tds[0]) )

    table_data = [ (names[j-1], get_text(tds[j])) for j in range(1, len(tds)) ]
    bets += handle_table_data(table_data, type_=type_, subtype=subtype)

  return bets


def handle_main_data(main_data):
  bets = []

  i = 0
  while i < len(main_data):
    if main_data[i][0] in ('ВРЕМЯ', 'Время', 'время'):
      time = main_data[i][1]
    elif main_data[i][0] in ('КОМАНДА1', 'Команда1', 'команда1', 'КОМАНДА 1', 'Команда 1', 'команда 1'):
      (special_word, home) = get_and_remove_special_word(main_data[i][1])
    elif main_data[i][0] in ('КОМАНДА1', 'Команда2', 'команда2', 'КОМАНДА 2', 'Команда 2', 'команда 2'):
      (special_word, away) = get_and_remove_special_word(main_data[i][1])
    elif main_data[i][0] in ('ДОП', 'Доп', 'доп'):
      additional = main_data[i][1]
    elif main_data[i][0] in ('1', 'X', '2', '1X', '12', 'X2'):
      bet = [special_word, 'Исход', '', main_data[i][0], None, float_safe(main_data[i][1])]
      bets.append(bet)
    elif main_data[i][0] in ('ФОРА1', 'Фора1', 'фора1', 'ФОРА 1', 'Фора 1', 'фора 1'):
      bet = [special_word, 'Фора', home, '', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])]
      bets.append(bet)
      i += 1
    elif main_data[i][0] in ('ФОРА2', 'Фора2', 'фора2', 'ФОРА 2', 'Фора 2', 'фора 2'):
      bet = [special_word, 'Фора', away, '', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])]
      bets.append(bet)
      i += 1
    elif main_data[i][0] in ('ТОТАЛ', 'Тотал', 'тотал'):
      bet = [special_word, 'Тотал', '', 'Мен', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])]
      bets.append(bet)
      bet = [special_word, 'Тотал', '', 'Бол', float_safe(main_data[i][1]), float_safe(main_data[i+2][1])]
      bets.append(bet)
      i += 2

    i += 1

  return (time, home, away, special_word, additional, bets)


def handle_table_data(main_data, type_, subtype):
  type_subtype = '%s (%s)' % (type_, subtype)

  bets = []

  i = 0
  while i < len(main_data):
    if main_data[i][0] in ('1', 'X', '2', '1X', '12', 'X2'):
      new_bets = [ [None, type_subtype, '', main_data[i][0], None, float_safe(main_data[i][1])] ]
    elif main_data[i][0] in ('ФОРА1', 'Фора1', 'фора1', 'ФОРА 1', 'Фора 1', 'фора 1'):
      new_bets = [ [None, type_subtype, 'Фора', '1', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])] ]
      i += 1
    elif main_data[i][0] in ('ФОРА2', 'Фора2', 'фора2', 'ФОРА 2', 'Фора 2', 'фора 2'):
      new_bets = [ [None, type_subtype, 'Фора', '2', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])] ]
      i += 1
    elif main_data[i][0] in ('ТОТАЛ', 'Тотал', 'тотал'):
      new_bets = [
        [None, type_subtype, '', 'Мен', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])],
        [None, type_subtype, '', 'Бол', float_safe(main_data[i][1]), float_safe(main_data[i+2][1])]
      ]
      i += 2
    else:
      new_bets = [ [None, type_subtype, '', main_data[i][0], None, main_data[i][1]] ]

    bets += new_bets
    i += 1

  return bets


matches_metadata = []

glob_path = os.path.join('tmp', 'data', 'betarch', 'datesHtml', '*.html')
for file_path in glob.iglob(glob_path):
  print(file_path)

  with open(file_path, 'r', encoding='utf-8') as f_in:
    for tournament_day_raw_match_data in handle(f_in):
      match_uuid_str = str(uuid.uuid4())
      match_date_str = datetime.datetime.strptime(tournament_day_raw_match_data['date'], '%d.%m.%Y').strftime('%Y-%m-%d')

      match_data = {
        'uuid': match_uuid_str,
        'tournament': tournament_day_raw_match_data['tournament'],
        'date': match_date_str,
        'time': tournament_day_raw_match_data['time'],
        'home': tournament_day_raw_match_data['home'],
        'away': tournament_day_raw_match_data['away'],
        'specialWord': tournament_day_raw_match_data['special_word'],
        'bets': tournament_day_raw_match_data['bets']
      }

      out_dir_path = os.path.join('tmp', 'data', 'betarch', 'matchesJson', match_date_str)
      os.makedirs(out_dir_path, exist_ok=True)
      out_file_path = os.path.join(out_dir_path, '%s.json' % (match_uuid_str,))
      with open(out_file_path, 'w', encoding='utf-8') as f_out:
        json.dump(match_data, f_out, ensure_ascii=False)

      match_metadata = {
        'uuid': match_uuid_str,
        'tournament': match_data['tournament'],
        'date': match_data['date'],
        'home': match_data['home'],
        'away': match_data['away'],
        'specialWord': match_data['specialWord']
      }
      matches_metadata.append(match_metadata)

matches_metadata_out_file_path = os.path.join('tmp', 'data', 'betarch', 'matches_metadata.json')
with open(matches_metadata_out_file_path, 'w', encoding='utf-8') as matches_metadata_f_out:
  json.dump(matches_metadata, matches_metadata_f_out, ensure_ascii=False)
