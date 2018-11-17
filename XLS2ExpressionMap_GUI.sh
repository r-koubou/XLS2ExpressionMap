#!/bin/sh

#----------------------------------------------------------------------------
#
# Launch for GUI with python runtime
#
#----------------------------------------------------------------------------

THISDIR=`dirname "${0}"`
expr "${0}" : "/.*" > /dev/null || THISDIR=`(cd "${THISDIR}" && pwd)`

pushd $THISDIR
    python convert_gui_main.py ${XLSX}
popd
