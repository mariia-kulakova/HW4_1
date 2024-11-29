from helpers.elasticsearch_helper import elasticsearch_client, INDEX_CVE
from fastapi import APIRouter
from uuid import uuid4

import os
import requests

router = APIRouter(tags=['Init DB'])

@router.get('/init-db')
def init_db():
    response = requests.get(os.environ.get('CVE_URL'),
                            headers={'accept': 'application/json'})

    cve_data = response.json()

    for cve in cve_data.get('vulnerabilities', []):
        elasticsearch_client().create(index=INDEX_CVE, id=str(uuid4()), body=cve)

    return 'Success!'
