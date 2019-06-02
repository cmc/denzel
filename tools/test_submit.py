import requests
jd = { 'refs': ['https://www.github.com'],
      'domains': ['https://www.google.com/', 'https://www.github.com']
     }

r = requests.post('http://localhost/compare', json=jd)
print(r.content)
