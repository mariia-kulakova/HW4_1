from helpers.elasticsearch_helper import elasticsearch_client, INDEX_CVE
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

    return [
        cve['_source'] for cve in response.get('hits', {}).get('hits', {})
    ]
