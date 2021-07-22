#Ex 36
word = str(input("enter alphabet: "))
if word =='a' or word == 'e' or word=='i' or word=='o' or word=='u':
    print("entered letter is a vowel.")
elif word =='y':
    print("y is a vowel, and sometimes y is a consonant.")
else:
    print("entered letter is a consonant")