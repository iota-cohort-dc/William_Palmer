# Print all odd numbers from 1 to 1000
for count in range(0,1000):
    if count % 2 != 0:
        print count

# Print all multiples of 5 from 5 to 1000000
for count in range(5, 1000001, 5):
    print count

# Print the sum of all values in a list
a = [1,2,5,10,255,3]
i=0
sum=0
while i < len(a):
    sum =sum+a[i]
    i+=1
print sum

# Print the average of all the values in a list
a = [1,2,5,10,255,3]
i=0
sum=0
while i < len(a):
    sum =sum+a[i]
    i+=1
print sum/len(a)
