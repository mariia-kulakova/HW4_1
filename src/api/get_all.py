from datetime import datetime, timedelta
from helpers.elasticsearch_helper import elasticsearch_client, INDEX_CVE
from fastapi import APIRouter

MAX_CVES_COUNT = 40
DAYS_AGO = 5

router = APIRouter(tags=['All CVEs'])

@router.get('/get/all')
def get_all():
    days_ago_str = datetime.today() - timedelta(days=DAYS_AGO)

    response = elasticsearch_client().search(index=INDEX_CVE, body={
        'size': MAX_CVES_COUNT,
        'sort': {
            'dateAdded': 'desc'
        },
        'query': {
            'bool': {
                'filter': {
                    'range' : {
                        'dateAdded' : { 'gte' : days_ago_str }
                    }
                }
            }
        }
    })

    return [
        cve['_source'] for cve in response.get('hits', {}).get('hits', {})
    ]
