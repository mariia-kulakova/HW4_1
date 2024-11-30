Progect setup locally to run in Debugger mode:

1) git clone git@github.com:mariia-kulakova/HW4_1.git

2) cd HW4_1

3) sudo apt install python3.10-venv

4) python3.10 -m venv ./

5) source ./bin/activate

6) pip install -r requirements.txt

7) open src file in vscode editor and add here debugger config file (.vscode/launch.json).
Use example-launch.json as pattern where change ES_URL (ElasticSearch endpoint url) and
ES_TOKEN (ElasticSearch encrypted token)

8) open migrations/create_cve_index.py and run current file with Debugger
or without (ES_URL and ES_TOKEN must be set as system ENV vars)
This migration creates 'cve' index in ElasticSearch DB

9) run FastAPI (use f5 button shortcut)

Server URL:
http://0.0.0.0:6980/

Routes:
/init-db - saves data from known_exploited_vulnerabilities.json to index 'cve' in ElasticSearch
/info - returns json with app and author info
/get/all - returns json with CVE in the last 5 days. Maximum 40 CVE
/get/new - returns json with newest 10 CVE
/get/known - returns json with CVE in which knownRansomwareCampaignUse - Known, maximum 10
/get?query="key" - returns json with CVE that contain the keyword
