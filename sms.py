# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import os
import psutil
import time

while True:
   
    load1, load5, load15  = psutil.getloadavg()
    cpu_usage = (load15/os.cpu_count())*100
    ram_usage = psutil.virtual_memory()[2]
    
    if cpu_usage>75 or ram_usage>75:
        client = Client("AC87e7dc1e314180e2ea0e462fe18d27b0", "5f18e202c54954de4352f857c73aa996")
        client.messages.create(to="+351916311649", from_="+16087361267", body="Pi Alert : CPU or RAM bigger thant 75%")
    
    time.sleep(900)