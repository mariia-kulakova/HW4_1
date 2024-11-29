from fastapi import APIRouter

router = APIRouter(tags=['Info Page'])

@router.get('/info')
def info():
    return {
        'app_name': 'CVEs filter',
        'version': '1.0',
        'description': 'Filter CVEs by creation date, by key, and by known ransomware campaign use',
        'author': 'Mariia Radzhapova'
    }
