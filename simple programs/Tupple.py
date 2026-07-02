# Program to know about tupple and its various methods
game = ("cricket","kabbaddi","kho-kho","football","Cycling")
print(type(game))
print(len(game)) # Print length of tupple
print()

# Program to write a tuple which contains only one element
num = (1)
print(type(num))
digit = (1,)
print(type(digit))
print()

# Program for slicing of a tuple
print(game)
print(game[1:4])
print(game[2:]) # same as game[2:len(game)]
print(game[:3]) # same as game[0:3]
print(game[:-2])
print(game[-4:])
print()

# Program using index() method
random = (4,5,6,7,8,9)
print(random.index(6))
print(game.index("cricket"))
print(game.index("kho-kho"))
print()

# Program using count() method
t = [40,24,42.0,48.4,42,45,87,87,65,45,55.8,42]
print(t.count(42))
print(t.count(65))
print(t.count(1.25))