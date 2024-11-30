from helpers.elasticsearch_helper import elasticsearch_client, INDEX_CVE
from fastapi import APIRouter
from uuid import uuid4
from json import loads

import os
import requests

CVES_FILENAME = 'known_exploited_vulnerabilities.json'

router = APIRouter(tags=['Init DB'])

def retrieve_cves():
    with open(CVES_FILENAME, 'r') as file:
        cves = loads(file.read())

        return cves


@router.get('/init-db')
def init_db():
    cve_data = retrieve_cves()

    for cve in cve_data.get('vulnerabilities', []):
        elasticsearch_client().create(index=INDEX_CVE, id=str(uuid4()), body=cve)

    return 'Success!'
