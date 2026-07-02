#if-else ladder
light = input("Enter colour of signal: ")
if(light=="red"or light=="Red"or light=="RED"):
    print("Stop")
elif(light=="yellow"or light=="Yellow"or light=="YELLOW"):
    print("Look")
elif(light=="green"or light=="Green"or light=="GREEN"):
    print("Safe to drive")
else:
    print("Signal is broken")

#ternary operator- Single line if
food=input("food: ")
eat="Yes"if food =="cake" else "No"
print(eat)
juice=input("Juice: ")
print("Yes") if juice=="lemon" or juice=="mango" else print("No")

#ternary operator- clever if
age = int(input("Enter age: "))
vote = ("Yes","No")[age<18]
print(vote)