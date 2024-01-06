a = int(input())


##TODO Piramid ##


""" for i  in range(0, a):
    for j in range(0 , a-i):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()

"""

# Todo star printing

""" 
for i  in range(0, a):
    for j in range(0, i+1):
        print("*", end=" ") #! end="" use to make space
    print()


"""
## TODO PIRAMID UPSIDE DOWN

""" for i in range(0, a):
    for j in range(0, i):
        print(end=" ")
    for j in range(0, a - i):
        print("*", end=" ")
    print()
 
"""
# TODO STAR PRINTING UPSIDE DOWN

""" for i in range(0, a):
    for j in range(0, (a) -i ):
        print("*", end=" ")
    print() 
"""

## ! box diamond startv printing

for i in range(0, a):
    for j in range(0, a -i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()
for i in range(0 , a):
    for j in range(0, i):
        print(end=" ")
    for j in range(0, a - i):
        print("*", end=" ")
    print()