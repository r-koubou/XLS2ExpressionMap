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
# http://pypi.python.org/pypi/xlrd
import xlrd

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
        self.book         = xlrd.open_workbook( xlsxFileName )
        self.outputDir    = outputDir

    """
    convert
    """
    def convert():
        pass
