# encoding: utf-8

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
    python ExpressionMap2Text.py <input file>
    <input file>: expression map file path
        """
    )

def main():
    if( len( sys.argv ) < 2 ):
        usage()
        return

    p = deconvert.ExpressionMap2Text( sys.argv[1] )
    p.deconvert()

if __name__ == '__main__':
    main()
