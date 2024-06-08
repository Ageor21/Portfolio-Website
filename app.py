from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SQLageor88'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_request
def create_tables():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(60))

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')
        
class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

projects = [
    { "id": 1,
     "Project": "Vacation Mobile Application",
      "Programming languages": "Java, SQLite",
      "Link": "https://github.com/Ageor21/Vacation-App"
      },

      { "id": 2,
     "Project": "Appointment Manager Application",
      "Programming languages": "Java, JavaFX MySQL",
      "Link": "https://github.com/Ageor21/Appointment-Manager-"
      },

      { "id": 3,
     "Project": "Interactive World Map",
      "Programming languages": "Typescript, Angular",
      "Link": "https://github.com/Ageor21/Interactive-World-Map"
      },

      { "id": 4,
     "Project": "Student Data Table",
      "Programming languages": "C++",
      "Link": "https://github.com/Ageor21/Student-Data-Table-"
      },

      { "id": 5,
     "Project": "Time and Weather Application",
      "Programming languages": "Pyton, Tkinter",
      "Link": "https://github.com/Ageor21/TIme_Weather_API"
      }
]


@app.route("/")
def portfolio():
    return render_template('home.html', names_projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)