#!/usr/bin/python

__author__ = 'Brandon Woodward'

import ConfigParser
import urllib2


Config = ConfigParser.ConfigParser()
Config.read("config.ini")

#Global Static Variables
stop_num = 6950


#Reads the key from the configuration file
def config_section_map(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


# Sample REST call
# http://api.pugetsound.onebusaway.org/api/where/arrival-and-departure-for-stop/1_75403.json?key=TEST&tripId=1_15551341&serviceDate=1291536000000&vehicleId=1_3521&stopSequence=42
# http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_75403.json?key=TEST
def current_arrivals_departures(stop_num, key):
    # route 304
    # stop 75190 W-bound 304
    # 6950 S-bound E-Line
    url = "http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_"
    urlreq = url + str(stop_num) + ".json?key=" + key
    print urlreq
    req = urllib2.Request(urlreq)
    response = urllib2.urlopen(req)
    return response.read()


def main():
    key = config_section_map("OBA")['key']
    #print "OBA access key : %s" % (key)
    print current_arrivals_departures(stop_num, key)
    pass


if __name__ == "__main__":
    main()
