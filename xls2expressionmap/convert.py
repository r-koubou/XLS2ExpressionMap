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

"""
Convert to xlsx file to Cubase *.expressionmap.
"""
class Xls2ExpressionMap:

    """
    ctor
    """
    def __init__( self, xlsxFileName, outputDir = '.' ):
        self.xlsxFileName = xlsxFileName
        self.book         = openpyxl.load_workbook( xlsxFileName )
        self.outputDir    = outputDir


    """
    Generate articulation xml string from given sheet
    """
    def generateArticulation( sheet ):
        pass

    """
    Generate velocity xml string from given sheet and row index
    """
    def generateVelocity( sheet, row_index ):
        pass

    """
    Generate MIDI CC xml string from given sheet and index(1-based. if multiple, set index>1 ), row index
    """
    def generateCC( sheet, index, row_index ):
        pass

    """
    Generate MIDI Program change xml string from given sheet and row index
    """
    def generatePC( sheet, row_index ):
        pass

    """
    Generate key switch xml string from given sheet
    """
    def generateKeySwitch( sheet ):
        pass

    """
    Convert to Expression map file
    """
    def convert():
        pass
