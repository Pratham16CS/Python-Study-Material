p=float(input("Enter Principal amount: "))
r=float(input("Enter Rate of interest: "))
t=float(input("Enter Time (in years): "))
si=(p*r*t)/100
amt = p+si
print("Simple interest:",si)
print("Total amount:",amt)