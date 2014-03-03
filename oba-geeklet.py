#!/usr/bin/python

import ConfigParser
import urllib2 

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

#Reads the key from the configuration file
def ConfigSectionMap(section):
  dict1 = {}
  options = Config.options(section)
  for option in options:
    try:
      dict1[option] = Config.get(section, option)
      if dict1[option] == -1:
        DebugPrint("skip: %s" % option)
    except:
      print("exception on %s!" % option)
      dict1[option] = None
  return dict1

# Sample REST call
# http://api.pugetsound.onebusaway.org/api/where/arrival-and-departure-for-stop/1_75403.xml?key=TEST&tripId=1_15551341&serviceDate=1291536000000&vehicleId=1_3521&stopSequence=42
# http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_75403.xml?key=TEST
def CurrentArrivalsAndDepatruresForStop(stop, key):
  # route 304
  # stop 75190 W-bound 304
  # 6950 S-bound E-Line
  url = "http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_" 
  urlreq = url + str(stop) + ".xml?key=" + key
  print urlreq
  req = urllib2.Request(urlreq)
  response = urllib2.urlopen(req)
  return response.read()

#Given a Stop and Key will return .xml formatted info about that stop
def StopInfo(stop, key):
  #http://api.pugetsound.onebusaway.org/api/where/stop/1_75403.xml?key=TEST
  url = "http://api.pugetsound.onebusaway.org/api/where/stop/1_"
  urlreq = url + str(stop) + ".xml?key=" + key
  print urlreq
  req = urllib2.Request(urlreq)
  response = urllib2.urlopen(req)
  return response.read() 

def main():
  key = ConfigSectionMap("OBA")['key']
  print "OBA access key : %s" % (key)
  stop = 6950
  #print StopInfo(stop, key)
  print CurrentArrivalsAndDepatruresForStop(stop, key)

if __name__ == "__main__":
  main()
