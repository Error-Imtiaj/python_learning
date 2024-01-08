## a = int(input()) ! please uncomment this to work all for loop


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

""" for i in range(0, a):
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
"""
##!  print string with loop action 


""" import math
import time

b = input("")
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,./;'\][-!@#$%^&*()+={\|'\"}]?"
v= " "
k =""
for i in b:
    for j in a:
        
        if(i == v):
            print(k+v)
            k = k + v
            break
        elif(i != j):
            print(k+j)
            
        elif(i == j):
            print(k+i)
            k = k + i
            break
        time.sleep(0.02)
    
   """ 
