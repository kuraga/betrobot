import re
import dirtyjson
import codecs
from betrobot.util.common_util import recursive_sub


def fix_dirtyjson(string):
    return recursive_sub(r',(\n*)(,|}|])', r',null\1\2', string)


def _extract_dirtyjson_definition(match_html, match_data, r, key, flags=0):
    m = re.search(r, match_html, flags)
    if m is None:
        return

    dirtyjson_string = m.group(1)
    fixed_dirtyjson_string = fix_dirtyjson(dirtyjson_string)

    value = dirtyjson.loads(fixed_dirtyjson_string)
    if value is None:
        return

    match_data[key] = value


def _extract_escaped_json_definition(match_html, match_data, r, key, flags=0):
    m = re.search(r, match_html, flags)
    if m is None:
        return

    json_string = m.group(1)
    unescaper = codecs.getdecoder('unicode_escape')
    unescaped_json_string = unescaper(json_string)[0]

    value = json.loads(unescaped_json_string)
    if value is None:
        return

    match_data[key] = value


def handle_match(html_or_file):
    if isinstance(html_or_file, str):
        match_html = html_or_file
    else:
        match_html = html_or_file.read()

    match_data = {}

    # WARNING: Предполагается отсутствие символа ';' в репрезентации значении переменной
    _extract_dirtyjson_definition(match_html, match_data, r'var matchCentreData = (.+?);', 'matchCentreData')
    # WARNING: В случае подключения других страниц (и необходимости):
    # _extract_dirtyjson_definition(match_html, match_data, r'var matchCentreEventType = (.+?);', 'matchCentreEventType')
    # _extract_dirtyjson_definition(match_html, match_data, r'var formationIdNameMappings = (.+?);', 'formationIdNameMappings')
    # _extract_dirtyjson_definition(match_html, match_data, r'var matchStats = (.+?);', 'matchStats', re.MULTILINE | re.DOTALL)
    # _extract_dirtyjson_definition(match_html, match_data, r'var initialMatchDataForScrappers = (.+?);', 'initialMatchDataForScrappers', re.MULTILINE | re.DOTALL)
    # _extract_escaped_json_definition(match_html, match_data, r'var matchHeaderJson = JSON.parse\(\'(.+?)\'\);', 'matchHeader', 0)
    # _extract_escaped_json_definition(match_html, match_data, r'var homePlayers = JSON.parse\(\'(.+?)\'\);', 'homePlayers', 0)
    # _extract_escaped_json_definition(match_html, match_data, r'var awayPlayers = JSON.parse\(\'(.+?)\'\);', 'awayPlayers', 0)

    return match_data
