from flask import render_template, flash, redirect, request, url_for
from app import app
from forms import LoginForm, UserAddForm
import  subprocess

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'MWS PO Member' }
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@app.route('/adduser')
def createUser():
    form = UserAddForm()
    return render_template('createUser.html', form=form)

@app.route('/perform', methods = ['GET', 'POST'])
def perform():
    if request.method == 'GET':
        return redirect('/')

    host = request.form['host']
    name = request.form['name']
    passwd = request.form['passwd']
    email = request.form['email']
    firstname = request.form['firstname']
    """
    middlename = request.form['middlename']
    lastname = request.form['lastname']
    nofity = request.form['nofity']
    port = request.form['port']
    roles = request.form['roles']
    orgroles = request.form['orgroles']
    siteroles = request.form['siteroles']
    orgs = request.form['orgs']
    locale = request.form['locale']
    """
    out = None
    if firstname != "":
        out = subprocess.Popen([firstname], stdout=subprocess.PIPE).communicate()[0]

    #list = subprocess.Popen(["netstat", "-pnlt"], stdout=subprocess.PIPE).communicate()[0]

    return render_template('done.html', host=host, name=name, passwd=passwd, email=email, out=out)
