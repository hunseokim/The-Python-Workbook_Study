#Ex 37
month = input("enter the month: ")
if month == '1월' or month == '3월' or month == '5월' or month == '7월' or month == '8월' or month == '10월' or month == '12월':
    print("31 days")
elif month =='2월':
    print("28 or 29 days")
elif month =='4월' or month =='6월' or month =='9월' or month =='11월':
    print("30 days")
else:
    print("error!")