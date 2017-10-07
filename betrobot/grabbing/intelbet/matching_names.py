import bs4
import re
import csv
import os
import pandas as pd
from betrobot.util.common_util import count, find_index
from betrobot.betting.sport_util import players_data, save_players_data
from betrobot.grabbing.intelbet.parsing import handle_match
from betrobot.grabbing.intelbet.downloading import intelbet_get


def _get_last_names():
    last_names = []
    for i, row in players_data.iterrows():
        player_name = row['whoscoredPlayerName']
        m = re.search('(\S+)$', player_name)
        last_name = m.group(1)
        last_names.append(last_name)

    return last_names


_last_names = _get_last_names()


def _get_first_letter_and_last_names():
    first_letter_and_last_names = []
    for i, row in players_data.iterrows():
        player_name = row['whoscoredPlayerName']
        m = re.search('(\S+)$', player_name)
        first_letter_and_last_name = player_name[0] + ' ' + m.group(1)
        first_letter_and_last_names.append(first_letter_and_last_name)

    return first_letter_and_last_names


_first_letter_and_last_names = _get_first_letter_and_last_names()


def _read_intelbet_player_names():
    intelbet_player_names_df = pd.read_csv(intelbet_player_names_file_path, encoding='utf-8').set_index('intelbetPlayerName', drop=False)

    return intelbet_player_names_df


intelbet_player_names_file_path = os.path.join('data', 'intelbet_player_names.csv')
intelbet_player_names_df = _read_intelbet_player_names()


def _save_intelbet_player_names():
    intelbet_player_names_df.to_csv(intelbet_player_names_file_path, encoding='utf-8', quoting=csv.QUOTE_NONNUMERIC, index=False)


def intelbet_player_names_add(intelbet_player_name, team):
    if intelbet_player_name not in intelbet_player_names_df.index.tolist():
        intelbet_player_names_df.loc[intelbet_player_name] = pd.Series({ 'intelbetPlayerName': intelbet_player_name, 'whoscoredName': team })
        _save_intelbet_player_names()


def intelbet_player_names_match(intelbet_player_name, whoscored_player_name):
    players_data.loc[players_data['whoscoredPlayerName'] == whoscored_player_name, 'intelbetPlayerName'] = intelbet_player_name
    save_players_data()


def match_names_automatically(ru_url):
    ru_html = intelbet_get(ru_url, delay=0.5)
    if ru_html is None:
        raise RuntimeError("can't download match!")
    (ru_home_player_names, ru_away_player_names) = handle_match(ru_html)

    ro_url = re.sub(r'ru\/match-center', r'ro/centrul-de-pariere', ru_url)
    print(ru_url, ro_url)
    ro_html = intelbet_get(ro_url, delay=0.5)
    if ro_html is None:
        print("Match hasn't a .ro version")
        return
    (ro_home_player_names, ro_away_player_names) = handle_match(ro_html)

    if ru_home_player_names is None or ru_away_player_names is None \
      or ro_home_player_names is None or ro_away_player_names is None:
        raise RuntimeError('Bad data!')

    ru_player_names = ru_home_player_names + ru_away_player_names
    ro_player_names = ro_home_player_names + ro_away_player_names

    ro_last_names = []
    for ro_player_name in ro_player_names:
        m = re.search('(\S+)$', ro_player_name)
        ro_last_name = m.group(1)
        ro_last_names.append(ro_last_name)

    ro_first_letter_and_last_names = []
    for ro_player_name in ro_player_names:
        m = re.search('(\S+)$', ro_player_name)
        ro_first_letter_and_last_name = ro_player_name[0] + ' ' + m.group(1)
        ro_first_letter_and_last_names.append(ro_first_letter_and_last_name)


    for i in range(len(ro_last_names)):
        ro_last_name = ro_last_names[i]
        ind = None

        n1 = count(ro_last_name, _last_names)
        if n1 == 1:
            ind = find_index(ro_last_name, _last_names)
            players_data.iloc[ind, players_data.columns.get_loc('intelbetPlayerName')] = ru_player_names[i]

        elif n1 > 1:
            ro_first_letter_and_last_name = ro_first_letter_and_last_names[i]
            n2 = count(ro_first_letter_and_last_name, _first_letter_and_last_names)
            if n2 == 1:
                ind = find_index(ro_first_letter_and_last_name, _first_letter_and_last_names)
                players_data.iloc[ind, players_data.columns.get_loc('intelbetPlayerName')] = ru_player_names[i]

        # TODO: Учитывать дефисы
        # TODO: Учитывать буквы с акцентами

        if ind is not None:
            print('%s - %s' % (ru_player_names[i], players_data.iloc[ind, players_data.columns.get_loc('whoscoredPlayerName')]))
        else:
            print("Can't match: %s" % (ru_player_names[i],))

    save_players_data()
