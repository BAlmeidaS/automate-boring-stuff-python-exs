#!python3
# A script that opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression and print matches results.

import os
import re


folder = input('pass a folder: ')

if not os.path.isabs(folder):
    folder = os.path.join(os.path.abspath(os.getcwd()), folder)

if not os.path.exists(folder) or not os.path.isdir(folder):
    raise RuntimeError('Invalid path')

user_regex = input(f'enter some regex: ')

try:
    pattern = re.compile(user_regex)
except re.error:
    raise RuntimeError('Invalid regex')

for f in os.listdir(folder):
    if f.endswith('.txt'):
        with open(os.path.join(folder, f), 'r') as f:
            for line in f.readlines():
                if re.match(pattern, line):
                    print(re.match(pattern, line).string)

# with open(reference_filepath, 'r') as f:
#     for line in f.readlines():
#         if re.match(pattern, line):
#             print(re.match('.*text.*', line).string)
