# count the even and odd numbers from 1 to 2000 while labeling each one even or odd
def odd_even():
    count=0
    while count < 2000:
        count += 1
        if count % 2 != 0:
            print 'Number is', count, '. This is an odd number.'
        else:
            print 'Number is', count, '. This is an even number.'

odd_even()


# Iterate through a list and returns a list with each value multiplied my 5
def multiply(a,x):
    i=0
    while i < len(a):
        a[i] = a[i]*x
        i += 1
    print a

multiply([2,60,10],5)
