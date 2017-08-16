# encoding: utf-8

#-------------------
# built in modules
#-------------------
import os
import sys
import html

#-------------------
# 3rd party modules
#-------------------
# https://pypi.python.org/pypi/openpyxl
import openpyxl

#-------------------
# My Script
#-------------------
from .util import util
from .expressionmap import template
from .xlsx import xlsutil

class Xls2ExpressionMap:

    """
    ctor
    """
    def __init__( self, xlsxFileName, outputDir = '.' ):
        self.xlsxFileName = xlsxFileName
        self.book         = openpyxl.load_workbook( xlsxFileName )
        self.outputDir    = outputDir

    """
    convert
    """
    def convert():
        pass
