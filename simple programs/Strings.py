# Program to show use of Escape sequence character 
str1 = "This is a string.\nWe are doing timepass." #next line
str2 = "A for apple\tB for Ball" #tab space
print("Output for nextline:")
print(str1)
print("\n")
print("Output for Tab space:")
print(str2)

# Program to print length of string
print(len(str1))

# Program for slicing of a string
name = "Pratham_Salgaonkar"
print(name[1:8])
print(name[8:18])
print(name[:7]) #same as name[0:7]
print(name[4:]) #same as name[4:len(name)]

# Program for slicing of string using negative indexing
new = "Abhimanyu"
print(new[-4:-1])
print(new[-9:])
print(new[:-2])
print(new[-8:-4])

# Program using endswith() method
print(new.endswith("u"))
print(name.endswith("Pratham"))

# Program using capitalize() method
name1 = "pratham"
print(name1.capitalize())
print("goa".capitalize())

# Program using replace() method
print("Prathamesh".replace("mesh","m"))
print(name1.replace(name1,name))
print(name1)

# Program using find() method 
print(name.find("_")) # returns index value
print(name.find("Sa"))
print(new.find("man"))

# Program using count() method
str3 = name + name1
print(name.count("a"))
print(str1.count("r"))
print(str2.count("for"))
print(str2.count("e"))
print(str3.count("am"))