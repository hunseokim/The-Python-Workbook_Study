#Ex 40
side1=int(input("Enter the first side of triangle: "))
side2=int(input("Enter the second side of triangle: "))
side3=int(input("Enter the third side of triangle: "))

if side1==side2 and side2==side3:
    print("Equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("Isosceles triangle")
else:
    print("Scalene triangle")