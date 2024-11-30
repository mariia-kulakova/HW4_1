from helpers.elasticsearch_helper import elasticsearch_client, extract_source_list, INDEX_CVE
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

    return extract_source_list(response)
