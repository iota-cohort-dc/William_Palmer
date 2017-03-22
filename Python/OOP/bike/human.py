class Human(object):
    def __init__(self, health, name, occupation, age):
        self.health = health
        self.name=name
        self.occupation=occupation
        self.age=age

    def eat(self):
        self.health += 10

    def sleep(self):
        self.health += 40
        self.age += 1

    def bathroom(self):
        self.health += 10
        self.age += 1

    def uppercut(self, HumanObj):
        print "fuck Off!!!"
        HumanObj.health -= 5
        return "Battle complete!"

print dir(Human)

Jimmy = Human(100, "Jimmy", "student", "35")
Danny = Human(100, "Danny", "student", "29")


print Jimmy.uppercut(Danny)
print Danny.health
