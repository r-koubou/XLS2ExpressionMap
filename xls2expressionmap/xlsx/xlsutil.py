# encoding: utf-8

# MIT License
#
# Copyright (c) 2017 R-Koubou
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# http://pypi.python.org/pypi/xlrd
import xlrd

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
