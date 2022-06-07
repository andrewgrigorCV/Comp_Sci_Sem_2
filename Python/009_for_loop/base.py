x = int(input("Give me a length: "))
y = (input("Want vertical (V) or horizontal (H) line??????"))

if(y == "H"):
    for i in range(0,x):
        print(i, end =", " )

elif(y == "V"):
    for i in range(0,x):
        print(i)
