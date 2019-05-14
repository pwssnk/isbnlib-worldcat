# -*- coding: utf-8 -*-
'''Query the WorldCat service for metadata. '''

# This code is partially based on the (now defunct) isbnlib-dnb module by arangb.
# https://pypi.org/project/isbnlib-dnb/ https://github.com/arangb/isbnlib-dnb

import logging

import bs4
import pycountry

from isbnlib.dev import stdmeta
from isbnlib.dev._bouth23 import u
from isbnlib.dev.webquery import query as wquery

UA = 'isbnlib (gzip)'
SERVICE_URL = 'https://www.worldcat.org/search?q=bn%3A{isbn}&lang={lang}'
QUERY_LANG = 'en'
LOGGER = logging.getLogger(__name__)


def parser_worldcat(data):
    '''Parse the response from the WorldCat service. The input data is the result webpage in html from the search.'''
    records = {}

    soup = bs4.BeautifulSoup(data, features='html.parser')

    try:
        result = soup.find('td', class_='result details')  # We should only need to look at the first entry

        # Extract title
        raw = result.find('div', class_='name').find('a').find('strong').contents[0]
        records['Title'] = str(raw.replace(' :', ':'))   # Fix a error in title markup

        # Extract list of author(s)
        raw = result.find('div', class_='author').contents[0].replace('by ', '')
        records['Authors'] = [atr.replace(';', '') for atr in raw.split('; ')]  # Split and fix another common error

        # Extract language
        langs = [i.contents[0] for i in result.find('div', class_='language').find_all('span', class_='itemLanguage')]
        lang_codes = []
        for lang in langs:
            code = pycountry.languages.lookup(str(lang))
            if code:
                lang_codes.append(code.alpha_2.lower())

        if len(lang_codes) == 1:
            records['Language'] = str(lang_codes[0])
        elif len(lang_codes) > 1:
            records['Language'] = str(', '.join(lang_codes))
        else:
            records['Language'] = ''

        # Extract publisher and year
        raw = result.find('span', class_='itemPublisher').contents[0]
        raw = raw.split(': ')[-1]  # Filter out publisher's seat
        raw = raw.split(', ')
        publisher = raw[0]
        year = raw[-1].replace('[', '').replace(']', '').replace('.', '')

        records['Publisher'] = str(publisher)
        records['Year'] = str(year)

    except (AttributeError, KeyError) as ex:
        LOGGER.debug('Error parsing WorldCat html. Did the layout change?')
        records = {}

    return records


def _mapper(isbn, records):
    '''Make records canonical.
    canonical: ISBN-13, Title, Authors, Publisher, Year, Language
    '''
    # handle special case
    if not records:  # pragma: no cover
        return {}
    # add ISBN-13
    records['ISBN-13'] = u(isbn)
    # call stdmeta for extra cleaning and validation

    return stdmeta(records)


def query(isbn):
    '''Query the WorldCat service for metadata. '''
    data = wquery(
        SERVICE_URL.format(isbn=isbn, lang=QUERY_LANG), user_agent=UA, parser=parser_worldcat)

    if not data:  # pragma: no cover
        LOGGER.debug('No data from WorldCat for isbn %s', isbn)
        return {}

    return _mapper(isbn, data)

