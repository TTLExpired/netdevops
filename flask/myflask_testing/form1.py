from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import input_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MyLittleSecret'


class LoginForm(FlaskForm):
    ''' This is our class form. It inherits from flask_wtf FlaskForm '''

    # wtform is our main engine:
    username = StringField('username', validators=[input_required()])
    password = PasswordField('password', validators=[input_required()])

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return f'Thank you {form.username.data}'
    # Pass the completed form to the template!
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
