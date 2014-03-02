#!/usr/bin/python

import ConfigParser
import 

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
#

def CurrentArrivalsAndDepatrures(stop, route):




def main():
  key = ConfigSectionMap("OBA")['key']
  print "OBA access key : %s" % (key)

if __name__ == "__main__":
  main()
