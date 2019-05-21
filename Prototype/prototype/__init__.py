from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'
db = "dbname='prototype' user='Casper' host='localhost' password = ''"
conn = psycopg2.connect(db)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login.login'

from prototype.Login.routes import Login
app.register_blueprint(Login)

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('prototype.tests')
    unittest.TextTestRunner(verbosity=2).run(tests)