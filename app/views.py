from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : "DOGE"}
    posts = [
        {
            'author': {'nickname': "DogeLuvr69"},
	    'body': 'So many DOGES in the house!!'
	},
	{
	    'author': {'nickname': 'Doge Enthusiast',
	    'body': 'WHO LET THE DOGES OUT'
	}
    ]
    return render_template('index.html',
                            title='DOGELAND', 
			    user=user,
			    posts=posts)
    
