from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginFrom
app = Flask(__name__)

app.config['SECRET_KEY']='ae86aa41ef54e8af661fd611265e4c1b'
posts = [
    {
        'author': 'Siddhant Mishra',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'April 29, 2019'
    },
    {
        'author': 'Ram Mishra',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'May 1st, 2019'
    },
    {
        'author': 'Harsh Singh',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 30, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' , posts=posts)
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    form=RegistrationForm()
    return render_template('register.html',title='Register',form=form)
         
@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Register',form=form)
                  
     



if __name__=='__main__':
    app.run(debug=True)    

