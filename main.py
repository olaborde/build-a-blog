from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)

    def __init__(self, title, author, date_posted):
        self.title = title
        self.description = description
        self.author = author
        self.date_posted = date_posted




blogs = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog = request.form['blog']
        blogs.append(blog)

    return render_template('todos.html',title="Get It Done!", tasks=tasks)


if __name__ == '__main__':
    app.run()