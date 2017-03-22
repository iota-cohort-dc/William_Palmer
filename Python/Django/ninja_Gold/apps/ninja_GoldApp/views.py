from django.shortcuts import render, redirect
import random
import datetime




def index(request):
    # session.clear()
    print"Looking fer gold!"

    if "gold" in request.session:
        pass
    else:
        request.session['gold'] = 0

    if "turn" in request.session:
        pass
    else:
        request.session['turn'] = []

    return render(request, "index.html")

def gettingGold(request):

    if request.method == "POST":


        if request.POST['fromPlace'] == "farmGold":

            request.session['random_num'] = random.randrange(10, 20)
            #in the range, the first and last numbers are inclusive.
            farmString = "You earned " + str(request.session['random_num']) + " gold coins from the farm." + " " + str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
            request.session['turn'].append(farmString)
            # adds to total gold
            request.session['gold'] += request.session['random_num']
            #can also use "session['gold']"+= randint(10,20). you don't need to set session['random_num'] first and then add it with the gold later.

        elif request.POST['fromPlace'] == "caveGold":
            request.session['random_num'] = random.randrange(5, 10)
            caveString = "You earned " + str(request.session['random_num']) + " gold coins from the cave." + " " + str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
            request.session['turn'].append(caveString)
            request.session['gold'] += request.session['random_num']

        elif request.POST['fromPlace'] == "houseGold":
            request.session['random_num'] = random.randrange(2, 5)
            houseString = "You earned " + str(request.session['random_num']) + " gold coins from the house." + " " + str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
            request.session['turn'].append(houseString)
            request.session['gold'] += request.session['random_num']

        elif request.POST['fromPlace'] == "casinoGold":
            randomNumber = random.randrange(0, 2)
            if randomNumber == 1:
                request.session['random_num'] = random.randrange(1,51)
                casinoString = "You entered a casino and won " + str(request.session['random_num']) + " gold coins at the casino." + " " + str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
                request.session['turn'].append(casinoString)
                request.session['gold'] += request.session['random_num']
            elif randomNumber == 0:
                request.session['random_num'] = random.randrange(1,51)
                casinoString = "You entered a casino and lost " + str(request.session['random_num']) + " gold coins at the casino." + " " + str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
                request.session['turn'].append(casinoString)
                request.session['gold'] -= request.session['random_num']

        return redirect ('/')

    else:
        return redirect('/')
