my_string ="If monkeys like bananas, then I must be a monkey"
print my_string.find("monkey")
my_secondString = my_string.replace("monkey", "alligator",2)
print my_secondString

my_list =[2,54,-2,7,12,98]
print max(my_list)
print min(my_list)

first_and_last = ["hello", 2,54,-2,7,12,98,"world"]
print first_and_last [0]
print first_and_last[(len(first_and_last)-1)]
x=[19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
firstHalf = x[0:(len(x)/2)]
secondHalf = x[(len(x)/2):len(x)]
secondHalf.insert(0, firstHalf)
print secondHalf
