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


def betstars(url):
        
    r = requests.get(url)
    a = json.loads(r.text)
    i=0
    matchs=[]
    for elem in a['event']:
        matchs.append(a['event'][i].get('name'))
        i = i+1
    i=0
    equipe_domicile=[]
    equipe_externe=[]

    for elem in matchs:
        equipe_domicile.append(matchs[i].split(' vs ')[0])
        equipe_externe.append(matchs[i].split(' vs ')[1])
        i = i+1
    i=0
    cote1=[]

    for elem in a['event']:
        cote1.append(a['event'][i].get('markets')[0].get('selection')[0].get('odds'))
        i = i+1
    i=0
    cote_exterieur=[]

    for elem in cote1:
        cote_exterieur.append(cote1[i].get('dec'))
        i = i+1
    i=0
    cote2=[]

    for elem in a['event']:
        cote2.append(a['event'][i].get('markets')[0].get('selection')[1].get('odds'))
        i = i+1
    i=0
    cote_nul=[]

    for elem in cote2:
        cote_nul.append(cote2[i].get('dec'))
        i = i+1     
    i=0
    cote3=[]

    for elem in a['event']:
        cote3.append(a['event'][i].get('markets')[0].get('selection')[2].get('odds'))
        i = i+1
    i=0
    cote_domicile=[]

    for elem in cote3:
        cote_domicile.append(cote3[i].get('dec'))
        i = i+1
    i=0
    cote_domicile=[]

    for elem in cote3:
        cote_domicile.append(cote3[i].get('dec'))
        i = i+1
    
    Ligue1=[]
    

    for i in range(len(equipe_domicile)):
        
        equipes = (equipe_domicile[i], equipe_externe[i])
        cotes = (float(cote_domicile[i]),float(cote_nul[i]),float(cote_exterieur[i]))
        
        Ligue1.append([equipes,cotes])
        
    dico_lock = {}
    dico_lock['betstars']=Ligue1
    
    return dico_lock