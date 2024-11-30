from helpers.elasticsearch_helper import elasticsearch_client, extract_source_list, INDEX_CVE
from fastapi import APIRouter

MAX_CVES_COUNT = 10

router = APIRouter(tags=['New CVEs'])

@router.get('/get/new')
def get_new():
    response = elasticsearch_client().search(index=INDEX_CVE, body={
        'size': MAX_CVES_COUNT,
        'sort': {
            'dateAdded': 'desc'
        }
    })

    return extract_source_list(response)
