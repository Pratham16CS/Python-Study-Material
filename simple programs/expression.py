# Expression execution
#1.String & Numeric values can operate together with '*'
A,B=2,3
txt="@"
print(A*txt*B)

#2.String & string can be operated with '+'
a,b="Pratham ",16
sign = '@'
print((sign+a)*b)

#3.NUmeric values can be operated with all arithmetic operators
num1=45
num2=15
num3=78
num4=2
num5=60
print(num1+num2/num3-num4*num5)

#4.Arithmetic expression with integer & float will result in float
A,B=10,5.0
print(A*B)

#5.Result of division operator with two integer will be float
A,B=1,2
print(A/B)
print(type(A/B))

#6.Integer division with float and integer will return integer displayed as float
A=7.2
B=3
C=A//B
print(C,A/B) 

#8.Remainder is negative if denominator is negative
a,b=5,-2
print(a%b,b%a)

#9.Power
m,n=3,2
print(m**n,n**m)