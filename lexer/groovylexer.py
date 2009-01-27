# -*- coding: utf-8 -*-
"""
    Lexer for the Groovy programming language
    http://groovy.codehaus.org
"""

from pygments.lexer import JavaLexer

class GroovyLexer(JavaLexer):
    name = 'Groovy'
    aliases = ['groovy']
    filenames = ['*.groovy']
    mimetypes = ['text/x-groovy']
