from flask import render_template,flash, redirect,request,url_for
from application import app

@app.route('/')
def index():
    return render_template('home.html',title= 'Tanveer')

@app.route('/posts')
def posts():
    user = {'username':'Tanveer'}
    posts = [
        {
            'author':{'username':'Nishant'},
            'body':'Did u see that movie??'
        },
        {
            'author':{'username':'Shubhanshu'},
            'body':'Yeah!!, Avengers Movie is Awesome :-)'
        }
    ]
    return render_template('posts.html', user = user,posts = posts)
