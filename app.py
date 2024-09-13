import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.peep_formatter import PeepFormatter
from lib.user_repository import UserRepository
from lib.sign_in_authenticator import SignInAuthenticator
from lib.peep_repository import PeepRepository
from datetime import datetime
from lib.peep import Peep
from lib.user import User
from lib.credentials_validator import CredentialsValidator
# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'im_not_sure_what_im_doing'
# == Your Routes Here ==
@app.route('/', methods = ["GET"])
def index():
    connection = get_flask_database_connection(app)
    peeps = PeepRepository(connection).all_decending(with_tags=True)
    formatted_peeps = [PeepFormatter(peep) for peep in peeps]
    if "handle" not in session:
        current_user = 'You are signed out, please sign in.'
        signed_in = False
    else:
        current_user = f"Hello {session['handle']}"
        signed_in = True
    return render_template('chitter/index.html', formatted_peeps=formatted_peeps, current_user=current_user, signed_in=signed_in)

@app.route('/sign-in', methods = ["GET"])
def go_to_sign_in():
    return render_template("chitter/sign_in.html")

@app.route('/sign-in', methods = ['POST'])
def sign_in():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    if SignInAuthenticator(repo).check_sign_in(email, password):
        user = repo.find_by_email(email)
        session["handle"] = user.handle
        session["name"] = user.name
        return redirect("/")
    else:
        return render_template("chitter/sign_in.html")
    
@app.route('/sign-out', methods = ["GET"])
def sign_out():
    del session["handle"]
    return redirect("/")

@app.route('/add-peep', methods = ['GET'])
def go_to_add_peep():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    handles = [user.handle for user in repo.all() if user.handle != session["handle"]]
    return render_template("chitter/add_peep.html", handles=handles)

@app.route('/add-peep', methods=["POST"])
def add_peep():
    connection = get_flask_database_connection(app)
    repo = PeepRepository(connection)
    content = request.form["content"]
    name = session["name"]
    handle = session["handle"]
    tags = request.form.getlist("tags")
    time = datetime.now()
    peep = Peep(None, content, name, handle, time, tags)
    repo.create(peep)
    return redirect("/")

@app.route('/create-account', methods = ["GET"])
def go_to_create_account():
    return render_template('chitter/create_account.html')

@app.route('/create-account', methods = ["POST"])
def create_account():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    email = request.form["email"]
    password = request.form["password"]
    if not CredentialsValidator().check_password(password):
        passwordmessage = "Invalid Password"
        return render_template('chitter/create_account.html', passwordmessage=passwordmessage)
    name = request.form["name"]
    handle = request.form["handle"]
    user = User(None, email, password, name, handle)
    session["handle"] = user.handle
    session["name"] = user.name
    repo.create(user)
    return redirect('/')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(
        debug=True, 
        port=int(os.environ.get('PORT', 5001)),
        host="0.0.0.0"
        )
