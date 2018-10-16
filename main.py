from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
  

    def __init__(self,title, description):
        # self.id = id
        self.title = title
        self.description = description
      




blogs = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog = request.form['blog']
        blogs.append(blog)

    return render_template('index.html')


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    return render_template('newpost.html')
@app.route('/addpost', methods=['POST', 'GET'])
def addpost(): 
    title = request.form['title']
    description = request.form['description']

    blog_entry = Blog(title=title, description=description)
    db.session.add(blog_entry)
    db.session.commit()

    return redirect(url_for('blog'))   

@app.route('/blog', methods=['POST', 'GET'])
def blog():
    return render_template('blog.html')
  

if __name__ == '__main__':
    app.run()