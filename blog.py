from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
from flask import session
import os,math
from werkzeug.utils import secure_filename

with open('config.json', 'r') as c:
    params = json.load(c)['params']

local_uri = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER']  = params['upload_location']

if (local_uri):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
mail = Mail(app)

# models


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Post(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String, nullable=True)


@app.route("/")
def home():
    posts = Post.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['number_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['number_posts']):(page-1)*int(params['number_posts'])+ int(params['number_posts'])]
    if page==1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page==last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)

    return render_template('index.html', params=params, posts=posts,prev=prev,next=next)


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if "user" in session and session['user'] == params['admin_user']:
        posts = Post.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')
        if username == params['admin_user'] and password == params['admin_password']:
            session['user'] = username
            posts = Post.query.all()
            return render_template('dashboard.html', params=params, posts=posts)

    return render_template('login.html', params=params)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if (request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        phone = request.form.get("phone")
        entry = Contact(name=name, email=email, message=message,
                        phone=phone, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        # mail.send_message("Hello,This is message from "+name,sender=email,recipients=[params['mail_id']],body= message+'/n'+name)
    return render_template('contact.html', params=params)


@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit(sno):

    if request.method == "POST":
        if (session['user'] == params['admin_user'] and "user" in session):
            title = request.form.get('title')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            slug = request.form.get('slug')
            date = datetime.now()

            if (sno == '0'):
                post = Post(title=title, content=content,
                            img_file=img_file, slug=slug, date=date)
                db.session.add(post)
                db.session.commit()
                return redirect('/admin')
            else:
                post = Post.query.filter_by(sno=sno).first()
                post.sno = sno
                post.title = title
                post.content = content
                post.img_file = img_file
                post.date = date
                post.slug = slug
                db.session.commit()
                return redirect('/edit/'+sno)
    if(sno=='0'):
        return render_template('newPost.html',params=params)
    
    post = Post.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, post=post)

@app.route('/upload',methods=['POST','GET'])
def upload():
    if "user" in session and session['user']==params['admin_user']:
        if request.method=='POST':
                f = request.files['file1']
                f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
                return "Uploaded successfully"


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/admin')
@app.route("/post")
def post():
    return render_template('post.html', params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    return render_template('post.html', post=post, params=params)


@app.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    post = Post.query.filter_by(sno=sno).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/admin')

app.run(debug=True)
