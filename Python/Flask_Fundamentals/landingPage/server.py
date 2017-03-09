from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def dojo_new():
    return render_template('dojos.html')

app.run(debug=True)

# you can have more than one @app.route per .py server page. the ('/') basically tells the server which page to serve up. The ('/dojo/new') does not reflect a folder path in your folder structure. Although it reads as a folder path, there is only one dojo.html page and not a dojo.html file inside of a folder.

# the name in the @app.route is to reference individual pages. there can be one @app.route or there can be thousands of them.
