#!/bin/sh

#----------------------------------------------------------------------------
#
# Launch for CLI with python runtime
#
#----------------------------------------------------------------------------

THISDIR=`dirname "${0}"`
expr "${0}" : "/.*" > /dev/null || THISDIR=`(cd "${THISDIR}" && pwd)`

XLSX=$(cd $(dirname $1 ) && pwd)/$(basename ${1})

pushd $THISDIR
    python convert_main.py ${XLSX}
popd
