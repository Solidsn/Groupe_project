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

from Betclic import betclic
from Betstars import betstars
from France_pari import france_pari
from William import william
from Net_bet import net_bet
from Parion_sport import parion_sport
from PMU import pmu,parse_page
from Zebet import zebet




bet = 'https://www.betclic.fr/football/ligue-1-conforama-e4'
pm = 'https://paris-sportifs.pmu.fr/pari/competition/169/football/ligue-1-conforama'
france = 'https://www.france-pari.fr/competition/96-parier-sur-ligue-1-conforama'
parion = 'https://www.enligne.parionssport.fdj.fr/lvs-api/next/50/p22892?originId=3&lineId=1&breakdownEventsIntoDays=true&pageIndex=0&eType=G&showPromotions=true'
net = 'https://www.netbet.fr/football/france/96-ligue-1-conforama'
wil = 'http://sports.williamhill.com/bet/fr-fr/betting/t/312/France+-+Ligue+1.html'
zeb = "https://www.zebet.fr/fr/competition/96-ligue_1_conforama"
bets = 'https://sports.betstars.fr/sportsbook/v1/api/getCompetitionEvents?competitionId=2152298&marketTypes=MRES%2CSOCCER%3AFT%3AAXB&includeOutrights=false&channelId=11&locale=fr-fr&siteId=32'

#print(betclic(bet))
#print("#"*20)
#print(betstars(bets))
#print("#"*20)
#print(france_pari(france))
#print("#"*20)
#print(william(wil))
#print("#"*20)
#print(net_bet(net))
#print("#"*20)
#print(parion_sport(parion))
#print("#"*20)
#print(pmu(pm))
#print("#"*20)
print(zebet(zeb))