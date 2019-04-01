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

def france_pari(url):
    cote_dom = []
    cote_null = []
    cote_ext  =[]
    cote_not_clean = []
    equipe = []
    equipe_dom = []
    equipe_ext = []
    liste = []

    scr = requests.get(url)
    soup = BeautifulSoup(scr.content,'html5lib')


    for elem in soup.find_all("div",attrs = {"class":"odd-event uk-grid"}):
        liste.append(elem.text.strip().replace("\n"," "))

    liste_no_hours = [elem[6:].strip() for elem in liste]

    for elem in liste_no_hours:
        for i,ele in enumerate(elem):
            if ele.isnumeric():
                cote_not_clean.append(elem[i:].split("+")[0].strip())
                equipe.append(elem[:i])

                break

    cote_not_clean = cote_not_clean[1:]

    for elem in cote_not_clean:
        tmp = elem.split(",")

        cote_dom.append(tmp[0] +"."+ tmp[1][:2])

        cote_null.append(tmp[1][-1] +"."+ tmp[2][:2] )
        cote_ext.append(tmp[2][-1] + "." + tmp[-1])
        for x in equipe:
            equipe_dom.append(x.split("/")[0].strip())
            equipe_ext.append(x.split("/")[1].strip())

    cote_dom = [float(elem) for elem in cote_dom]
    cote_null = [float(elem) for elem in cote_null]
    cote_ext  =[float(elem) for elem in cote_ext]

    cotes = tuple(zip(equipe_dom,equipe_ext))
    equipes = list(zip(cote_dom,cote_null,cote_ext))

    return {"france_pari":[[cotes[i],equipes[i]] for i in range(len(equipes))]}
