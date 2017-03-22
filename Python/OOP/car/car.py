class Car(object):
    def __init__(self,price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage


        if self.price > 100000:
            tax = ".15"
        else:
            tax = ".12"

        self.tax=tax

        self.display_all()

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "tax: " + str(self.tax)
        print "\n"

car1 = Car(35000, 100, 'empty',10000)
car2 = Car(15000, 130, "hlaf full", 534)
car3 = Car(150000, 180, 'full',19000)
car4 = Car(220000, 225, 'quarter empty',3500)
car5 = Car(22000, 120, 'empty',100000)
car6 = Car(40000, 155, 'full',85945)
