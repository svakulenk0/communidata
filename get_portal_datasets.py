#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 2, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Collect metadata of the portal datasets

'''
import os
import requests
import pickle


PORTAL_WATCH_API = 'http://data.wu.ac.at/portalwatch/api/v1/portal/'
LATEST_SNAPSHOT = '1702'  # format: yyww (year/week)
AT_PORTALS = ['www_opendataportal_at', 'data_gv_at']  # ids of the austrian open data portals


def get_descriptions_of_all_portal_datasets(portal_id, snapshot=LATEST_SNAPSHOT):
    '''
    Get description metadata for all datasets for a given portal 
    '''
    # Get the list of all portal datasets 
    # e.g. http://data.wu.ac.at/portalwatch/api/v1/portal/www_opendataportal_at/1643/datasets
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
    # Using "id", get the metadata for a dataset
    # e.g. http://data.wu.ac.at/portalwatch/api/v1/portal/www_opendataportal_at/1643/dataset/c4feea62-92d8-4855-a2b5-98338a0ffe41
    descriptions = []
    descriptions_dump = 'datasets/%s_%s_titles.txt' % (portal_id, snapshot)
    with open(descriptions_dump, 'w') as outfile:
        print len(datasets), 'datasets in', portal_id, 'portal'
        for dataset in datasets:
            dataset_id = dataset['id']
            meta_api = PORTAL_WATCH_API + '/'.join([portal_id, snapshot, 'dataset', dataset_id])
            # make sure we receive all the data from the API
            success = False
            while not success:
                response = requests.get(meta_api).json()
                try:
                    meta = response[0]['raw']
                    description = meta['title']
                    outfile.write(description.encode('utf-8')+'\n')
                    # description = meta['notes']
                    descriptions.append(description)
                    success = True
                except:
                    print response
    print len(descriptions), 'descriptions retrieved'
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
    '''
    Test get description metadata for all datasets for a given portal 
    '''
    portal_ids = AT_PORTALS
    for portal_id in portal_ids:
        descriptions = get_descriptions_of_all_portal_datasets(portal_id)
        assert descriptions


def download_portal_files(portal_id, snapshot=LATEST_SNAPSHOT, formats=['csv']):
    '''
    Download all datasets from a given portal
    * formats <list> - download only the files with the specified extensions
    '''
    print portal_id, "data loading.."
    api_call = PORTAL_WATCH_API + '%s/%s/resources'  % (portal_id, snapshot)
    response = requests.get(api_call)
    file_urls = response.json()
    print len(file_urls), 'files found'
    csv_urls = [url for url in file_urls if url[-3:]=='csv']
    print len(csv_urls), 'csvs found'
    output_folder = 'datasets/%s/csvs/' % portal_id
    # make sure the folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for url in csv_urls:
        response = requests.get(url)
        if response.status_code == 200:
            filename = url.replace('/','_')
            # print filename
            # print response.headers['content-type']
            with open(output_folder+filename, 'wb') as f:
                f.write(response.content)


def test_download_portal_files():
    '''
    Test download all datasets from a given portal 
    '''
    portal_ids = AT_PORTALS
    for portal_id in portal_ids:
        download_portal_files(portal_id)


if __name__ == '__main__':
    test_download_portal_files()
