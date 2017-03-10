from  flask import  Flask, render_template, request, redirect, flash, session

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "Hotshoe"
print "Step 1"
@app.route('/')
def index():
    print "Step 2"
    return render_template('index.html')

@app.route('/reg_user', methods=['POST'])
def register():
    print "Got Post info"
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("You entered an invlaid email")
        return redirect('/')

    if len(request.form['frstNm']) < 1:
        flash("First name cannot be blank.")
        return redirect('/')
    if len(request.form['lstNm']) < 1 :
        flash("Last name cannot be blank.")
        return redirect('/')

    if len(request.form['passW']) < 1 or len(request.form['passW']) < 9:
        flash("Password cannot be blank and must be atleast 8 characters.")
        return redirect('/')
    if len(request.form['passC']) < 1:
        flash("Password Confirmation cannot be blank")
        return redirect('/')
    if request.form['passW'] != request.form['passC']:
        flash("Password and Password Confirmation must match!")
        return redirect('/')
    else:
        flash("Thank you for your submission")
        return redirect('/')

app.run(debug=True)
