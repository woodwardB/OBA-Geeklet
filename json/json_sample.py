#!/usr/bin/python

import json

#def walk(node):
#    """ iterate tree in pre-order depth-first search order """
#    yield node
#    for child in node.children:
#        for n in walk(child):
#            yield n


def walkDict( aDict, visitor, path=() ):
    for  k in aDict:
        if k == 'attrs':
            visitor( path, aDict[k] )
        elif type(aDict[k]) != dict:
            pass
        else:
            walkDict( aDict[k], visitor, path+(k,) )

def printMe( path, element ):
    print path, element

def filterFor( path, element ):
    if element['id'] == '4130-2-2':
        print path, element



sample = open("data.json", "r")

data = sample.read()

#print 'DATA:',(data)

decoded_data = json.loads(data)



#print decoded_data


print type(decoded_data)


#for key0 in decoded_data['data']:
	#for key1 in decoded_data['data'][key0]:
	#	print key1, decoded_data['data'][key0]
	#print key, decoded_data['data'][key]

