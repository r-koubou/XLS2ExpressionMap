# coding: utf-8

# Convert from Cubase expression map data to csv format for XLS2ExpressionMap

import sys
from os import path

from xls2expressionmap import deconvert

def usage():
    print(
"""---------------------
  ExpressionMap2Text
  2017 (c) R-Koubou
---------------------
usage:
    python ExpressionMap2Text.py <input file> [input file] ...
    <input file>: expression map file path
        """
    )

def main():
    if( len( sys.argv ) < 2 ):
        usage()
        return

    for i in sys.argv[1:]:
        print( "{i}".format( i = i ) )
        outputDir = path.dirname( i )
        p = deconvert.ExpressionMap2Text( sourceFileName=i, outputDir=outputDir )
        p.deconvert()

if __name__ == '__main__':
    main()
