
# coding: utf-8

# In[13]:


#importing libraries
import pylab as pl
import json
import csv
import urllib2 as urllib
import sys
import pandas as pd
import config


# In[14]:


#Creating system arguments to run the code
if len(sys.argv) != 3:
    print("Invalid number of arguments run as: python get_bus_info_soa238.py <APIKEY> <Bus line>")
    sys.exit()


# In[47]:


#identifying system arguments
key= sys.argv[1]
busline= sys.argv[2]


# In[57]:


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+busline


# In[63]:


#pulling data from URL and reading them
rawdata = urllib.urlopen(url)
decodeddata = rawdata.read().decode("utf-8")
decodeddata = json.loads(decodeddata)
datapath = decodeddata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

try:
    datapath=decodeddata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
except KeyError:
    datapath='N/A'
    
datapath


# In[65]:


print (datapath[0]['MonitoredVehicleJourney']['PublishedLineName'])
loop = 0
for busdata in datapath:
    busdata=busdata['MonitoredVehicleJourney']
    print ('Bus',loop, 'is at latitude', busdata['VehicleLocation']['Latitude'],'&longitude',busdata['VehicleLocation']['Longitude'])
    loop+=1

