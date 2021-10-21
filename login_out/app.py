from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''' + \
                                        '@localhost:3306/mydb'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Person(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    pwd = db.Column(db.String(80))

@login_manager.user_loader
def load_user(id):
    return Person.query.get(int(id))

class LoginForm(FlaskForm):
    id = StringField('id', validators=[InputRequired()])
    pwd = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Person.query.filter_by(id=form.id.data).first()
        if user:
            if user.pwd == form.pwd.data:
            # if check_password_hash(user.pwd, form.pwd.data):
                login_user(user, remember=form.remember.data)
                return redirect("engineer_profile")

        return '<h1>Invalid ID or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)
    
@app.route('/engineer_profile')
@login_required
def dashboard():
    return render_template('engineer_profile.html', name=current_user.id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
