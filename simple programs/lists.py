# Program for declaring & knowing more about list
marks = [84,45,65,47,45,65]
print(marks)
print(type(marks))
print(marks[0])
print(marks[5])
print(len(marks)) # List length
print()

# Program for slicing of a list
geo = [40,20,"North","South",25.5,41.12]
print(type(geo))
print(type(geo[2]))
print(type(geo[5]))
print(geo[2:5])
print(geo[:3]) # same as geo[0:3]
print(geo[2:]) # same as geo[2:len(geo)]

#Slicing using negative indexing
print(geo[-5:-1])
print(geo[-5:]) 
print(geo[:-1])

# Program using append() method 
films =["Bahubali","RRR","3 Idiots","Sholay"]
print(films)
films.append("Golmaal")
print(films)
films.append("Abhimanyu") # upcoming remember the name
print(films)

# Program using sort() sort(reverse) method
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

# Program using insert() method
films.insert(0,"Hera Pheri")
print(films)
films.insert(4,"Kalki 2898 AD")
print(films)

#Program using remove() method
marks.remove(47)
print(marks)
marks.remove(45)
print(marks)

# Program using pop() method
marks.pop(2)
print(marks)