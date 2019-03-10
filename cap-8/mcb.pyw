#!python

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

# The .pyw extension means that Python won’t show a Terminal
# window when it runs this program.

import pyperclip
import shelve
import sys
import pprint
pp = pprint.PrettyPrinter(indent=2)

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pp.pprint(dict(mcb_shelf))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
