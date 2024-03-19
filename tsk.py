swimtime=int(input("What was your swimming time in minutes?"))
cycletime=int(input("What was your cycling time in minutes?"))
runtime=int(input("What was your running time in minutes?"))
totaltime=swimtime+cycletime+runtime
if totaltime > 110:
    print(totaltime)
    print("No award given, better luck next time")
elif totaltime <= 110 and totaltime > 105:
    print(totaltime)
    print("You have received a Provincial Scroll.")
elif totaltime <= 105 and totaltime > 100:
    print(totaltime)
    print("You have recieved Provincial Half Colours.")
elif totaltime<=100:
    print(totaltime)
    print("You have recieved Provincial Colours.")
