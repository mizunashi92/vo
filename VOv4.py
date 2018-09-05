
# coding: utf-8

# In[17]:

import io
import requests
import webbrowser
import random
import time
import os
browserExe = "chrome.exe"
import mysql.connector

mydb = mysql.connector.connect(
  host="35.240.178.224",
  user="mizunashi",
  passwd="almukayo",
  database="default"  
)
veronica = mydb.cursor()


# In[ ]:

while True:
    b = random.randint(0, 999)
    c = "Select * from youtube where ID = 'ROW"+str(b)+"'"
    veronica.execute(c)
    karen = veronica.fetchall()
    print("Currently playing",karen[0][0],"\nEstimated time of",int(karen[0][1])/60+0.1, "minutes")
    webbrowser.open(karen[0][2])
    time.sleep(int(karen[0][1]) + random.randint(0, int(int(karen[0][1])/20)))
    os.system("taskkill /f /im "+browserExe)
    time.sleep(random.randint(0,25))    


# In[ ]:



