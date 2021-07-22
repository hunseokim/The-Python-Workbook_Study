#Ex 49
sc=float(input("Enter the magnitude: "))

if sc<2.0:
    print("Micro earthquake")
elif sc>=2.0 and sc<3.0:
    print("Very minor earthquake")
elif sc>=3.0 and sc<4.0:
    print("Minor earthquake")
elif sc>=4.0 and sc<5.0:
    print("Light earthquake")
elif sc>=5.0 and sc<6.0:
    print("Moderate earthquake")
elif sc>=6.0 and sc<7.0:
    print("Strong earthquake")
elif sc>=7.0 and sc<8.0:
    print("Major earthquake")
elif sc>=8.0 and sc<10.0:
    print("Great earthquake")
elif sc>=10.0:
    print("Meteoric earthquake")