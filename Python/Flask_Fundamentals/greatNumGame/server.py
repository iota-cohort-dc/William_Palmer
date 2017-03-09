from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'tomfoolery'
import random

# magicNumber = random.range(0,101)
# session['secretNumber']= magicNumber
# session.pop('inputNum')
@app.route('/')

def random_Num():
    # session.clear()
    if "mysteryNum" in session:
        pass
    else:
        session['mysteryNum'] = random.randrange(0,100)

    print session['mysteryNum'],"lllllll______________lllllllll"
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def highOrLow():
    # print session['mysteryNum']
    guess = int(request.form['inputNum'])
    if guess < session['mysteryNum']:
        print guess
        session['highLow']="Too Low! Try again."
        print session['highLow']
        return render_template('index.html', highLow = "Too Low! Try again.")

    elif guess > session['mysteryNum']:
        print guess
        session['highLow']="Too High! Try again."
        print session['highLow']
        return render_template('index.html', highLow = "Too High! Try again.")

    elif guess == session['mysteryNum']:
        print "WINNER!!!!!!!!"
        return render_template('congrats.html')

# @app.route('/win', methods=["POST"])
# def gotNumber():
#     if guess == session['mysteryNum']:
#         print guess, "You got it"
#         return redirect('congrats.html',highLow = "Congrats!!!!")

@app.route('/reset', methods=['POST'])
def reset():
    # print session['mysteryNum']
    # guess = int(request.form['inputNum'])
    session.clear()
    return redirect('/')
    # if request.form['again'] == 'Play Again?':
    #     session.clear()
    #     # print guess
    #     # session['highLow']="Too Low! Try again."
    #     # print session['highLow']
    #     return redirect('/')



app.run(debug=True)#run the server
