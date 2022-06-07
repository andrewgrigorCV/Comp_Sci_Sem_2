thislist = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
import random
x = (random.randrange(0,3))

if(x == 0):
    print(thislist[0])
    
elif(x == 1):
    print(thislist[1])

elif(x == 2):
    print(thislist[2])
    
else:
    print("done")
