# WAP to check if a list contains a palindrome of elements in a list
num = [12,41,48,41,12]
new = num.copy()
num.reverse()
if(new == num):
    print("Palindrome")
else:
    print("Not Palindrome")