#Ex 48
year = int(input("Enter year: "))

if year%12 == 1:
    print("Rooster's Year")
elif year%12 == 2:
    print("Dog's Year")
elif year%12 == 3:
    print("Pig's Year")
elif year%12 == 4:
    print("Rat's Year")
elif year%12 == 5:
    print("Ox's Year")
elif year%12 == 6:
    print("Tiger's Year")
elif year%12 == 7:
    print("Hare's Year")
elif year%12 == 8 :
    print("Dragon's Year")
elif year%12 == 9 :
    print("Snake's Year")
elif year%12 == 10 :
    print("Horse's Year")
elif year%12 == 11 :
    print("Sheep's Year")
elif year%12 == 0 :
    if year == 0 :
        print("Error")
    else :
        print("Monkey's Year")