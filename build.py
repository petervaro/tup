#!/usr/bin/env python3
## INFO ##
## INFO ##

# Import python modules
from os.path import join

# Import tmtools modules
try:
    from tmtools.convert import Language
except ImportError:
    from sys import exit
    print('[ ERROR ] tmtools modules are missing: '
          'install it from http://github.com/petervaro/tmtools')
    exit(1)

# Module level constants
CURRENT_DIR = '.'
LANG_PATH  = join(CURRENT_DIR, 'langs')


#------------------------------------------------------------------------------#
# Import C11 modules
from src.tup import syntax

# Setup names and locations
lang = Language(name='tup',
                path=LANG_PATH,
                scope='tup',
                comments={'line_comments' : ('#',)},
                test_name='Tupfile_TEST',
                test_path='~/.config/sublime-text-3/Packages/User/Tupfile_TEST')
# Convert and save language file
lang.from_dict(syntax)
lang.write()
