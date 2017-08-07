import bs4
import re


def get_text(tag_or_string):
  if isinstance(tag_or_string, bs4.Tag):
    return tag_or_string.get_text(separator=' ', strip=True)
  else:
    return str(tag_or_string)


def handle_date(html_or_file):
    data = []

    soup = bs4.BeautifulSoup(html_or_file, 'lxml')

    tables = soup.find_all('table', class_='tiles-bets')
    for table in tables:
      head_tr_ths = table.find('thead').find('tr', recursive=False).find_all('th', recursive=False)
      intelbet_country = get_text(head_tr_ths[1])
      intelbet_tournament = get_text(head_tr_ths[1])

      trs = table.find('tbody').find_all('tr', recursive=False)
      for tr in trs:
          teams_tag = tr.find('td', class_='name-with-icon')
          intelbet_home_tag = teams_tag.find_all('span')[0]
          intelbet_home = get_text(intelbet_home_tag)
          intelbet_away_tag = teams_tag.find_all('span')[1]
          intelbet_away = get_text(intelbet_away_tag)

          url_tag = tr.find('a')
          url = 'http:%s' % (url_tag['href'],)

          match_time_tag = tr.find('td', class_='tiles-bet-time')
          match_time_str = get_text(match_time_tag)

          item = (intelbet_country, intelbet_tournament, intelbet_home, intelbet_away, url, match_time_str)
          data.append(item)

    return data


def _extract_player_names(table_tag):
    player_names = []

    trs = table_tag.find('tbody').find_all('tr', recursive=False)
    for tr in trs:
        tds = tr.find_all('td', recursive=False)
        player_name_td = tds[1]
        player_name = get_text(player_name_td)
        player_names.append(player_name)

    return player_names


def handle_match(html_or_file):
    home_player_names = None
    away_player_names = None

    soup = bs4.BeautifulSoup(html_or_file, 'lxml')

    approximate_lineup_tag = soup.find(string=re.compile(r'^\s*Ориентировочный состав\s*$'))
    accurate_lineup_tag = soup.find(string=re.compile(r'^\s*Стартовый состав\s*$'))
    if accurate_lineup_tag is not None:
        lineup_tag = accurate_lineup_tag
    elif approximate_lineup_tag is not None:
        lineup_tag = approximate_lineup_tag
    else:
        lineup_tag = None

    if lineup_tag is not None:
        home_lineup_table_tag = lineup_tag.parent.find_next(class_='match-team-table')
        home_player_names = _extract_player_names(home_lineup_table_tag)

        away_lineup_table_tag = home_lineup_table_tag.find_next(class_='match-team-table')
        away_player_names = _extract_player_names(away_lineup_table_tag)

    return (home_player_names, away_player_names)
