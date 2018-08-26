# coding: utf-8

# https://pypi.python.org/pypi/openpyxl
import openpyxl

from .. import constants

"""
Get a Cell from given cells tuple instanse that get from openpyxl.WorkSheet.rows and row index and cell string value of Row 1.
"""
def getValueFromColumnName( rows, rowIndex, columnName, defaultValue = None ):

    HEADER_ROW_INEDX = getRowIndexCompat( rows )[ 0 ]

    i = 0
    for name in rows[ HEADER_ROW_INEDX ]:
        if name.value == columnName:
            v = rows[ rowIndex ][ i ].value
            if( v == None ):
                return defaultValue
            return v
        i += 1

    return defaultValue


"""
@deprecated Convert to rowindex. This is keep compatibility v0.6 and v0.7.
@return list of modifed index value - [HEADER_ROW_INEDX, START_ROW_INEDX]
"""
def getRowIndexCompat( rows ):
    # V0.7 later mode
    a0 = rows[ 0 ][ 0 ].value
    if a0 == constants.COLUMN_OUTPUTNAME:
        return [ constants.__HEADER_ROW_INEDX, constants.__START_ROW_INEDX ]
    # Switching to V0.6 mode
    else:
        return [ constants.__HEADER_ROW_INEDX_V6, constants.__START_ROW_INEDX_V6 ]
