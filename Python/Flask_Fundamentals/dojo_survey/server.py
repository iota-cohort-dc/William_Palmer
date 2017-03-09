from  flask import  Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post info"
    name = request.form['name']
    location = request.form['location']
    language =request.form['language']
    comments = request.form['comments']
    print name
    print language
    print location
    print comments
    return render_template('/userInfo.html',name=name,location=location,language=language,comments=comments)

app.run(debug=True)
