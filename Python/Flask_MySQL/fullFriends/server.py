from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key='shhhhh'
mysql = MySQLConnector(app,'friendsdb')


@app.route('/')
def index():
    query = "SELECT * FROM friends" # defines the query
    friends = mysql.query_db(query) # runs query in the db
    return render_template('index.html', all_friends=friends) #passes datat o template
    # return render_template('index.html')


@app.route ('/friends',methods=['POST'])
def create():
    query = 'INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())'
    data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email']
            }
    mysql.query_db(query,data)

    #
    # emails=mysql.query_db('SELECT * FROM email')
    #
    # flash('The email that you entered ' + emailData + ' is a valid email. Thanks.')

    return redirect('/')

@app.route ('/friend/<id>/edit')
def edit(id):
    # query = 'SELECT (first_name, last_name, email) FROM friends WHERE id=:id';
    query = "SELECT * FROM friends WHERE id =:id"
    # print id
    data = {
            "id":id,
            }
    single_friend = mysql.query_db(query,data)
    print single_friend[0]
    return render_template('edit.html', friend=single_friend[0])
    # friends = mysql.query_db(query, data)

    # mysql.query_db(query,data)


    return render_template('edit.html')

@app.route ('/friend/<id>', methods=['POST'])
def update(id):
    query = 'UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:id';
    data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'id':id
            }
    mysql.query_db(query,data)
    return redirect('/')

@app.route ('/friend/<id>/delete', methods=['POST'])
def destroy(id):
    query = 'DELETE FROM friends WHERE id=:id';
    data = {
        "id": id
        }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
