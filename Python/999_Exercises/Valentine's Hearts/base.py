Peeps = ["He ", "Alex" , "Gabe" , "Your mother" , ]
Comlpiments = ["is hot" , "is cool" , "is tall"]

import random
num_peeps = random.randrange(0,len(Peeps)) 
num_comps = random.randrange(0,len(Compliments)) 

print(Peeps[num_peeps]) + " " + Compliments[num_comps]