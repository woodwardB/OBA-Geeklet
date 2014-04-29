#!/usr/bin/python

import json
import time
from pprint import pprint


def infinite_defaultdict():
    return defaultdict(infinite_defaultdict)

sample = open("data1.json", "r")

data = sample.read()

#print 'DATA:',(data)

decoded_data = json.loads(data)

#print type(decoded_data)

#print decoded_data['data']['arrivalsAndDepartures']['routeShortName']

#pprint(decoded_data)

#sample.close()

arrivals_and_departures = decoded_data['data']['entry']['arrivalsAndDepartures']

#print arrivals_and_departures['routeShortName'].keys()

#print decoded_data['data']['arrivalsAndDepartures'][0]['routeShortName']

for buses in decoded_data['data']['entry']['arrivalsAndDepartures']:
    assert isinstance(time.gmtime(buses['predictedDepartureTime']).tm_hour, object)
    print buses['routeShortName'], time.gmtime(buses['predictedDepartureTime']).tm_hour, 'mins'