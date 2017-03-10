from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'goldDigger'
from random import randint
# can use just "import random" here but you will have to reference the method in code below with random.randint()
#if you use "from random import randint", you can just use randint() in the code.

@app.route('/')
def index():
    # session.clear()
    if "gold" in session:
        pass
    else:
        session['gold'] = 0

    if "turn" in session:
        pass
    else:
        session['turn'] = []

    return render_template("index.html")

@app.route("/gettingGold", methods=['POST'])
def gettingGold():

    if request.form['fromPlace'] == "farmGold":
        print "from________________________farm."
        session['random_num'] = randint(10, 20)
        #in the range, the first and last numbers are inclusive.
        farmString = "You earned" + str(session['random_num']) + " gold coins from the farm."
        print farmString
        session['turn'].append(farmString)
        print session['turn']
        # adds to total gold
        session['gold'] += session['random_num']
        #can also use "session['gold']"+= randint(10,20). you don't need to set session['random_num'] first and then add it with the gold later.
        print session['gold']

    elif request.form['fromPlace'] == "caveGold":
        print "from________________________cave."
        session['random_num'] = randint(5, 10)
        caveString = "You earned" + str(session['random_num']) + " gold coins from the cave."
        print caveString
        session['turn'].append(caveString)
        print session['turn']

        session['gold'] += session['random_num']
        print session['gold']
    elif request.form['fromPlace'] == "houseGold":
        print "from________________________hosue."
        session['random_num'] = randint(2, 5)
        houseString = "You earned" + str(session['random_num']) + " gold coins from the house."
        print houseString
        session['turn'].append(houseString)
        print session['turn']

        session['gold'] += session['random_num']
        print session['gold']
    else:
        request.form['fromPlace'] == "casinoGold"
        print "from________________________casino."
        winlose = randint(0,1)
        if winlose > 0:
            session['random_num'] = randint(0, 50)
            casinoString = "You won " + str(session['random_num']) + " gold coins at the casino."
            print casinoString
            session['turn'].append(casinoString)
            print session['turn']

            # adds to total gold
            session['gold'] += session['random_num']
            print session['gold']
        else:
            session['random_num'] = randint(0, 50)
            casinoString = "You lost " + str(session['random_num']) + " gold coins at the casino."
            print casinoString
            session['turn'].append(casinoString)
            print session['turn']

            # adds to total gold
            session['gold'] -= session['random_num']
            print session['gold']

    return redirect ('/')



app.run(debug=True)
