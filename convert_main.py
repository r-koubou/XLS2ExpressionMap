# coding: utf-8

import appinfo
from os import path
import sys

from xls2expressionmap import constants
from xls2expressionmap import convert
from xls2expressionmap.expressionmap import template
from xls2expressionmap.xlsx import xlsutil

def usage():
    print(
"""
XLS2ExpressionMap {version}

2017 (c) {author}
{url}

usage:
    XLS2ExpressionMap <input file> [<input file>] ...

    [parameter]
    <input file>: xlsx file path
""".format( version=appinfo.VERSION, author=appinfo.AUTHOR, url=appinfo.URL )
    )

def main():
    if( len( sys.argv ) < 2 ):
        usage()
        return

    # Checking: xlsx files exist
    for i in sys.argv[1:]:
        if( path.exists( i ) == False ):
            usage()
            return

    for i in sys.argv[1:]:
        print( "#------------------------------------------" )
        print( "# {i}".format( i = i ) )
        print( "#------------------------------------------" )
        outputDir = path.dirname( i )
        p = convert.XLS2ExpressionMap( xlsxFileName = i, outputDir = outputDir )
        p.convert()

if __name__ == '__main__':
    main()
