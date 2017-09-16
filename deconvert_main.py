# coding: utf-8

# Convert from Cubase expression map data to csv format for XLS2ExpressionMap

import sys
from xls2expressionmap import deconvert

def usage():
    print(
"""---------------------
  ExpressionMap2Text
  2017 (c) R-Koubou
---------------------
usage:
    * Require Python 3.x
    python ExpressionMap2Text.py <input file> [<input file>] ...
    <input file>: expression map file path
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
        p = deconvert.ExpressionMap2Text( i )
        p.deconvert()

if __name__ == '__main__':
    main()
