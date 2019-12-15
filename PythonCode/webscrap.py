import os
from bs4 import BeautifulSoup
import time
import requests
import xml
import csv 
import xml.etree.ElementTree as et
#from parser import *
count = 0
while True:
    r = requests.get('https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN')
    soup = BeautifulSoup(r.text,"xml")
    Main_url = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span')
    print("The current price is :" + str(Main_url.text))

    '''f r.status_code == 200:
        print("Good Connection")
    elif r.status_code == 400:
        print("Bad gateway")
    count+= 1
print("function is working\n")
time.sleep(1)
if count == 10:
    exit(1)'''








    





    