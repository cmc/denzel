import ssdeep
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
  
from raspipe import RasPipe
    
app = Flask(__name__)
  
rp = RasPipe(None)
rp.input_lines.append('starting up...')
rp.render_frame()
 
@app.route('/compare', methods=['POST'])
def compare():

 
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
