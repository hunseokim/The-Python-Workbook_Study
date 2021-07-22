#Ex 37
sides = int(input("enter the number of sides: "))
shapes = {3:'삼',4:'사',5:'오',6:'육',7:'칠',8:'팔',9:'구',10:'십'}
if sides >3 and sides<10:
    print(shapes[sides]+'각형')
else:
    print("error")