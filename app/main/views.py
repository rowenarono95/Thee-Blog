from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile,BlogForm,CommentForm
from ..models import User
from ..request import get_quote
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home - Roro blog website'
    content = "WELCOME TO THEE BLOG WEBSITE"
    quote = get_quote()

    return render_template('index.html', title = title,content = content,quote = quote)

