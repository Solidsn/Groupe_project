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


def betclic(url):


    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html5lib')
    final = []
    for elem in soup.find_all('div',attrs={"class":"match-entry clearfix CompetitionEvtSpe"}):
        cotes = elem.find_all("div",attrs = {"class":"match-odd"})
        cotes = [float(ele.text.strip().replace(",",".")) for ele in cotes]
        equipe = elem.a.text.strip()
        equipe = tuple([ele.lower() for ele in equipe.split(" - ")])

        final.append([equipe,cotes])
    return {"betclic":final}
