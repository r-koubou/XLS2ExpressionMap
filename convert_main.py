# coding: utf-8

import sys

from xls2expressionmap import constants
from xls2expressionmap import convert
from xls2expressionmap.expressionmap import template
from xls2expressionmap.xlsx import xlsutil

def usage():
    print(
"""---------------------
  XLS2ExpressionMap
  2017 (c) R-Koubou
---------------------
usage:
    * Require Python 3.x
    python XLS2ExpressionMap.py <input file> [<input file>] ...
    <input file>: xlsx file path
        """
    )

def main():
    if( len( sys.argv ) < 2 ):
        usage()
        return

    for i in sys.argv[1:]:
        print( "#------------------------------------------" )
        print( "# {i}".format( i = i ) )
        print( "#------------------------------------------" )
        p = convert.XLS2ExpressionMap( xlsxFileName = i )
        p.convert()

if __name__ == '__main__':
    main()
