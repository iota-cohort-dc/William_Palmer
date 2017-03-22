from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "secretkey"
mysql = MySQLConnector(app,'emaildb')


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def vaildate():
    if not EMAIL_REGEX.match(request.form['email']):
        # print "hello"
        flash('INVALID EMAIL ADDRESS')
        return redirect('/')
    else:
        session['email'] = request.form['email']
        emailData = str(session['email'])
        # session['sentence'].append(emailData)
        print("happy test")
        query = 'INSERT INTO email (email,created_at,updated_at) VALUES (:email, NOW(), NOW())'
        data = {
                'email':request.form['email'],
                }
        mysql.query_db(query,data)

        emails=mysql.query_db('SELECT * FROM email')

        flash('The email that you entered ' + emailData + ' is a valid email. Thanks.')

        return render_template('valid.html', all_emails=emails) #passes datat to template



app.run(debug=True)
