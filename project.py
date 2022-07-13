from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re 




 
app = Flask(__name__)
  
  
app.secret_key = '123456'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'project'
  
mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        username = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE EMAIL = % s AND PASS = % s', (EMAIL, PASS, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id'] // problem ,
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('Teams.html', msg = msg)
        else:
            msg = 'Incorrect email / password !'
    return render_template('signin.html', msg = msg)






@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST'  and 'password' in request.form and 'email' in request.form :
        
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE EMAIL= % s', (EMAIL, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        
        elif not  not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO Users VALUES ( % s, % s)', (EMAIL, PASS,  ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('signup.html', msg = msg)
    
    
    
    

