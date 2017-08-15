# encoding: utf-8

# http://pypi.python.org/pypi/xlrd
import xlrd

from ..util import util

"""
Get a Cell array from given sheet instanse and cell string value of Row 1.
"""
def getRowsFromComnName( sheet, colmnName ):
    for c in range( sheet.ncols ):
        name = sheet.cell( 0, c ).strip()
        if( name == colmnName ):
            return sheet.col_slice( 1, c )
    return []

"""
Get a Cell from given sheet instanse and row index and cell string value of Row 1.
"""
def getCellFromColmnName( sheet, rowIndex, colmnName ):

    colmnName = colmnName

    for c in range( sheet.ncols ):
        cell = sheet.cell( 0, c )
        name = cell.value
        if( name == colmnName ):
            return sheet.cell( rowIndex, c )

    return ""

def getGroupValue( sheet, row ):
    group = getCellFromColmnName( sheet, row, "Group" )

    # Since v0.0.5: Colmn "Group" check (+backward compatibility)
    if( group != None and hasattr( group, "value" ) ):
        # float to int saferty
        group = util.float2int( group.value ) - 1

        if( group < 0 ):
            group = 0
    else:
        group = 0

    return group
