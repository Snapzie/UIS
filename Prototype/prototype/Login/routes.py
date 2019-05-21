from flask import render_template, url_for, flash, redirect, request, Blueprint
from prototype import app, conn, bcrypt
from prototype.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from prototype.models import Patients, select_Patient

Login = Blueprint('Login', __name__)

@Login.route("/")
@Login.route("/home")
def home():
    return render_template('home.html')

@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = select_Patient(form.id.data, conn)
        if user is not None and user.password == form.password.data:
            login_user(user)
            flash('Login successful.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Login.home'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@Login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Login.login'))