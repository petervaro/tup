## INFO ##
## INFO ##

#-- CHEATSHEET ----------------------------------------------------------------#
# HOWTO: http://sublimetext.info/docs/en/reference/syntaxdefs.html
# REGEX: http://manual.macromates.com/en/regular_expressions

# Syntax Definition
syntax = {
    'name': '{NAME}',
    'comment': ('\n\t\tCopyright (C) 2015 - 2016 Peter Varo'
                '\n\t\t<http://github.com/petervaro/tup>'
                '\n'
                '\n\t\tThis program is free software: you can redistribute it'
                '\n\t\tand/or modify it under the terms of the GNU General'
                '\n\t\tPublic License as published by the Free Software'
                '\n\t\tFoundation, either version 3 of the License, or (at your'
                '\n\t\toption) any later version.'
                '\n'
                '\n\t\tThis program is distributed in the hope that it will be'
                '\n\t\tuseful, but WITHOUT ANY WARRANTY; without even the'
                '\n\t\timplied warranty of MERCHANTABILITY or FITNESS FOR A'
                '\n\t\tPARTICULAR PURPOSE. See the GNU General Public License'
                '\n\t\tfor more details.'
                '\n'
                '\n\t\tYou should have received a copy of the GNU General Public'
                '\n\t\tLicense along with this program, most likely a file in'
                '\n\t\tthe root directory, called "LICENSE". If not, see'
                '\n\t\t<http://www.gnu.org/licenses>.'
                '\n\t'),
    'scopeName': 'source.{SCOPE}',
    'fileTypes': ['Tupfile', 'tup'],
    # Patterns
    'patterns':
    [
#-- COMMENT -------------------------------------------------------------------#
        {
            # One-liner
            'name' : 'comment.line.hashmark.{SCOPE}',
            'begin': r'(?<!\\)^\s*#',
            'patterns':
            [
                {
                    'name' : 'comment.line.hashmark.line_continuation.{SCOPE}',
                    'match': r'\\\s*\n'
                }
            ],
            'end': r'(?<!\\)\n'
        },

#-- MACROS --------------------------------------------------------------------#
        {
            'name' : 'meta.macro.definition.{SCOPE}',
            'begin': r'^\s*(!)(.+?)\s*(=)\s*',
            'beginCaptures':
            {
                1: {'name': 'keyword.operator.macro.prefix.{SCOPE}'},
                2: {'name': 'entity.other.inherited-class.macro.variable.{SCOPE}'},
                3: {'name': 'keyword.operator.macro.assignment.{SCOPE}'}
            },
            'patterns':
            [
                {
                    'name' : 'keyword.operator.group.{SCOPE}',
                    'match': r'<(.+?)>',
                    'captures':
                    {
                        1: {'name': 'storage.modifier.group.{SCOPE}'}
                    }
                },
                {
                    'name' : 'keyword.operator.bin.{SCOPE}',
                    'match': r'{(.+?)}',
                    'captures':
                    {
                        1: {'name': 'storage.type.bin.{SCOPE}'}
                    }
                },
                {
                    'name' : 'string.unquoted.command.{SCOPE}',
                    'begin': r'(\|>)',
                    'beginCaptures':
                    {
                        1: {'name': 'keyword.operator.arrow.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {
                            'name' : 'string.unquoted.command.{SCOPE}',
                            'begin': r'(\|>)',
                            'beginCaptures':
                            {
                                1: {'name': 'keyword.operator.arrow.{SCOPE}'}
                            },
                            'patterns':
                            [
                                {
                                    'name' : 'keyword.operator.bin.{SCOPE}',
                                    'begin': r'{(.+?)}',
                                    'beginCaptures':
                                    {
                                        1: {'name': 'storage.type.bin.{SCOPE}'},
                                    },
                                    'patterns':
                                    [
                                        {
                                            'name' : 'invalid.illegal.group_after_bin.{SCOPE}',
                                            'match': r'<.+?>.*'
                                        },
                                        {
                                            'name' : 'invalid.illegal.bin_after_bin.{SCOPE}',
                                            'match': r'{.+?}.*'
                                        },
                                        {'include': '#io_string'},
                                    ],
                                    'end': r'(?=$|(\\)*\n)'
                                },
                                {
                                    'name' : 'keyword.operator.group.{SCOPE}',
                                    'begin': r'<(.+?)>',
                                    'beginCaptures':
                                    {
                                        1: {'name': 'storage.modifier.group.{SCOPE}'}
                                    },
                                    'patterns':
                                    [
                                        {
                                            'name' : 'invalid.illegal.group_after_group.{SCOPE}',
                                            'match': r'<.+?>.*'
                                        },
                                        {
                                            'name' : 'keyword.operator.bin.{SCOPE}',
                                            'begin': r'{(.+?)}',
                                            'beginCaptures':
                                            {
                                                1: {'name': 'storage.type.bin.{SCOPE}'}
                                            },
                                            'patterns':
                                            [
                                                {
                                                    'name' : 'invalid.illegal.group_after_bin.{SCOPE}',
                                                    'match': r'<.+?>.*'
                                                },
                                                {'include': '#io_string'},
                                            ],
                                            'end': r'(?=$|(\\)*\n)'
                                        },
                                        {'include': '#io_string'},
                                    ],
                                    'end': r'(?=$|(\\)*\n)'
                                },
                                {'include': '#io_string'},
                            ],
                            'end': r'(?=(?<!\\)\n)'
                        },
                        {'include': '#cmd_string'},
                    ],
                    'end': r'(?=(?<!\\)\n)'
                },
                {'include': '#io_string'}
            ],
            'end': r'(?<!\\)\n|$'
        },

#-- RULES ---------------------------------------------------------------------#
        {
            'name' : 'meta.rule.{SCOPE}',
            'begin': r'^\s*(:)',
            'beginCaptures':
            {
                1: {'name': 'entity.other.rule.{SCOPE}'},
            },
            'patterns':
            [
                {
                    'name' : 'string.unquoted.inputs.{SCOPE}',
                    'begin': r'(?<=:)\s*(foreach\b)?\s*',
                    'beginCaptures':
                    {
                        1: {'name': 'keyword.control.iteration.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {
                            'name' : 'keyword.operator.group.{SCOPE}',
                            'match': r'<(.+?)>',
                            'captures':
                            {
                                1: {'name': 'storage.modifier.group.{SCOPE}'}
                            }
                        },
                        {
                            'name' : 'keyword.operator.bin.{SCOPE}',
                            'match': r'{(.+?)}',
                            'captures':
                            {
                                1: {'name': 'storage.type.bin.{SCOPE}'}
                            }
                        },
                        {
                            'name' : 'string.unquoted.command.{SCOPE}',
                            'begin': r'(\|>)',
                            'beginCaptures':
                            {
                                1: {'name': 'keyword.operator.arrow.{SCOPE}'}
                            },
                            'patterns':
                            [
                                {
                                    'name' : 'string.unquoted.command.{SCOPE}',
                                    'begin': r'(\|>)',
                                    'beginCaptures':
                                    {
                                        1: {'name': 'keyword.operator.arrow.{SCOPE}'}
                                    },
                                    'patterns':
                                    [
                                        {
                                            'name' : 'keyword.operator.bin.{SCOPE}',
                                            'begin': r'{(.+?)}',
                                            'beginCaptures':
                                            {
                                                1: {'name': 'storage.type.bin.{SCOPE}'},
                                            },
                                            'patterns':
                                            [
                                                {
                                                    'name' : 'invalid.illegal.group_after_bin.{SCOPE}',
                                                    'match': r'<.+?>.*'
                                                },
                                                {
                                                    'name' : 'invalid.illegal.bin_after_bin.{SCOPE}',
                                                    'match': r'{.+?}.*'
                                                },
                                                {'include': '#io_string'},
                                            ],
                                            'end': r'(?=$|(\\)*\n)'
                                        },
                                        {
                                            'name' : 'keyword.operator.group.{SCOPE}',
                                            'begin': r'<(.+?)>',
                                            'beginCaptures':
                                            {
                                                1: {'name': 'storage.modifier.group.{SCOPE}'}
                                            },
                                            'patterns':
                                            [
                                                {
                                                    'name' : 'invalid.illegal.group_after_group.{SCOPE}',
                                                    'match': r'<.+?>.*'
                                                },
                                                {
                                                    'name' : 'keyword.operator.bin.{SCOPE}',
                                                    'begin': r'{(.+?)}',
                                                    'beginCaptures':
                                                    {
                                                        1: {'name': 'storage.type.bin.{SCOPE}'}
                                                    },
                                                    'patterns':
                                                    [
                                                        {
                                                            'name' : 'invalid.illegal.group_after_bin.{SCOPE}',
                                                            'match': r'<.+?>.*'
                                                        },
                                                        {'include': '#io_string'},
                                                    ],
                                                    'end': r'(?=$|(\\)*\n)'
                                                },
                                                {'include': '#io_string'},
                                            ],
                                            'end': r'(?=$|(\\)*\n)'
                                        },
                                        {'include': '#io_string'},
                                    ],
                                    'end': r'(?=(?<!\\)\n)'
                                },
                                {'include': '#cmd_string'},
                            ],
                            'end': r'(?=(?<!\\)\n)'
                        },
                        {'include': '#io_string'}
                    ],
                    'end': r'(?=(?<!\\)\n)'
                },
            ],
            'end': r'(?<!\\)\n|$'
        },

#-- STATEMENTS ----------------------------------------------------------------#
        {
            'name' : 'keyword.control.no_arg.{SCOPE}',
            'match': r'^\s*(else|endif|include_rules|\.gitignore)$'
        },
        {
            'name' : 'string.unquoted.single_arg.{SCOPE}',
            'begin': r'^\s*(ifn?def|run|include|export)\b',
            'beginCaptures':
            {
                1: {'name': 'keyword.control.single_arg.{SCOPE}'}
            },
            'patterns':
            [
                {'include': '#cmd_string'},
            ],
            'end': r'(?<!\\)\n'
        },
        {
            'name' : 'string.unquoted.single_arg.no_eval.{SCOPE}',
            'match': r'^\s*(error)\s+.+?(?<!\\)\n',
            'captures':
            {
                1: {'name': 'keyword.control.single_arg.no_eval.{SCOPE}'}
            }
        },
        {
            'name' : 'meta.control.double_args.{SCOPE}',
            'begin': r'^\s*(ifn?eq)\s+\(\s*',
            'beginCaptures':
            {
                1: {'name': 'keyword.control.conditional.{SCOPE}'},
            },
            'patterns':
            [
                {
                    'name' : 'string.unquoted.lval.{SCOPE}',
                    'begin': r'(?<=\()\s*',
                    'patterns':
                    [
                        {'include': '#cmd_string'},
                    ],
                    'end' : r'\s*(?=,)'
                },
                {
                    'name' : 'meta.control.double_args.separator.{SCOPE}',
                    'begin': r'(?<=,)',
                    'patterns':
                    [
                        {
                            'name' : 'string.unquoted.rval.{SCOPE}',
                            'begin': r'(?<=,)',
                            'patterns':
                            [
                                {'include': '#cmd_string'},
                            ],
                            'end': r'(?=\))'
                        }
                    ],
                    'end': r'(?=\))'
                }
            ],
            'end': r'\)|(?<!\\)\n'
        },

#-- OPERATORS -----------------------------------------------------------------#
        {
            'name' : 'string.unquoted.value.{SCOPE}',
            'begin': r'((:|\+)?=)',
            'beginCaptures':
            {
                1: {'name': 'keyword.operator.assignment.{SCOPE}'}
            },
            'patterns':
            [
                {'include': '#io_string'},
            ],
            'end': r'(?<!\\)\n'
        },
    ],

#-- REPOSITORY ----------------------------------------------------------------#
    'repository':
    {
        'flags':
        {
            'patterns':
            [
                {
                    'name' : 'string.interpolated.flags.percent.{SCOPE}',
                    'match': r'%(f|b|B|e|o|O|d|g)'
                },
                {
                    'name' : 'constant.character.flags.caret.{SCOPE}',
                    'begin': r'\^(c|o)',
                    'patterns':
                    [
                        # %-flags
                    ],
                    'end': r'\^'
                },
            ]
        },
        'variables':
        {
            'patterns':
            [
                {
                    'name' : 'keyword.operator.reference.special.{SCOPE}',
                    'match': r'(\$\((TUP_CWD)|@\((TUP_(PLATFORM|ARCH)))\)',
                    'captures':
                    {
                        2: {'name' : 'support.variable.special.dollar.{SCOPE}'},
                        3: {'name' : 'support.variable.special.at.{SCOPE}'}
                    }
                },
                {
                    'name' : 'keyword.operator.reference.at.{SCOPE}',
                    'match': r'(@\(|\$\((CONFIG_))(.+?)\)',
                    'captures':
                    {
                        2: {'name': 'constant.character.escape.conf_var.{SCOPE}'},
                        3: {'name': 'constant.character.escape.conf_var.{SCOPE}'},
                    }
                },
                {
                    'name' : 'keyword.operator.reference.dollar.{SCOPE}',
                    'match': r'\$\((.+?)\)',
                    'captures':
                    {
                        1: {'name': 'variable.tup_variable.{SCOPE}'},
                    }
                },
            ]
        },
        'macros':
        {
            'patterns':
            [
                {
                    'name' : 'meta.macro.invocation.{SCOPE}',
                    'match': r'(!(?!\s))(.+?)\b',
                    'captures':
                    {
                        1: {'name': 'keyword.operator.macro.prefix.{SCOPE}'},
                        2: {'name': 'entity.other.inherited-class.macro.variable.{SCOPE}'}
                    }
                }
            ]
        },
        'wildcards':
        {
            'patterns':
            [
                {
                    'name' : 'constant.character.wildcard.{SCOPE}',
                    'match': r'\*|\?|\[.+?\]'
                }
            ]
        },
        'io_string':
        {
            'patterns':
            [
                {
                    'name' : 'keyword.operator.order_only_separator.{SCOPE}',
                    'match': r'\|'
                },
                {
                    'include': '#wildcards'
                },
                {
                    'include': '#flags'
                },
                {
                    'include': '#variables'
                },
                {
                    'include': '#macros'
                },
            ]
        },
        'cmd_string':
        {
            'patterns':
            [
                {
                    'include': '#flags'
                },
                {
                    'include': '#variables'
                },
                {
                    'include': '#macros'
                },
            ]
        },
    },
    'uuid': 'F0C79525-E092-4B6B-9A4E-185453A89AE4',
}
