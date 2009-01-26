"""
Pygments plugin
"""
from setuptools import setup

setup(
    name='Groovy'
    version='0.1'
    author='Matthew Taylor',
    description='Groovy Lexer for Pygments',
    packages=['lexer'],
    entry_points='''
    [pygments.lexers]
    groovylexer = lexer.Groovy
    '''
)
