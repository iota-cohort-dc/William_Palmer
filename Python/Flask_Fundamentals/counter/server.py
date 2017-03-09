from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'tomfoolery'

@app.route('/')
def index():
    return render_template('index.html')
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 0
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count():
    session["counter"] += 1
    return redirect('/')

# the below route is being added for the Sessions lesson in the Flask Platform
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)#run the server
