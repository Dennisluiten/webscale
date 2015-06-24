# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:01:00 2015

@author: Dennis
"""

import requests

 # http://krabspin.uci.ru.nl/getcontext.json/?i=1&runid=1&teamid=teamPancake&teampw=eb932e1586902b93a5ca86ff03d5aa90
teamid = "teamPancake"
password = "eb932e1586902b93a5ca86ff03d5aa90"

def getData(runid, i):
    url = "http://krabspin.uci.ru.nl/getcontext.json/?i={}&runid={}&teamid={}&teampw={}".format(i, runid, teamid, password)
    r = requests.get(url)
    return r.json()
    
    
def submitResponse(runid, i, header, adtype, color, productid, price):
    url = "http://krabspin.uci.ru.nl/proposePage.json/?i={}&runid={}&teamid={}&teampw={}&header={}&adtype={}&color={}&productid={}&price={}".format(i, runid, teamid, password, header, adtype, color, productid, price)
    r = requests.get(url)
    return r.json()
    
    
print("This code is executed too")    
print (getData(2, 2))