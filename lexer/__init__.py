# -*- coding: utf-8 -*-
"""
    Lexer for the Groovy language.
    http://groovy.codehaus.org

    :copyright: 2009 Matthew Taylor
    :license: BSD, see LICENSE for more details.
"""

from pygments.scanner import Scanner
from pygments.lexer import RegexLexer, include, bygroups, using, \
                           this
from pygments.util import get_bool_opt, get_list_opt
from pygments.token import \
     Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, \
     Error

__all__ = ['GroovyLexer']