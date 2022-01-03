"""
    discreet
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
    Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


D_BLACK_1 =       "#151515"
D_BLACK_2 =       "#161a1f"
D_BLACK_4 =       "#333333"
D_GRAY_3 =        "#8c8c8c"
D_WHITE_1 =       "#dedede"
D_ORANGE_2 =      "#fd971f"
D_YELLOW_2 =      "#eedc82"
D_AQUAMARINE_4 =  "#458b74"
D_CYAN_1 =        "#457f8b"
D_BLUE_1 =        "#87cefa"
D_PINK_2 =        "#f92672"

class DiscreetStyle(Style):

    default_style = ''

    background_color = D_BLACK_1

    styles = {
        # No corresponding class for the following:
        Text:                      D_WHITE_1,        # class:  ''
        Whitespace:                "",               # class: 'w'
        Error:                     "",               # class: 'err'
        Other:                     "",               # class 'x'

        Comment:                   D_GRAY_3,         # class: 'c'
        Comment.Multiline:         "",               # class: 'cm'
        Comment.Preproc:           "",               # class: 'cp'
        Comment.Single:            "",               # class: 'c1'
        Comment.Special:           "",               # class: 'cs'

        Keyword:                   D_PINK_2,         # class: 'k'
        Keyword.Constant:          "",               # class: 'kc'
        Keyword.Declaration:       "",               # class: 'kd'
        Keyword.Namespace:         "",               # class: 'kn'
        Keyword.Pseudo:            "",               # class: 'kp'
        Keyword.Reserved:          "",               # class: 'kr'
        Keyword.Type:              "",               # class: 'kt'

        Operator:                  D_WHITE_1,        # class: 'o'
        Operator.Word:             "",               # class: 'ow'

        Punctuation:               D_WHITE_1,        # class: 'p'

        Name:                      D_WHITE_1,        # class: 'n'
        Name.Attribute:            D_ORANGE_2,       # class: 'na'
        Name.Builtin:              "",               # class: 'nb'
        Name.Builtin.Pseudo:       "",               # class: 'bp'
        Name.Class:                "",               # class: 'nc'
        Name.Constant:             "",               # class: 'no'
        Name.Decorator:            "",               # class: 'nd'
        Name.Entity:               "",               # class: 'ni'
        Name.Exception:            "",               # class: 'ne'
        Name.Function:             "",               # class: 'nf'
        Name.Property:             "",               # class: 'py'
        Name.Label:                "",               # class: 'nl'
        Name.Namespace:            "",               # class: 'nn'
        Name.Other:                "",               # class: 'nx'
        Name.Tag:                  D_AQUAMARINE_4,   # class: 'nt'
        Name.Variable:             "",               # class: 'nv'
        Name.Variable.Class:       "",               # class: 'vc'
        Name.Variable.Global:      "",               # class: 'vg'
        Name.Variable.Instance:    "",               # class: 'vi'

        Number:                    D_WHITE_1,        # class: 'm'
        Number.Float:              "",               # class: 'mf'
        Number.Hex:                "",               # class: 'mh'
        Number.Integer:            "",               # class: 'mi'
        Number.Integer.Long:       "",               # class: 'il'
        Number.Oct:                "",               # class: 'mo'

        Literal:                   D_WHITE_1,        # class: 'l'
        Literal.Date:              "",               # class: 'ld'

        String:                    D_YELLOW_2,       # class: 's'
        String.Backtick:           "",               # class: 'sb'
        String.Char:               "",               # class: 'sc'
        String.Doc:                "",               # class: 'sd'
        String.Double:             "",               # class: 's2'
        String.Escape:             "",               # class: 'se'
        String.Heredoc:            "",               # class: 'sh'
        String.Interpol:           "",               # class: 'si'
        String.Other:              "",               # class: 'sx'
        String.Regex:              "",               # class: 'sr'
        String.Single:             "",               # class: 's1'
        String.Symbol:             D_BLUE_1,         # class: 'ss'

        Generic:                   "",               # class: 'g'
        Generic.Deleted:           "",               # class: 'gd',
        Generic.Emph:              "",               # class: 'ge'
        Generic.Error:             "",               # class: 'gr'
        Generic.Heading:           "",               # class: 'gh'
        Generic.Inserted:          "",               # class: 'gi'
        Generic.Output:            "",               # class: 'go'
        Generic.Prompt:            "",               # class: 'gp'
        Generic.Strong:            "",               # class: 'gs'
        Generic.Subheading:        "",               # class: 'gu'
        Generic.Traceback:         "",               # class: 'gt'
    }
