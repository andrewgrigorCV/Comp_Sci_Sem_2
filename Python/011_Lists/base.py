thislist = ["Why did the chicken cross the road?    He needed money for his dogs." , "What is the name of the tree that took out my wife?    A cheating tree" , "What is a tree called?    A house"]
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
