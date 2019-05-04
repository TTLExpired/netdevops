from flask import Flask, render_template
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bill'}
    posts = [
        {
            'author': {'username': 'Bill'},
            'body': 'My first post.'
        },
        {
            'author': {'username': 'Benji'},
            'body': "my boy's first post."
        }
    ]
    return render_template('index.html', title='blabla', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True)