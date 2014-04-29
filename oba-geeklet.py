#!/usr/bin/python

import ConfigParser
import urllib2 
import json
import time

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

class OBA(object):
  def __init__(self, route, stop):
    self.bus = bus
    self.route = route

  def route(self):
    return self.route

  def stop(self):
    return self.stop

  def __str__(self):
    return "Gathering information on Route " + self.route + " at stop #" + self.stop

  

#Reads the key from the configuration file
def config_section_map(section):
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
# http://api.pugetsound.onebusaway.org/api/where/arrival-and-departure-for-stop/1_75403.json?key=TEST&tripId=1_15551341&serviceDate=1291536000000&vehicleId=1_3521&stopSequence=42
# http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_75403.json?key=TEST
def CurrentArrivalsAndDepatruresForStop(stop, key):
  # route 304
  # stop 75190 W-bound 304
  # 6950 S-bound E-Line
  url = "http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_" 
  urlreq = url + str(stop) + ".json?key=" + key
  print urlreq
  req = urllib2.Request(urlreq)
  response = urllib2.urlopen(req)
  return response.read()

#Given a Stop and Key will return .json formatted info about that stop
def stop_info(stop, key):
  #http://api.pugetsound.onebusaway.org/api/where/stop/1_75403.json?key=TEST
  url = "http://api.pugetsound.onebusaway.org/api/where/stop/1_"
  urlreq = url + str(stop) + ".json?key=" + key
  print urlreq
  req = urllib2.Request(urlreq)
  response = urllib2.urlopen(req)
  return response.read() 

def main():
  key = config_section_map("OBA")['key']
  print "OBA access key : %s" % (key)
  stop = 6950
  #print stop_info(stop, key)
  arrivals =  CurrentArrivalsAndDepatruresForStop(stop, key)
  print arrivals

  #js = json.load(arrivals)



if __name__ == "__main__":
  main()
