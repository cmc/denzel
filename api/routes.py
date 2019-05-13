import json
import ssdeep
import requests
import logging
from api import app
from lib import compare, slackmessage
from workers import comparator
from flask_restful import Resource, request, abort


class Compare(Resource):
    def post(self):
        if not request.json:
            abort(400)
        logging.info(request.json)
        urls = []
        urls.append(request.json['ref'])
        urls.append(request.json['domain'])
        job  = comparator.compare.delay(urls)
        return "OK"

    def get(self):
        return "OMEC THE TEMPLE GOD"
