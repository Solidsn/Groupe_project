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


def net_bet(url):


      r = requests.get(url)
      soup = BeautifulSoup(r.content,'html5lib')

      equipes1 = []
      equipes2 = []
      for elem in soup.find_all('a', attrs={"class" :"uk-margin-right uk-text-truncate"}):
          try:
              equipes1.append(elem.text.strip().split(' / ')[0])
          except:
              equipes1.append(None)
          try:
              equipes2.append(elem.text.strip().split(' / ')[1])
          except:
              equipes2.append(None)

      domicile = []
      exterieur = []
      Null = []
      liste = soup.find_all('a',attrs={"class" :"nb-load uk-flex"})
      parie =[]
      n=0

      for i in range(0,len(liste),6):
           parie.append(liste[i:i+6][:3])
      for elem in parie:

          domicile.append(elem[0].text)
          Null.append(elem[1].text)
          exterieur.append(elem[2].text)
          if n == len(equipes1)-1:
              break
          n+=1
      ligue_1 = []
      for i in range(len(equipes1)):
          #ligue_1.append({equipes1[i]:domicile[i], "Null":Null[i], equipes2[i]:exterieur[i]})
          dom = float(domicile[i].replace(",","."))
        
          nul = float(Null[i].replace(",","."))

          ext = float(exterieur[i].replace(",","."))

          ligue_1.append([(equipes1[i],equipes2[i]),(dom,nul,ext)])
      dico_marianna = {}
      dico_marianna['Net_bet']=ligue_1

      return dico_marianna
