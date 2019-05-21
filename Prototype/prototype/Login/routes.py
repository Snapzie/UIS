from flask import render_template, url_for, flash, redirect, request, Blueprint
from prototype import app, conn, bcrypt
from prototype.forms import RegistrationForm, CustomerLoginForm, EmployeeLoginForm
from flask_login import login_user, current_user, logout_user, login_required
from prototype.models import Patients, select_Patient

Login = Blueprint('Login', __name__)

@Login.route("/login", methods=['GET', 'POST'])
def login():
    is_employee = True if request.args.get('is_employee') == 'true' else False
    form = EmployeeLoginForm() if is_employee else CustomerLoginForm()
    return render_template('login.html', title='Login', is_employee=is_employee, form=form)

