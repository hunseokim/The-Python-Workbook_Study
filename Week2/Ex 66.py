#Ex 66
def grade_point(grade):
    if grade=='A+':
        return 4.0
    elif grade=='A':
        return 4.0
    elif grade=='A-':
        return 3.7
    elif grade=='B+':
        return 3.3
    elif grade=='B':
        return 3.0
    elif grade=='B-':
        return 2.7
    elif grade=='C+':
        return 2.3
    elif grade=='C':
        return 2.0
    elif grade=='C-':
        return 1.7
    elif grade=='D+':
        return 1.3
    elif grade=='D':
        return 1.0
    elif grade=='F':
        return 0
point=0
count=0
while True:
    grade=input("Enter your grade: ")
    if grade!='':
        point += int(grade_point(grade))
        count+=1
    else: break
score=point/count
print("Your everage score is %.1f" %score)
