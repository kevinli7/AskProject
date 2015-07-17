from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : "DOGE"}
    return render_template('index.html',
                            title='DOGELAND', 
			    user=user)
    
