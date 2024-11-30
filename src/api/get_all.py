from helpers.date_time_helper import days_ago_str
from helpers.elasticsearch_helper import elasticsearch_client, extract_source_list, INDEX_CVE
from fastapi import APIRouter

MAX_CVES_COUNT = 40
DAYS_AGO = 5

router = APIRouter(tags=['All CVEs'])

@router.get('/get/all')
def get_all():

    response = elasticsearch_client().search(index=INDEX_CVE, body={
        'size': MAX_CVES_COUNT,
        'sort': {
            'dateAdded': 'desc'
        },
        'query': {
            'bool': {
                'filter': {
                    'range': {
                        'dateAdded': { 'gte': days_ago_str(DAYS_AGO) }
                    }
                }
            }
        }
    })

    return extract_source_list(response)
