import json
import logging
import ssdeep
import requests
from os import getenv
from flask import Flask
from flask import request, abort

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config.from_json(
    getenv('APP_CONFIG_PATH',
           '/src/config/config.json'),
    silent=False
)


def send_to_slack(text):
    data = {
        'text': str(text),
        'username': 'HAL',
        'icon_emoji': ':robot_face:'
    }

    response = requests.post(app.config['SLACK_WEBHOOK'], data=json.dumps(
        data), headers={'Content-Type': 'application/json'})

    logging.info('Response: ' + str(response.text))
    logging.info('Response code: ' + str(response.status_code))


@app.route('/compare', methods=['POST'])
def compare():
    if not request.json:
        abort(400)

    logging.info(request.json)
    try:
        domain = request.json['domain']
        logging.info(domain)
        dom_hash_bitmex = ssdeep.hash(
            requests.get("https://www.bitmex.com", verify=False).text)
        dom_hash_submission = ssdeep.hash(
            requests.get("https://" + domain, verify=False).text)
        result = ssdeep.compare(dom_hash_bitmex, dom_hash_submission)
        logging.info(dom_hash_bitmex)
        logging.info(dom_hash_submission)
        logging.info(result)
    except Exception as e:
        logging.info(e)

    resp = {}
    resp['domain'] = domain
    if result > 55:
        resp['result'] = "MATCH"
    else:
        resp['result'] = "NO_MATCH"
    send_to_slack(resp)
    return json.dumps(resp)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
