# encoding: utf-8

import sys
from cx_Freeze import setup, Executable

exe = Executable (script = 'XLS2ExpressionMap.py', base = None)

setup(  name = 'XLS2ExpressionMap',
        version = '0.0.5',
        description = 'Excel file(*.xlsx) to Cubase Expression Map file converter',
        executables = [exe] )
