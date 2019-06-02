import requests
jd = { 'refs': ['https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin', 'https://bitmex.com'],
      'domains': ['https://www.google.com/', 'https://www.github.com', 'https://bitmex.com']
     }

r = requests.post('http://localhost/compare', json=jd)
print(r.content)
