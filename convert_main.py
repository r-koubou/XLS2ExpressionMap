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
    python XLS2ExpressionMap.py <input file>
    <input file>: xlsx file path
        """
    )

def main():
    if( len( sys.argv ) < 2 ):
        usage()
        return

    p = convert.XLS2ExpressionMap( xlsxFileName = sys.argv[ 1 ] )
    p.convert()

if __name__ == '__main__':
    main()
