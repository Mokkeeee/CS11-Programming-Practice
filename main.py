print("Problem 1 below")

radius = input("What is the raidus of the circle? ")
radius = int(radius)
type_of_radius = type(radius)
print(type_of_radius)
area = 3.14*(radius*radius)
print("This is the area of your circle: "+ str(area))

print("***********************************")


print("Problem 2 Below")

a = int(input("What is the value for a? "))
b = int(input("What is the value for b? "))

print("Thanks! Let's solve for (a-b)+(a*b):")
answer = (a-b)+(a*b)
print("Here is the answer: " + str(answer))

print("***********************************")


print("problem 3 below")

print("ASCII art display here!")
which_art = input("Do you want to see art 1 or art 2?: ")

if which_art == "1":
    print('''hi
    this is a string
    ''')
else:
    print('''this is the else''')