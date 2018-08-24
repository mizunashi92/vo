
# coding: utf-8

# In[ ]:

import io
import requests
import webbrowser
import random
import time
import os
import csv
browserExe = "chrome.exe"
url="https://raw.githubusercontent.com/mizunashi92/busster/master/youtube2.csv"
s=requests.get(url).content
io.StringIO(s.decode('utf-8'))


# In[ ]:

veronica= []
with io.StringIO(s.decode('utf-8')) as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        veronica.append(row)


# In[ ]:

while True:
    b = random.randint(0, len(veronica))
    print("Currently playing",veronica[b][0],"\nwith estimated time of",int(veronica[b][1])/60+1, "minutes")
    webbrowser.open(veronica[b][2])
    time.sleep(int(veronica[b][1]) + random.randint(0, int(int(veronica[b][1])/20)))
    os.system("taskkill /f /im "+browserExe)
    time.sleep(random.randint(0,25))    

