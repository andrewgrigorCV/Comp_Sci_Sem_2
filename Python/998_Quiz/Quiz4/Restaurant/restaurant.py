restaurants =("MacDonalds M8" , "Child Fil A" , "Pizza Gut")
MCD = ("fries: $3.99" , "burger: $9.99" , "drink: $6.99")
CFA = ("chiccen sand: $6.99" , "fries: $3.99" , "drink: $5.99")
PG = ("PepPizza: $10.99" , "Cheese Pizza: $9.99" , "Drink: $5.99")
best = input("Choose a restaurant: m for mcdonalds, c for chic fil a, and p for pizza hut: ")
if best == "m":
    print("Mcdonalds Menu here: " + MCD)
elif best == "c":
    print("CHic fil a menu here: " + CFA)
elif best == "p":
    print("Pizza Hut menu here:" + PG)