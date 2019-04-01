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

def william(url):
        
        
    r = requests.get(url)
    ligue1 = BeautifulSoup(r.content,'html5lib')
    for elem in ligue1.find_all('tbody',attrs={'id':'tup_mkt_grp_tbl_UC_9d8a08d4b13c912153e27659829a27ad'}):
        a=" ".join(elem.text.split()).split('+') 
    date=[]
    infos_equipe=[]
    for elem in a:
        try:
            infos_equipe.append(elem.split('UK')[1].strip())

        except:
            pass
        try:
            date.append(elem.split('UK')[0].strip())
        except:
            pass

    new_date = []
    for ele in date:
        if len(ele) > 12:
            new_date.append(ele[len(ele)-12:])
        elif len(ele) < 12:
            new_date.append("No infos")
        else:
            new_date.append(ele)
    dom = []
    ext = []
    Null = []
    dom_score = []
    ext_score = []
    for elem in infos_equipe:
        for i in range(len(elem)):
            if elem[i].isnumeric():
                tmp1 = elem[:i].split("₋")[0].strip() #Nom de l'équipe domicile

                tmp2 = elem[:i].split("₋")[1].strip()#Nom de l'équipe extérieur

                dom1 = elem[i:].split()[0].strip()
                null = elem[i:].split()[1].strip()
                ext1 = elem[i:].split()[2].strip()
                dom.append(tmp1)
                ext.append(tmp2)
                dom_score.append(dom1)
                ext_score.append(ext1)

                Null.append(null)
                break   
    dico_oumar = {}
    ligue1 = []
    for i in range(len(infos_equipe)):
        #ligue1.append({"date":new_date[i],dom[i]:dom_score[i],"Null":Null[i],ext[i]:ext_score[i]})
        ligue1.append([(dom[i],ext[i]),(float(dom_score[i]),float(Null[i]),float(ext_score[i]))])
    dico_oumar["william"] = ligue1 
    
    return dico_oumar