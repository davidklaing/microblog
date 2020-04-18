from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'David'},
            'body': 'I agree, it was dope.'
        }
    ]
    return render_template('index.html', user=user, posts=posts)