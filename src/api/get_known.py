from helpers.elasticsearch_helper import elasticsearch_client, extract_source_list, INDEX_CVE
from fastapi import APIRouter

MAX_CVES_COUNT = 10

router = APIRouter(tags=['Known CVEs'])

@router.get('/get/known')
def get_known():
    response = elasticsearch_client().search(index=INDEX_CVE, body={
        'size': MAX_CVES_COUNT,
        'query': {
            'match': {
                'knownRansomwareCampaignUse': 'Known'
            }
        }
    })

    return extract_source_list(response)
