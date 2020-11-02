from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile,BlogForm,CommentForm
from ..models import User,Blog
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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)   



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))  



@main.route('/blog/new', methods=['GET', 'POST'])
@login_required
def newblog():
    """
    View Blog function that returns the BLog page and data
    """
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog_title= blog_form.blog_title.data
        description = blog_form.description.data
        print(blog_title)
        new_blog = Blog(title_blog=blog_title, description=description, user_id=current_user)
        new_blog.save_blog()
        return redirect(url_for('main.blog'))
    title = 'Roro Blog'
    return render_template('blog.html', title=title, blog_form=blog_form)   


@main.route('/blog/display')
@login_required
def blog():
    return render_template('myblogs.html')

