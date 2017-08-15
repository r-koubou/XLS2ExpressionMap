# encoding: utf8

import uuid

def createUUID():
    return uuid.uuid4().fields[ 0 ]

def createUUIDList( listSize ):
    ret = [0] * listSize
    for i in range( listSize ):
          ret[ i ] = uuid.uuid4().fields[ 0 ]

    return ret

def float2int( v, defaultValue = 0 ):
    if( isinstance( v, float ) ):
        return int( v )
    else:
        return defaultValue

def str2int( v, defaultValue = 0 ):
    if( isinstance( v, str ) ):
        return int( v )
    else:
        return defaultValue
