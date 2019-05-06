from flask import Flask

app = Flask(__name__)
# My Secret Key for forms.
app.config['SECRET_KEY'] = 'ThisIsMySecretPassword'

from app import routes