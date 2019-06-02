import celery
import json
import ssdeep
from os import getenv
from lib.compare import fetchssdeep
from lib.slackmessage import send_to_slack
app = celery.Celery('denzel')

with open(getenv('APP_CONFIG_PATH', '/src/config/config.json'), 'r') as f:
    config = json.load(f)
    app.conf.update(BROKER_URL=config['REDIS'],
                    CELERY_RESULT_BACKEND=config['REDIS'])


@app.task(bind=True)
def compare(self, equalize):
    refs = {}
    for domain in equalize['refs']:
        refs[domain] = fetchssdeep(domain)
    suspect_domains = {}
    for domain in equalize['domains']:
        suspect_domains[domain] = fetchssdeep(domain)

    for reference in refs:
        for suspect in suspect_domains:
            print(reference)
            print(suspect)
            r = ssdeep.compare(refs[reference],
                               suspect_domains[suspect]
                              )
            if r > 55:
                resp = {
                    'reference_url': reference,
                    'suspect_url': suspect,
                    'percent': int(r)
                }
                send_to_slack(json.dumps(resp))
    return
