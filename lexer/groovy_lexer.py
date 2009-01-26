"""
    Lexer for the Groovy programming language
    http://groovy.codehaus.org
"""

from pygments.lexer import ExtendedRegexLexer

class GroovyLexer(ExtendedRegexLexer):
    name = 'Groovy'
    aliases = ['groovy']
    filenames = ['*.groovy']
    mimetypes = []
