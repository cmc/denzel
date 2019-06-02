import requests
jd = { 'ref': 'https://www.github.com',
      'domain': 'https://www.google.com/'
     }

r = requests.post('http://localhost/compare', json=jd)
print(r.content)
