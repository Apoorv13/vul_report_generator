from flask import Flask, render_template, url_for, request, session, redirect
from flask.ext.pymongo import PyMongo
import requests
import bcrypt
import json
from flask import Flask, render_template, request
from werkzeug import secure_filename
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = 'static/vul'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MONGO_DBNAME'] = 'report_helper'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/report_helper'


mongo = PyMongo(app)
number_of_vulns = 0

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('news'))

    return render_template('index.html')

@app.route('/upload_vulns', methods=['POST', 'GET'])
def upload_vulns():
    if 'username' in session:
            username = session['username']
            print number_of_vulns
            if request.method == 'POST':
                for i in range(number_of_vulns):
                    ph_index = "vul"+i
                    if ph_index not in request.files:
                       flash('No file part')
                       return redirect(request.url)
                    file = request.files[ph_index]
                        # if user does not select file, browser also
                        # submit a empty part without filename
                    if file.filename == '':
                        flash('No selected file')
                        return redirect(request.url)
                    if file:
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        print "Uploaded"
                        print filename
            return "Uploaded"
#render_template('upload.html')
    return "FAILED"
#render_template('index.html')
            
@app.route('/select_vulns', methods=['POST', 'GET'])
def select_vulns():
    if 'username' in session:
            username = session['username']
            if request.method == 'POST':
                number_of_vulns = request.form['number_vul']
                print number_of_vulns
            return render_template('upload_report.html', num = int(number_of_vulns), username = username)                
    return render_template('index.html')

@app.route('/news', methods=['POST', 'GET'])
def news():
    if 'username' in session:
        if request.method == 'POST':
                number_of_vulns = request.form['number_vul']
                print number_of_vulns
                return redirect(url_for('select_vulns'))
        return render_template('table.html')

    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)