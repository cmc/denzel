import ssdeep
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
  
    
app = Flask(__name__)
  
@app.route('/compare', methods=['POST'])
def compare():
    if not request.json:
        abort(400)
    print(request.json)

 
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
