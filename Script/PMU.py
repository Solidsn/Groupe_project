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

def parse_page(url):
    
    def extract_away_win(soup):
        away = []
        Away_win = []

        for i in soup.find_all("div", attrs={"class":"obet-event-list-grid-formatter-col col-rows col-xs-3"}):
            for e in i.find_all("em", attrs={"class":"trow--event--name"}):
                away.append(e.text.strip().split("//")[1])
        for e in soup.find_all("li", attrs={"class":"col-sm-3 trow--odd--item"}):
            for e in e.find_all('a', attrs={"data-minor-sort":"A"}):
                Away_win.append(e.text.strip())

        return away, Away_win

     # extracting all the draw cotes
    def draws(soup):
        Nul = []
        for e in soup.find_all("li", attrs={"class":"col-sm-3 trow--odd--item"}):
            for e in e.find_all('a', attrs={"data-minor-sort":"D"}):
                Nul.append(e.text.strip())

        return Nul

    # extracting home win cotes

    def extract_home_win(soup):
        home = []
        Home_win =[]
        for i in soup.find_all("div", attrs={"class":"obet-event-list-grid-formatter-col col-rows col-xs-3"}):
            for e in i.find_all("em", attrs={"class":"trow--event--name"}):
                home.append(e.text.strip().split("//")[0])
        for e in soup.find_all("li", attrs={"class":"col-sm-3 trow--odd--item"}):
            for e in e.find_all('a', attrs={"data-minor-sort":"H"}):
                Home_win.append(e.text.strip())



        return home, Home_win
    
    r = requests.get(url)
    html = r.text.strip()
    soup = BeautifulSoup(html, 'html5lib')


    away, Away_win = extract_away_win(soup)

    Nul = draws(soup)

    home, Home_win = extract_home_win(soup)


    detail = []

    for i in range(len(Home_win)):
        detail.append({home[i]:Home_win[i],"Nul":Nul[i],away[i]:Away_win[i]})

    #saving as a pickle file 

    pickle.dump(detail,open('Cote_France-Paris','wb'))

    return detail


    
def pmu(url):
    
    wmn_exp = parse_page(url)
    dico_tashi = []
    for dic in wmn_exp:
        equi1 = list(dic.keys())[0]
        equip2 = list(dic.keys())[2]
        nul = list(dic.keys())[1]
        dico_tashi.append(((equi1.strip(),equip2.strip()),(float(dic[equi1].replace(",",".")),float(dic[nul].replace(",",".")),float(dic[equip2].replace(",",".")))))
            
        
    return {"PMU" : dico_tashi}