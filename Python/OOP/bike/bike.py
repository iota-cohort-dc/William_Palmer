class Bike(object):
    def __init__(self):
        print "New Bike"
        self.price = 300
        self.max_speed = 24
        self.miles = 0

    def displayInfo(self):

        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self




# print dir(Bike)

bike1 = Bike()
bike2 = Bike()
bike3 = Bike()

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
