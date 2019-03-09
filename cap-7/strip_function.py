#! python3

import re
from copy import copy


def my_strip_dummy(string, sub_string=' '):
    result = copy(string)
    for c in sub_string:
        result = result.replace(c, '')
    return result


def my_strip(string, sub_string=' '):
    return re.sub(f'[{sub_string}]*', '', string)


assert my_strip_dummy('   bruno  ') == 'bruno'
assert my_strip_dummy('   bruno  ', 'u') == '   brno  '
assert my_strip_dummy('   bruno  ', ' u') == 'brno'
assert my_strip_dummy('   bruno  ', 'bn') == '   ruo  '
assert my_strip_dummy('   bruno  ', ' bun') == 'ro'

assert my_strip('   bruno  ') == 'bruno'
assert my_strip('   bruno  ', 'u') == '   brno  '
assert my_strip('   bruno  ', ' u') == 'brno'
assert my_strip('   bruno  ', 'bn') == '   ruo  '
assert my_strip('   bruno  ', ' bun') == 'ro'
