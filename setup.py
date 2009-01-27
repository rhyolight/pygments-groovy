# -*- coding: utf-8 -*-
"""
Pygments Groovy Lexer plugin setup file for setuptools
"""
from setuptools import setup

setup(
    name='Groovy'
    version='0.1'
    author='Matthew Taylor',
    author_email='matt.taylor@springsource.com'
    description='Groovy Lexer for Pygments',
    license='BSD',
    url='http://weblog.dangertree.net/pygments-groovy-lexer'
    keywords='groovy grails syntax highlighting'
    packages=find_packages(),
    entry_points='''
        [pygments.lexers]
        groovylexer = lexer.GroovyLexer
    '''
)
