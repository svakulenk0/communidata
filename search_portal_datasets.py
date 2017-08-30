#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Aug 30, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Search through the portal datasets

'''
import requests

IDEA = {
            'title': "Musik im Park",
            'description': "Begründung : es gibt fast nirgendwo ein park mit musik ausser wenn man per handy eine musik aufdreht und es währe doch angenehm in einem park öffentliche musik zu haben",
            'category': "FREIZEIT"
        }

AT_SEARCH_API = 'http://data.wu.ac.at/portalwatch/api/v1/search/austrian?q=%s&limit=10&offset=0'


def search_at_portals(keyword):
    api_call = AT_SEARCH_API % keyword
    response = requests.get(api_call)
    return response.json()


def test_search():
    print search_at_portals(IDEA['title'])


if __name__ == '__main__':
    test_search()
