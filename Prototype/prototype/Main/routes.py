from flask import render_template, url_for, flash, redirect, request, Blueprint
from prototype import conn
from prototype.Main.forms import LoginForm
from flask_login import login_user, current_user, logout_user
from prototype.models import select_Patient, get_History, get_Diagnoses, get_Active_Prescriptions, insert_New_Renewed_Prescription

Main = Blueprint('Main', __name__)

@Main.route("/receptfornyelse")
def receptfornyelse():
    p = get_Active_Prescriptions(current_user.get_id(), conn)
    return render_template('receptfornyelse.html', percs=p)

@Main.route('/renew/<med_name>/<med_conc>')
def renew(med_name, med_conc):
    insert_New_Renewed_Prescription(current_user.get_id(), med_name, med_conc, conn)
    p = get_Active_Prescriptions(current_user.get_id(), conn)
    flash('Receptfornyelse godkendt.', 'success')
    return redirect(url_for('.receptfornyelse', percs=p))

@Main.route("/meddelser")
def meddelelser():
    return render_template('meddelelser.html')

@Main.route("/aftaler")
def aftaler():
    return render_template('aftaler.html')

@Main.route("/historik")
def historik():
    h = get_History(current_user.get_id(), conn)
    return render_template('historik.html', history=h)

@Main.route("/sundhedsdata")
def sundhedsdata():
    d = get_Diagnoses(current_user.get_id(), conn)
    return render_template('sundhedsdata.html', diagnoses=d)

@Main.route("/fahjaelp")
def fahjaelp():
    return render_template('fahjaelp.html')

@Main.route("/")
@Main.route("/profil")
def profil():
    if not current_user.is_authenticated:
        return redirect(url_for('Main.login'))
    return render_template('profil.html')

@Main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Main.profil'))
    form = LoginForm()
    if form.validate_on_submit():
        user = select_Patient(form.id.data, conn)
        if user is not None and user.password == form.password.data:
            login_user(user)
            flash('Login successful.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Main.profil'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@Main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Main.login'))