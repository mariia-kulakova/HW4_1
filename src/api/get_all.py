from helpers.date_time_helper import days_ago
from helpers.elasticsearch_helper import elasticsearch_client, extract_source_list, INDEX_CVE
from fastapi import APIRouter

MAX_CVES_COUNT = 40

# 4 days ago + today = last 5 days
DAYS_AGO = 4

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
                        'dateAdded': { 'gte': str(days_ago(DAYS_AGO)) }
                    }
                }
            }
        }
    })

    return extract_source_list(response)
