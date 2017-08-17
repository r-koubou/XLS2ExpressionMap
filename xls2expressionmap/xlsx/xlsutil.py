# encoding: utf-8

# https://pypi.python.org/pypi/openpyxl
import openpyxl

from ..util import util

"""
Get a Cell array from given sheet instanse and cell string value of Row 1.
"""
def getRowsFromColumnName( sheet, colmnName ):
    for c in range( sheet.ncols ):
        name = sheet.cell( 0, c ).strip()
        if( name == colmnName ):
            return sheet.col_slice( 1, c )
    return []

"""
Get a Cell from given sheet instanse and row index and cell string value of Row 1.
"""
def getValueFromColumnName( sheet, rowIndex, colmnName, defaultValue = None ):

    colmnName = colmnName
    maxColumn =  sheet.max_column

    for c in range( 1, maxColumn ):
        cell = sheet.cell( row = 1, column = c )
        name = cell.value
        if( name == colmnName ):
            cell = sheet.cell( row = rowIndex, column = c )
            if cell.value == None:
                return defaultValue
            return cell.value

    return defaultValue
