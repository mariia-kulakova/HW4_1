from elasticsearch import Elasticsearch
import os

INDEX_CVE = os.environ.get('INDEX_CVE')

def elasticsearch_client():
    es_url = os.environ.get('ES_URL')
    es_token = os.environ.get('ES_TOKEN')

    if not (es_url and es_token):
        print('Not provided ElasticSearch URL and Token!')

    return Elasticsearch(es_url, api_key=es_token)
