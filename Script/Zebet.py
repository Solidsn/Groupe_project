import pandas as pd
import numpy as np
import datetime
import requests
from bs4 import BeautifulSoup
import re
import pickle
from urllib.request import urlopen
import time
import random
import re
import json
import lxml
import logging
import collections
from time import gmtime, strftime
import html5lib
import os


def zebet(url):
        
        
    r = requests.get(url)
    bet = BeautifulSoup(r.content,'html5lib')
    
    cote = []
    for a in bet.find_all("span", attrs = {"class":"pmq-cote uk-width-1-1"}):
        cote.append(a.text)
    
    t1 = []
    t2 = []
    for t in bet.find_all("div", attrs ={"class":"uk-visible-small uk-text-bold uk-margin-left uk-text-truncate"}):
        t1.append(t.text.split('/')[0].strip())
    for e in bet.find_all("div", attrs ={"class":"uk-visible-small uk-text-bold uk-margin-left uk-text-truncate"}):
        t2.append(e.text.split('/')[1].strip())
        
    date = []
    heure = []
    for d in bet.find_all("div", attrs={"class":"bet-time"}):
        date.append(d.text.split(" ")[0])
    for h in bet.find_all("div", attrs={"class":"bet-time"}):
        heure.append(h.text.split(" ")[1])
        
    team1 = cote[0::3]
    nul = cote[1::3]
    team2 = cote[2::3]

    dico_ary = []
  
    for i in range(len(t1)):
        #dico_ary.append([t1[i]:team1[i], "Nul":nul[i], t2[i]:team2[i], "Date":date[i], "Heure":heure[i]])
        dico_ary.append([(t1[i],t2[i]),(float(team1[i]),float(nul[i]), float(team2[i]))])
    return {"Zebet":dico_ary}