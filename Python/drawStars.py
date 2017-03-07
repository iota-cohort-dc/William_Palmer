'''print stars for the number value of each item in a list
[1,2,3,4,2,1] would return
*
**
***
****
**
*'''

from types import *

def drawStars(arr):
#x=[2,4,6,1,69]
    for item in arr:
        if type(item) is IntType:
            print item * "*"
        else:
            type(item) is StringType
            print item[0].lower() * len(item)




drawStars([1,3,"Steve",7,2,"Henry",20,1,"Moma"])
