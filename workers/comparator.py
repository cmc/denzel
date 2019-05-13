import celery
import json
import ssdeep
from os import getenv
from lib.compare import fetchssdeep
from lib.slackmessage import send_to_slack
app = celery.Celery('denzel')

with open(getenv('APP_CONFIG_PATH', '/src/config/config.json'), 'r') as f:
    config = json.load(f)
    print(config)
    app.conf.update(BROKER_URL=config['REDIS'],
                    CELERY_RESULT_BACKEND=config['REDIS'])


@app.task(bind=True)
def compare(self, urls):
    """
        This is going to get a huge refactor... eventually
        todos: Caching of results
        proxy config / rotation
        knownbad table (cached ssdeeps of gsuite/aws/sso logins)
    """
    dom_hash_ref = fetchssdeep(urls[0])
    dom_hash_submission = fetchssdeep(urls[1])
    print(dom_hash_ref)
    print(dom_hash_submission)

    result = ssdeep.compare(dom_hash_ref, dom_hash_submission)
    resp = {
        'url': urls[1],
        'ref': urls[0]
    }
    if result > 55:
        resp['result'] = "MATCH"
    else:
        resp['result'] = "NO_MATCH"
    resp['percent'] = int(result)
    send_to_slack(json.dumps(resp))
    return
