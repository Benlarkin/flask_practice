from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Ben'}
    posts = [
        {
            'author': {'username': 'John'},
            'body' : 'Beautiful day in Bellingham!'
        },
        {
            'author': {'username': 'Bennyboo'},
            'body' : 'Beyond the Permafrost!'
        }

    ]
    
    return render_template('index.html', title='Home', user =user, posts = posts)