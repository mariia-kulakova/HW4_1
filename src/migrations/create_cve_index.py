from elasticsearch import Elasticsearch
import os

INDEX_CVE = os.environ.get('INDEX_CVE')

def elasticsearch_client():
    es_url = os.environ.get('ES_URL')
    es_token = os.environ.get('ES_TOKEN')

    if not (es_url and es_token):
        print('Not provided ElasticSearch URL and Token!')

    return Elasticsearch(es_url, api_key=es_token)

def create_cve_index():
    response = elasticsearch_client().indices.create(index=INDEX_CVE)

    if response.meta.status == 200:
        print('Success!')
    else:
        print('Creation Failed!')

if __name__ == '__main__':
    create_cve_index()
