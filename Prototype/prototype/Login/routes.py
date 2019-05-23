from flask import render_template, url_for, flash, redirect, request, Blueprint
from prototype import conn
from prototype.forms import LoginForm
from flask_login import login_user, current_user, logout_user
from prototype.models import select_Patient, get_Prescriptions, get_History, get_Diagnoses

Login = Blueprint('Login', __name__)

@Login.route("/receptfornyelse")
def receptfornyelse():
    p = get_Prescriptions(current_user.get_id(), conn)
    return render_template('receptfornyelse.html', percs=p)

@Login.route("/meddelser")
def meddelelser():
    return render_template('meddelelser.html')

@Login.route("/aftaler")
def aftaler():
    return render_template('aftaler.html')

@Login.route("/historik")
def historik():
    h = get_History(current_user.get_id(), conn)
    return render_template('historik.html', history=h)

@Login.route("/sundhedsdata")
def sundhedsdata():
    d = get_Diagnoses(current_user.get_id(), conn)
    return render_template('sundhedsdata.html', diagnoses=d)

@Login.route("/fahjaelp")
def fahjaelp():
    return render_template('fahjaelp.html')

@Login.route("/")
@Login.route("/profil")
def profil():
    if not current_user.is_authenticated:
        return redirect(url_for('Login.login'))
    return render_template('profil.html')

@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Login.profil'))
    form = LoginForm()
    if form.validate_on_submit():
        user = select_Patient(form.id.data, conn)
        if user is not None and user.password == form.password.data:
            login_user(user)
            flash('Login successful.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Login.profil'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@Login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Login.login'))