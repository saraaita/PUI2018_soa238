
# coding: utf-8

# In[5]:


import pylab as pl
import json
import csv
import urllib2 as urllib
import sys
import pandas as pd


# In[9]:


#Creating system arguments to run the code
if len(sys.argv) != 3:
    print("Invalid number of arguments run as: python get_bus_info_soa238.py <APIKEY> <Bus_line> <BUS_LINE.csv>")
    sys.exit()


# In[18]:


#identifying system arguments
key= sys.argv[1]
busline= sys.argv[2]


# In[19]:


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+busline


# In[12]:


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


# In[13]:


#Creating a dataframe for bus location and status data
loop = 0
for busdata in datapath:
    busdata=busdata['MonitoredVehicleJourney']
    loop+=1
try:
    status=busdata['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
except KeyError:
    status='N/A'
try:
    stop=busdata['OnwardCalls']['OnwardCall'][0]['StopPointName']
except KeyError:
    stop='N/A'
df=pd.DataFrame(columns=[busdata['VehicleLocation']['Latitude'],busdata['VehicleLocation']['Longitude'],busdata['OnwardCalls']['OnwardCall'][0]['StopPointName'],busdata['VehicleLocation']['Longitude'],busdata['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']])


# In[14]:


df.loc[loop] = [busdata['VehicleLocation']['Latitude'],busdata['VehicleLocation']['Longitude'],busdata['OnwardCalls']['OnwardCall'][0]['StopPointName'],busdata['VehicleLocation']['Longitude'],busdata['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']]
df


# In[17]:


#Exporting dataframe into csv
df.to_csv('busline.csv')

