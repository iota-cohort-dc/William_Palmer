from flask import Flask, render_template, request, redirect
app = Flask(__name__)



# @app.route('/users/<username>')
# def show_user_profile(username):
#     return render_template("user.html", username=username)

# @app.route('/route/with/<vararg>')
# def handler_function(vararg):
#
#     print vararg

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/tmnt')
def tmnt():
    allNinjas = True

    return render_template('theNinjas.html', allNinjas=allNinjas)

@app.route('/tmnt/<color>')
def getColor(color):
    allNinjas = False

    return render_template('theNinjas.html', allNinjas=allNinjas, color=color)



app.run(debug=True)
