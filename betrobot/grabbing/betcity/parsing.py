import bs4
import re
from betrobot.util.common_util import float_safe, get_tag_text


def remove_colon_and_dash(string):
  if len(string) == 0:
    return ''

  m = re.search('^(.+?)(?:\s*[-:])?$', string)
  return m.group(1)


def get_and_remove_special_word(string):
  m = re.search(r'^(?:(УГЛ|ЖК|% владения мячом|удары в створ|фолы|офсайды)\s+)?(.+?)(?:\s+(УГЛ|ЖК|% владения мячом|удары в створ|фолы|офсайды))?$', string)

  if m.group(1) is not None:
    return (m.group(1), m.group(2))
  elif m.group(3) is not None:
    return (m.group(3), m.group(2))
  else:
    return (None, string)


def handle(html_or_file):
  soup = bs4.BeautifulSoup(html_or_file, 'lxml')

  current = soup.contents[0]
  while current is not None:

    if current.name == 'table' and current.get('cellspacing') == '2' and current.get('cellpadding') == '1' and current.get('width') == '100%':
      try:
        for tournament_raw_match_data in handle_tournament(current):
          yield tournament_raw_match_data
      except Exception:
        pass
      current = current.next_sibling
    else:
      current = current.next_element


def handle_tournament(tournament_table):
  raw_matches_data = []

  tournament_table_tbodies = tournament_table.find_all('tbody', recursive=False)
  tournament_name_tbody = tournament_table_tbodies[0]

  tournament_name = get_tag_text( tournament_name_tbody.find('tr', recursive=False).find('td', recursive=False) )

  tournament_main_tbody = tournament_table_tbodies[1]

  bets = None
  trs = tournament_main_tbody.find_all('tr', recursive=False)
  for tr in trs:
    if 'ng-hide' in tr.get('class', []):
      continue
    if 't_comment' in tr.find('td', recursive=False).get('class', []):
      continue

    if tr.find('td', recursive=False).get('colspan') == '13':
      if bets is not None:
        raw_match_data = {
          'tournament': tournament_name,
          'date': match_date_str,
          'time': time,
          'home': home,
          'away': away,
          'special_word': special_word,
          'bets': bets
        }
        raw_matches_data.append(raw_match_data)

      match_date_str = get_tag_text( tr.find('td', recursive=False) )

    if 'th' in tr.get('class', []):
      main_data_name_tds = tr.find_all('td', recursive=False)
      main_data_names = [ get_tag_text(main_data_name_td) for main_data_name_td in main_data_name_tds ]

    if 'tc' in tr.get('class', []) or 'tc1' in tr.get('class', []):

      if bets is not None:
        raw_match_data = {
          'tournament': tournament_name,
          'date': match_date_str,
          'time': time,
          'home': home,
          'away': away,
          'special_word': special_word,
          'bets': bets
        }
        raw_matches_data.append(raw_match_data)

      main_data_tds = tr.find_all('td', recursive=False)
      main_data = [ (main_data_names[i], get_tag_text(main_data_tds[i])) for i in range(len(main_data_names)) ]
      try:
        (time, home, away, special_word, additional, main_data_bets) = handle_main_data(main_data)
      except Exception:
        return raw_matches_data

      bets = []
      bets += main_data_bets

    elif 'tcd' in tr.get('class', []) or 'tcd1' in tr.get('class', []):

      divs_and_tables = tr.find('td').find('div', class_='extTbl').find('div').contents
      try:
        for element in divs_and_tables:
          if element.name == 'div':
            bets += handle_bets(element.contents, home=home, away=away)
          elif element.name == 'table':
            bets += handle_bets([ element ], home=home, away=away)
          else:
            continue
      except Exception:
        pass

    else:
      continue

  if bets is not None:
    raw_match_data = {
      'tournament': tournament_name,
      'date': match_date_str,
      'time': time,
      'home': home,
      'away': away,
      'special_word': special_word,
      'bets': bets
    }
    raw_matches_data.append(raw_match_data)

  return raw_matches_data


def handle_bets(elements, home, away):
  bets = []

  for element in elements:
    try:
      if element.name == 'div':
        # WARNING: На betarch'e было внутри element может быть table
        bets += get_bets_from_line(element, home=home, away=away)

      elif element.name == 'table':
        bets += get_bets_from_table(element, home=home, away=away)

      else:
        continue

    except Exception:
      continue

  bets = [ bet for bet in bets if bet[5] is not None ]

  return bets


def get_bets_from_line(element, home, away):
  bets = []

  type_ = remove_colon_and_dash( get_tag_text( element.contents[0].contents[0] ) )

  bet_blocks = []
  bet_block = ['', '', None]
  bet_elements = list(element.contents[1].descendants)
  i = 0
  while i < len(bet_elements):
    current = bet_elements[i]
    if current.name == 'b':
      bet_blocks.append(bet_block)

      bet_block = ['', '', None]
      bet_block[0] = remove_colon_and_dash( get_tag_text(current) )
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

      bet = [bet_special_word, type_, prefix, name, handicap, value]
      bets.append(bet)

  return bets


def get_bets_from_table(element, home, away):
  bets = []

  thead_trs = element.find('thead', recursive=False).find_all('tr', recursive=False)
  type_ = remove_colon_and_dash( get_tag_text( thead_trs[0] ) )
  name_tds = thead_trs[2].find_all('td', recursive=False)[1:]
  names = [ get_tag_text(name_td) for name_td in name_tds ]

  tbody_trs = element.find_all('tbody', recursive=False)[1].find_all('tr', recursive=False)
  for tr in tbody_trs:
    tds = tr.find_all('td', recursive=False)
    if len(tds) == 0:
      continue
    subtype = remove_colon_and_dash( get_tag_text(tds[0]) )

    table_data = [ (names[j-1], get_tag_text(tds[j])) for j in range(1, len(tds)) ]
    bets += handle_table_data(table_data, type_=type_, subtype=subtype, home=home, away=away)

  return bets


def handle_main_data(main_data):
  bets = []

  i = 0
  while i < len(main_data):
    if re.search(r'^Время$', main_data[i][0], re.IGNORECASE) is not None:
      time = main_data[i][1]
    elif re.search(r'^Команда ?1$', main_data[i][0], re.IGNORECASE) is not None:
      (special_word, home) = get_and_remove_special_word(main_data[i][1])
    elif re.search(r'^Команда ?2$', main_data[i][0], re.IGNORECASE) is not None:
      (special_word, away) = get_and_remove_special_word(main_data[i][1])
    elif re.search(r'^Доп$', main_data[i][0], re.IGNORECASE) is not None:
      additional = main_data[i][1]
    elif main_data[i][0] in ('1', 'X', '2', '1X', '12', 'X2'):
      bet = [special_word, 'Исход', '', main_data[i][0], None, float_safe(main_data[i][1])]
      bets.append(bet)
    elif re.search(r'^Фора ?1$', main_data[i][0], re.IGNORECASE) is not None:
      bet = [special_word, 'Фора', home, '', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])]
      bets.append(bet)
      i += 1
    elif re.search(r'^Фора ?2$', main_data[i][0], re.IGNORECASE) is not None:
      bet = [special_word, 'Фора', away, '', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])]
      bets.append(bet)
      i += 1
    elif re.search(r'^Тотал$', main_data[i][0], re.IGNORECASE) is not None:
      bet = [special_word, 'Тотал', '', 'Мен', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])]
      bets.append(bet)
      bet = [special_word, 'Тотал', '', 'Бол', float_safe(main_data[i][1]), float_safe(main_data[i+2][1])]
      bets.append(bet)
      i += 2

    i += 1

  return (time, home, away, special_word, additional, bets)


def handle_table_data(main_data, type_, subtype, home, away):
  type_subtype = '%s (%s)' % (type_, subtype)

  bets = []

  i = 0
  while i < len(main_data):
    if main_data[i][0] in ('1', 'X', '2', '1X', '12', 'X2'):
      new_bets = [ [None, type_subtype, '', main_data[i][0], None, float_safe(main_data[i][1])] ]
    elif re.search(r'^Фора ?1$', main_data[i][0], re.IGNORECASE) is not None:
      new_bets = [ [None, type_subtype, 'Фора', home, float_safe(main_data[i][1]), float_safe(main_data[i+1][1])] ]
      i += 1
    elif re.search(r'^Фора ?2$', main_data[i][0], re.IGNORECASE) is not None:
      new_bets = [ [None, type_subtype, 'Фора', away, float_safe(main_data[i][1]), float_safe(main_data[i+1][1])] ]
      i += 1
    elif re.search(r'^Тотал$', main_data[i][0], re.IGNORECASE) is not None:
      new_bets = [
        [None, type_subtype, 'Тотал', 'Мен', float_safe(main_data[i][1]), float_safe(main_data[i+1][1])],
        [None, type_subtype, 'Тотал', 'Бол', float_safe(main_data[i][1]), float_safe(main_data[i+2][1])]
      ]
      i += 2
    else:
      new_bets = [ [None, type_subtype, '', main_data[i][0], None, main_data[i][1]] ]

    bets += new_bets
    i += 1

  return bets
