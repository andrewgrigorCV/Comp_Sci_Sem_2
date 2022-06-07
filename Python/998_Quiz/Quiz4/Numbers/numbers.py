numblist = [6,9,32,28,15,22,3,18]
x = (numblist[1] + numblist[2] + numblist[3] + numblist[4] + numblist[5] + numblist[6] + numblist[7])/8
x = str(x)
print("The average of the list is: " + x)
abc = 55
d = 0
for i in range(0,7):
    if abc > numblist[i]:
       abc = numblist[i]
abc = str(abc)
print("The minimum of the list is: " + abc)
for y in range(0,7):
    if d<numblist[y]:
        d = numblist[y]
d = str(d)
print("The maximum of the list is: " + d)
print("SUPER CASH MONEYYYYYYYYYYYYYYYYYYYYYY")