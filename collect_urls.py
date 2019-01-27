#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python module for SEMrush useful functions

@author: j.ibragimova
"""

import pandas as pd
from urllib import request
import json
from bs4 import BeautifulSoup


def get_domains_google(phrases, lang='en'):

    '''
    This function gets the top-1 search result domain for the keywords from Google search results.
    Returns dictionary dict['phrase'] = 'domain'
    For now returns full links, to be updated

    phrases - list of search phrases/keywords, array-like of strings
        of shape (n,)
    lang - two letter language code, string
    '''

    url = 'http://www.google.com/search?q=%s&hl=%s'
    headers = {'User-Agent': 'Mozilla/5.0'}
    result = {}

    for phrase in phrases:
        ph = phrase.lower().strip().replace(' ', '+')
        req = url % (ph, lang)
        req = request.Request(req, headers=headers)
        page = request.urlopen(req)
        soup = BeautifulSoup(page, 'lxml')
        res = soup.find_all('h3', attrs={"class":"r"})[0].find_all('a')[0].get(
                'href')[7:].split('&')[0]
        result[phrase] = res

    return result
