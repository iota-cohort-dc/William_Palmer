from flask import Flask render_template, session, redirect, request, flash
app = Flask(__name__)
app.secret_key = "secretValidation"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['Post'])
def process():
    #the len() function will take the length of an import form, in the below case it is the "name" input field in the index.html
    #<form action='/process' method='POST'>
        #Name:<input type="text" name="name">
        #<input type="submit" value="Submit">
    #</form>
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")#passes a string to the flash message
        #error message
    else:
        flash("Success! Your name is {}".format(request.form['name']))
        #pass a string to the flash message.
        #success message



    return redirect('/')

app.run(debug=True)
