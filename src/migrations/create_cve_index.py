from helpers.elasticsearch_helper import elasticsearch_client, INDEX_CVE

def create_cve_index():
    response = elasticsearch_client().indices.create(index=INDEX_CVE)

    if response.meta.status == 200:
        return 'Success!'
    else:
        return 'Creation Failed!'

if __name__ == '__main__':
    create_cve_index()
