#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 2, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Collect metadata of the portal datasets

'''

import requests


PORTAL_WATCH_API = 'http://data.wu.ac.at/portalwatch/api/v1/portal/'


def get_descriptions_of_all_portal_datasets(portal_id, snapshot='1643'):
    # Get the list of all portal datasets, e.g. http://data.wu.ac.at/portalwatch/api/v1/portal/www_opendataportal_at/1643/datasets
    datasets_api = PORTAL_WATCH_API+'/'.join([portal_id, snapshot, 'datasets'])
    response = requests.get(datasets_api)
    datasets = response.json()
    # Using "id", get the metadata for a dataset, e.g. http://data.wu.ac.at/portalwatch/api/v1/portal/www_opendataportal_at/1643/dataset/c4feea62-92d8-4855-a2b5-98338a0ffe41
    descriptions = []
    for dataset in datasets[:10]:
        dataset_id = dataset['id']
        meta_api = PORTAL_WATCH_API+'/'.join([portal_id, snapshot, 'dataset', dataset_id])
        response = requests.get(meta_api)
        meta = response.json()[0]['raw']
        # title = meta['title']
        description = meta['notes']
        descriptions.append(description)
    return descriptions

    # All available snapshots (yyww), e.g. http://data.wu.ac.at/portalwatch/api/v1/portal/www_opendataportal_at/snapshots
    # SNAPSHOTS_API = ''


def test_get_descriptions_of_all_portal_datasets():
    # data.gv.at
    # portal_id = 'data_gv_at'
    portal_id = 'www_opendataportal_at'
    descriptions = get_descriptions_of_all_portal_datasets(portal_id)
    print descriptions


if __name__ == '__main__':
    test_get_descriptions_of_all_portal_datasets()