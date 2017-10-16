# coding: utf-8

# https://pypi.python.org/pypi/openpyxl
import openpyxl

from .. import constants

"""
Get a Cell from given cells tuple instanse that get from openpyxl.WorkSheet.rows and row index and cell string value of Row 1.
"""
def getValueFromColumnName( rows, rowIndex, columnName, defaultValue = None ):

    i = 0
    for name in rows[ constants.HEADER_ROW_INEDX ]:
        if name.value == columnName:
            v = rows[ rowIndex ][ i ].value
            if( v == None ):
                return defaultValue
            return v
        i += 1

    return defaultValue
