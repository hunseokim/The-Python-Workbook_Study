#Ex 39
db = int(input("Enter the decibel level: "))
def noise_name(db, name):
    print(f"{db}dB is a Noise of {name}")
def noise_bet(db, name1, name2):
    print(f"{db}dB is a Noise between {name1} and {name2}")

if db>130:
    print(f"{db} has higher level of noise than Jackhammer")
elif db==130:
    noise_name(db, "Jackhammer")
elif db<130 and db>106:
    noise_bet(db, "Gas lawnmower","Jackhammer")
elif db==106:
    noise_name(db, "Gas lawnmower")
elif db>70 and db<106:
    noise_bet(db,"Alarm clock","Gas lawnmower")
elif db==70:
    noise_name(db,"Alarm clock")
elif db>40 and db<70:
    noise_bet(db, "Quiet room", "Alarm clock")
elif db==40:
    noise_name(db,"Quiet room")
elif db<40:
    print(f"{db} has lower level of noise than Quiet room")