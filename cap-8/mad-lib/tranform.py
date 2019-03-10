#!python3
# tranform the text reference-text.txt to a new one, based on some user inputs
# and create a new file final-text.txt.
# Changes the words NOUN, VERB, ADVERB and ADJECTIVES in the text to user
# inputs.

import os
import re

special_words_pattern = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)(.*)')

reference_filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                  'reference-text.txt')

final_filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                  'final-text.txt')

#raises ans exception if it does not find the file
if not os.path.exists(reference_filepath):
    raise RuntimeError(f'{reference_filepath} does not exist')

reference_file = open(reference_filepath, 'r')
final_file = open(final_filepath, 'w')

for line in reference_file.readlines():
    new_line = []

    for word in line.split():
        if re.match(special_words_pattern, word):
            special_word = re.match(special_words_pattern, word)[1].lower()
            new_word = input(f'enter {special_word}:\n')

            word = re.sub(special_words_pattern,
                            r'{}\2'.format(new_word),
                            word)

        new_line.append(word)

    final_file.write(" ".join(new_line) + '\n')


reference_file.close()
final_file.close()
