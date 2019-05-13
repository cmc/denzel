import requests
jd = { 'ref': 'https://www.google.com/',
      'domain': 'https://www.google.com/'
     }

r = requests.post('http://localhost/compare', json=jd)
