from helpers.elasticsearch_helper import elasticsearch_client, INDEX_CVE
from fastapi import APIRouter

router = APIRouter(tags=['Get CVEs by key'])

@router.get('/get')
async def get_by_key(query):
    response = elasticsearch_client().search(index=INDEX_CVE, body={
        'query': {
            'multi_match': {
                'query': query,
                'fields': ['*']
            }
        }
    })

    return [
        cve['_source'] for cve in response.get('hits', {}).get('hits', {})
    ]
