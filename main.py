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
    publisher = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime)
  

    def __init__(self,title, description, publisher, date_posted):
        # self.id = id
        self.title = title
        self.description = description
        self.publisher = publisher
        self.date_posted = datetime.now()
      


blogs = []

@app.route('/', methods=['POST', 'GET'])
def index():

    blogs = Blog.query.all()

    # if request.method == 'POST':
    #     blog = request.form['blog']
    #     blogs.append(blog)

    return render_template('index.html', blogs=blogs)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    return render_template('newpost.html')
@app.route('/addpost', methods=['POST', 'GET'])
def addpost(): 
    title = request.form['title']
    description = request.form['description']
    publisher = request.form['publisher']
    blog_entry = Blog(title=title, description=description, publisher=publisher, date_posted=datetime.now())
    db.session.add(blog_entry)
    db.session.commit()

    return redirect(url_for('index'))   

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).one()
    date_posted =blog.date_posted.strftime('%B %d, %Y')
    return render_template('blog.html', blog=blog, date_posted=date_posted)
  

if __name__ == '__main__':
    app.run()

    