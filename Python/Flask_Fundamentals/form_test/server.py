from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
# the app.secret_key needs to be set, with a value ("ThisIsSecret") in order for the session to run


# the index route will handle rendering the form
@app.route('/')
def index():
    return render_template('index.html')


# the below route will handle form submission
# this defines which HTTP method is allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
#
    session['name'] = request.form['name']
    session['email'] = request.form['email']
# session before the bracketed variable allows access to the name and email stored from one function in another
    # name = request.form['name']
    # email = request.form['email']

#  redirects back to the '/' route
    return redirect('/show')

# the below route is being added for the Sessions lesson in the Flask Platform
@app.route('/show')
def show_user():
    return render_template('user.html')


app.run(debug=True)#run the server
