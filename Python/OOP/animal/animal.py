class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def walk(self):
        self.health -= 1;
        return self

    def run(self):
        self.health -=5
        return self

    def display_health(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Animal, self).__init__()
        self.health = 150

    def pet(self):
        self.health += 5
        return self

Dog1=Dog("Wade")
Dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Animal, self).__init__()
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "This is a dragon",self.health
        return self



Dragon1=Dragon("smoke")
Dragon1.walk().walk().walk().run().run().fly().fly().display_health()

animal1=Animal('ani', 100)
animal1.pet().run().fly()
