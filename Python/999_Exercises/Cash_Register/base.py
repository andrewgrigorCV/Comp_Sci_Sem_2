x = int(input("How many items do you wanna buy dude or dudette?: "))
total = 0
for i in range(0, x):
        xName = input("What is the item?")
        price = float(input("How much is it?"))
        print("Thanks for purchasing " + xName)
        total = total + price
print("Your total is: " + str(total))

