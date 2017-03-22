from flask import Flask, render_template, request, redirect, session, flash

from mysqlconnection import MySQLConnector
# from flask.ext.bcrypt import bcrypt
from flask_bcrypt import Bcrypt

import re

lettersOnly = re.compile(r'^[a-zA-Z]+$')
#this will check the username and make sure that it is all letters.
emailCheck = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# checks the email address to make sure it looks like an email
app = Flask(__name__)
app.secret_key = "nogo"
mysql = MySQLConnector(app, "the_wall")
bcrypt = Bcrypt(app)



@app.route('/')
def landing_page():
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def registration():
    flag = False
    #below creates variables for the input from the register forms. The variables are the used in the series of if statements to test for length, valid format and matching before they are written into the database.
    data = {
        'fname': request.form['first_name'],
        'lname': request.form['last_name'],
        'email': request.form['email'],
        'pass': request.form['password'],
        'cpass': request.form['cpassword'],
    }
    # print("where we at??????????")

# first name validation for just letters and length is more than 2 characters
    if not lettersOnly.match(data['fname']):
        flag = True
        flash("You can only have letters in you first name")
        return redirect('/')

    if len(data['fname']) < 2:
        flag = True
        flash("Your first name must be at least 2 characters.")
        return redirect('/')

    if not data['fname']:
        flag = True
        flash("You must submit a first name.")
        return redirect('/')

# last name validation for just letters and length is more than 2 characters
    if not lettersOnly.match(data['lname']):
        flag = True
        flash("You can only have letters in you last name")
        return redirect('/')

    if len(data['lname']) < 2:
        flag = True
        flash("Your last name must be at least 2 characters.")
        return redirect('/')

    if not data['lname']:
        flag = True
        flash("You must submit a last name.")
        return redirect('/')

    #because of the flag = False above, if the match is true, then it returns a not false to allow us to continue to the next part

# email vlaidation for email format, not empty and submitted.
    if not emailCheck.match(data['email']):
        flag = True
        flash("You must enter a valid email.")
        return redirect('/')

    if not data['email']:
        flag = True
        flash("You must enter an email")
        return redirect('/')

# password check for not blank and length at least 8 characters.
    if len(data['pass']) < 8:
        flag = True
        flash("Your password must be at least 8 characters long.")
        return redirect('/')

    if not data['pass']:
        flag = True
        flash("You must enter a password")
        return redirect('/')

# confirm password check for not blank matches password.
    if data['pass'] != data['cpass']:
        flag = True
        flash("Your passwords don't match")
        return redirect('/')

    if flag:#this means that the flag is true and a check failed because the state ofthe flag was changed from False to True.
        return redirect ('/')
    else:
        # send information to the database
        pw_hash = bcrypt.generate_password_hash(data['pass'])

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:fname, :lname, :email, :pass, NOW(), NOW())"

        query_data = {
            "fname": data['fname'],
            "lname": data['lname'],
            "email": data['email'],
            "pass": pw_hash

        }
        user_id = mysql.query_db(query, query_data)
        session['user_id']= user_id
        return redirect("/the_wall")








@app.route("/login", methods=['POST'])
def login():
    query = "SELECT * FROM users WHERE email = :email"
    data = {
        "email":request.form['email']
    }
    userInQuestion = mysql.query_db(query, data)

    if not userInQuestion:
        flash("Invalid Email.")
        return redirect("/")
    else:
        if bcrypt.check_password_hash(userInQuestion[0]['password'], request.form['password']):
            session['user_id']=userInQuestion[0]['id']
            return redirect("/the_wall")
        else:
            flash("This password is invlaid")
            return redirect("/")

@app.route("/the_wall")
def the_wall():
    if "user_id" not in session:
        return redirect('/')


    query = "SELECT * FROM users WHERE id = :id"
    data = {
        "id":session['user_id']
    }
    logged_user = mysql.query_db(query, data)
    # print('logged_user')
    q_messages = "SELECT users.first_name, users.last_name, messages.id AS message_id, messages.message FROM messages LEFT JOIN users ON messages.user_id = users.id"

    messages = mysql.query_db(q_messages)

    c_messages = "SELECT users.first_name, users.last_name, comments.id AS comment_id, comments.comment, comments.message_id FROM comments LEFT JOIN users ON comments.user_id = users.id"
    comments = mysql.query_db(c_messages)

    return render_template("the_wall.html", user = logged_user[0], wall_messages = messages, wall_comments=comments)


@app.route("/addMessage", methods=['POST'])
def addMessage():
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"
    data = {
        "message":request.form['message'],
        "user_id":session['user_id']
    }
    mysql.query_db(query, data)
    return redirect("/the_wall")


@app.route("/addComment", methods=['POST'])
def addComment():
    # print("adding commentXXXXXXXXXXXXXXXXXXXXXXX")
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
    data = {
        "message_id":request.form['message_id'],
        "user_id":session['user_id'],
        "comment": request.form['comment']
    }
    print("THIS IS STILL WORKING!!!!!!!")
    mysql.query_db(query,data)
    return redirect("/the_wall")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")




app.run(debug=True)
