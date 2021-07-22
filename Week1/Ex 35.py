#Ex 35
year = int(input("enter the year: "))

if year <=2 and year>=0:
    print(year*10.5,"dog year old")
elif year > 2:
    print((year-2)*4+21,"dog year old")
elif year<0:
    print("error")