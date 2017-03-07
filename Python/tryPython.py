name="camelCase"
name="Marlon Brando"
occupation="actor"
print 4+8
print name + occupation
print str(4) + "Marlon" #using str() will return the number inside the () but it is not acutally an integer
print name + "80" # this will also return 80 but it is not an integer. This and the str() convert the number to a string
integer = 80
print name + `integer`# the backticks will maintain the number as an integer.
print type(integer)
print type(name)
print type(name + str(4))
