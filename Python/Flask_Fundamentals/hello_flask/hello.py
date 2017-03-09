from flask import Flask, render_template
app = Flask(__name__)
#print 'hello'
@app.route('/')
def hello_world():
    return render_template('index.html', name="Batman")
app.run(debug=True)
