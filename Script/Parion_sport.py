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


def parion_sport(url):

    headers = {'Accept' :'application/json, text/plain, */*'.encode('cp1252'),
    'Accept-Encoding':'gzip, deflate, br'.encode('cp1252'),
    'Accept-Language':'fr-FR'.encode('cp1252'),
    'Cache-Control':'max-age=0'.encode('cp1252'),
    'Connection':'keep-alive'.encode('cp1252'),
    'Cookie':'abp-pselw=abpwfr11006_1443; device_view=full; fdj_status_cookie=true; TCPID=11931104559846318062; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22fc25f63d-1361-4385-8a83-648840dc31e6%22%2C%22options%22%3A%7B%22end%22%3A%222020-04-18T09%3A45%3A59.438Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-484303-%22%2C%22at%22%3A%22%22%2C%22ac%22%3A0%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; cikneeto_uuid=id:cf2bc69e-3470-4040-aa5d-1e8e0a45c874; cikneeto=date:1552905064863; fdj-pac=%7B%22appName%22%3A%22PORTAIL_WEB_PW%22%2C%22appVersion%22%3A%221516%22%2C%22pushInfo%22%3A%22%22%7D; fdj_privacy_cookie=true; TC_OPTOUT=0@@@@@@ALL'.encode('cp1252'),
    'Host':'www.enligne.parionssport.fdj.fr'.encode('cp1252'),
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'.encode('cp1252'),
    'X-LVS-HSToken':'ktNVYXgYJAEgn-80jGBesRtSL98_aOGqNsFJgTKqZPFZGney6O8kSIpkfeNCCgcbX8DGhCiaUVSq_cS88gbRwvRs1ylbD_Rc2Ysqey_O0Y2GaB38hdM9vQzEQvibcNGwOcF-6u_qQE6WlhKNLeBN8w=='.encode('cp1252'),
    }
    
    r = requests.get(url , headers = headers )
    json.loads(r.text)
    x=json.loads(r.text)
    xjson = x['items']
    Parent_n = []
    for elem in xjson :
        if "m" in elem :
            Parent_n.append(elem)
    keys_e = []
    for elem in xjson :
        if "e" in elem :
            keys_e.append(elem)
    dico_e = {}
    for elem in xjson :
        for k  in keys_e :
            if elem == k :
                dico_e[k] = xjson.get(elem).get('desc')
    dico_e = {}
    for elem in xjson :
        for k in Parent_n :
            if k in  xjson.get(elem).get('parent') :
                dico_e[k] =  xjson.get(elem).get('desc')
    match = []
    Team = {}
    Nul = {}
    for elem in xjson :
        if 'p' in  xjson.get(elem).get('parent'):
            match.append(xjson.get(elem).get('desc'))
        if 'm' in  xjson.get(elem).get('parent'):
            Team[xjson.get(elem).get('desc')] = xjson.get(elem).get('price')
            if "N" in xjson.get(elem).get('desc'):
                Nul[dico_e.get(xjson.get(elem).get('parent'))] = xjson.get(elem).get('price')
    match.remove('Ligue 1 Conforama')
    match
    n = []
    for elem in match:
        n.append(elem.split("vs"))
    l = []
    for elem in n :
        dic = {}
        for el in elem :
            dic[el] = Team[el.strip()]
            if el.strip() in Nul :
                dic["Nul"] = Nul[el.strip()]
        l.append(dic)
    dico_alain = {}
    dico_alain["ligue_1_alain"] = l

    return dico_alain
