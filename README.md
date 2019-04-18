# denzel
checks site content against known good ssdeep hash, identifies matches.

Implements ssdeep piecewise hashing to identify phishing sites, or sites which have a >55% match on our company domain. It compares the returned data from the site and compares. Sites which have a high similarity to ours are considered potential phishing sites, can be blocked on the corporate network and sent for takedown.

Also, Denzel Washington is "the equalizer", and this code checks.. if site content across 2 sites match.. if its.. equal.. yeah you get it.


<img src="https://github.com/cmc/denzel/blob/master/images/denzel.jpg" width="1000" height="500">

<code>
root@ip-172-30-0-111:/home/ubuntu/comparator# sh -x tools/test_submit.sh

curl --header Content-Type: application/json --request POST --data {"domain":"bitmex.com", "source":"trollbox"} http://localhost:5000/compare
  
{"result": "MATCH"}
  
curl --header Content-Type: application/json --request POST --data {"domain":"binance.com", "source":"trollbox"} http://localhost:5000/compare

{"result": "NO_MATCH"}

root@ip-172-30-0-111:/home/ubuntu/comparator#
</code>

Coming soon - 

  - Submit matches direct to OpenDNS API for blocking
  - Crawl several times w/ various UAs
  - Implement regional proxies when requesting content from domains
