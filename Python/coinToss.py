import random


heads=0
tails=0
face=""
headCount=0
tailCount=0
print "Starting the program"
for count in range (0,5000):
    x = random.random()
    x_rounded = round(x)
    if x_rounded == 1.0:
        face = 'Heads'
        count += 1
        headCount += 1
    else:
        face = 'Tails'
        count += 1
        tailCount += 1
    print 'Attempt #',count,":  Tossing a coin.... It's",face,"!... Got ",headCount, " Heads and ",tailCount, "Tails so far."
print "Ending the program, thank you!"
