import json
import logging
import ssdeep
import requests
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
  
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
  
@app.route('/compare', methods=['POST'])
def compare():
    if not request.json:
        abort(400)

    logging.info(request.json)
    try:
        domain = request.json['domain']
        logging.info(domain)
        dom_hash_bitmex = ssdeep.hash(requests.get("https://www.bitmex.com", verify=False).text)
        dom_hash_submission =  ssdeep.hash(requests.get("https://" + domain, verify=False).text)
        result = ssdeep.compare(dom_hash_bitmex, dom_hash_submission)
        logging.info(dom_hash_bitmex)
        logging.info(dom_hash_submission)
        logging.info(result)
    except Exception as e:
        logging.info(e)
    return json.dumps(request.json)

 
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
