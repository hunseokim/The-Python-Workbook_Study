#Ex 64
total=0
switch=True
while switch:
    inp=input("Enter the price: ")
    if inp=='':
        switch=False
    else:
        total += float(inp)
print("Total Cost: ",total)
pen=total % 0.05
if pen==0:
    cost= total
elif pen<0.025:
    cost = total - pen
elif pen>0.025:
    cost = total + (0.05-pen)
print("You have to pay %.2f" %cost)