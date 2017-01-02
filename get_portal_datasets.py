#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 2, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Collect metadata of the portal datasets

'''

import requests
import pickle
# from generate_wordcloud import generate_wordcloud

PORTAL_WATCH_API = 'http://data.wu.ac.at/portalwatch/api/v1/portal/'


def get_descriptions_of_all_portal_datasets(portal_id, snapshot='1643'):
    # Get the list of all portal datasets, e.g. http://data.wu.ac.at/portalwatch/api/v1/portal/www_opendataportal_at/1643/datasets
    datasets_dump = 'datasets/'+portal_id+'_'+snapshot+'.json'
    try:
        with open(datasets_dump, 'r') as infile:
            datasets = pickle.load(infile)
    except:
        datasets_api = PORTAL_WATCH_API+'/'.join([portal_id, snapshot, 'datasets'])
        response = requests.get(datasets_api)
        datasets = response.json()
        with open(datasets_dump, 'w') as outfile:
            pickle.dump(datasets, outfile)
    # Using "id", get the metadata for a dataset, e.g. http://data.wu.ac.at/portalwatch/api/v1/portal/www_opendataportal_at/1643/dataset/c4feea62-92d8-4855-a2b5-98338a0ffe41
    descriptions = []
    descriptions_dump = 'datasets/%s_%s_titles.txt' % (portal_id, snapshot)
    with open(descriptions_dump, 'w') as outfile:
        print len(datasets), 'datasets in', portal_id, 'portal'
        for dataset in datasets[:2]:
            dataset_id = dataset['id']
            meta_api = PORTAL_WATCH_API+'/'.join([portal_id, snapshot, 'dataset', dataset_id])
            response = requests.get(meta_api).json()
            try:
                meta = response[0]['raw']
                description = meta['title']
                outfile.write(description.encode('utf-8')+'\n')
                # description = meta['notes']
                descriptions.append(description)
            except:
                print response
    return descriptions

    # All available snapshots (yyww), e.g. http://data.wu.ac.at/portalwatch/api/v1/portal/www_opendataportal_at/snapshots
    # SNAPSHOTS_API = ''


# def dump_descriptions():
#     # portal_id = 'www_opendataportal_at'
#     portal_id = 'data_gv_at'
#     descriptions_dump = 'datasets/%s_titles.txt' % portal_id
#     descriptions = get_descriptions_of_all_portal_datasets(portal_id)
#     print descriptions
#     with open(descriptions_dump, 'w') as outfile:
#         outfile.writelines("%s\n" % l for l in descriptions)


def test_get_descriptions_of_all_portal_datasets():
    # data.gv.at
    portal_id = 'data_gv_at'
    # portal_id = 'www_opendataportal_at'
    descriptions = get_descriptions_of_all_portal_datasets(portal_id)
    assert descriptions
    # generate_wordcloud(' '.join(descriptions))


if __name__ == '__main__':
    test_get_descriptions_of_all_portal_datasets()
    # dump_descriptions()