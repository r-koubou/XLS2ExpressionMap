# encoding: utf-8

# Extract expression map data to xlsx format utility
# usage
# python extraxt.py <file.expressionmap>


# MIT License
#
# Copyright (c) 2016 R-Koubou
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

import re
import sys
import html
import itertools

ARGV      = sys.argv[1:]
articulationList = []
colorList        = []
groupList        = []
artiTypeList     = []

if( len(ARGV) == 0 ):
    print("""
usage:
    python extraxt.py <file.expressionmap>
""")
    sys.exit(1)

def match( pattern, line, targetList, dupulicate = True ):
    regex   = re.compile( pattern )
    line    = line.strip()
    match   = re.match( regex, line )
    m       = ""
    if match != None and targetList != None:
        m = match.group( 1 )
        if( not m in targetList and dupulicate == False ):
            targetList.append( m )
        else:
            targetList.append( m )

    return m

fp = open( ARGV[ 0 ], "r", encoding = "utf-8" )
line = fp.readline()
while line:
    match( r"<string\s+name=\"text\"\s+value=\"([^\"]+)\".*",               line, articulationList, False )
    match( r"<int name=\"color\"\s+value=\"([0-9])\"\s*/>",                 line, colorList )
    match( r"<int\s+name=\"articulationtype\"\s+value=\"([0-9])\"/\s*>",    line, artiTypeList )
    match( r"<int\s+name=\"group\"\s+value=\"([0-9])\"\s*/>",               line, groupList )

    line    = fp.readline()

fp.close()

for arti, color, artiType, group, in itertools.zip_longest( articulationList, colorList, artiTypeList, groupList ):

    arti = html.unescape( arti )

    if( artiType == "1" ):
        artiType = "Direction"
    else:
        artiType = "Attribute"

    print( "{arti}\t{color}\t{arti}\t{artiType}\t{group}".format(
        arti = arti,
        color = color,
        artiType = artiType,
        group = group
    ))

