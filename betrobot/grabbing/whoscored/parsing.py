import re
import dirtyjson
import codecs
from betrobot.util.common_util import recursive_sub


def fix_dirtyjson(string):
    return recursive_sub(r',(\n*)(,|}|])', r',null\1\2', string)


def extract_dirtyjson_definition(match_html, match_data, r, key, flags=0):
    m = re.search(r, match_html, flags)
    if m is None:
        return

    dirtyjson_string = m.group(1)
    fixed_dirtyjson_string = fix_dirtyjson(dirtyjson_string)

    value = dirtyjson.loads(fixed_dirtyjson_string)
    if value is None:
        return

    match_data[key] = value


def extract_escaped_json_definition(match_html, match_data, r, key, flags=0):
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
