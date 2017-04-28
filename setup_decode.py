# encoding: utf-8

import sys
from cx_Freeze import setup, Executable

exe = Executable (script = 'ExpressionMap2Csv.py', base = None)

setup(  name = 'ExpressionMap2Csv',
        version = '0.0.1',
        description = ' Cubase Expression Map file to csv converter',
        executables = [exe] )
