# denzel
 REST service, accepts submissions of domains and checks site content against known good site, returns match status.

Implements ssdeep piecewise hashing to identify phishing sites, or sites which have a >55% content match on our company site. It compares the returned html/data from the submitted site and compares hashes with our known good site. Submitted domains which have a high content similarity to ours are considered potential phishing sites. These can then be blocked on the corporate network and sent for takedown.

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

  - Submit matches (suspected phish domains) direct to OpenDNS API for blocking
  - db backed domain whitelist
  - Crawl several times w/ various UAs
  - Implement regional proxies when requesting content from domains
  - Capture and store the hostile site DOM at time of crawl, request headers + screenshot of the hostile site to supply in takedown communications as evidence of bad faith of behalf of the registrant.
