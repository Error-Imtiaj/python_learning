######################## Bee crowd problem 1150 ########################

""" 

Write a program that reads two integers: X and Z (Z must be read as many times as necessary, until a number greater than X is read). 
Count how many integers must be summed in sequence (starting at and including X) so that the sum exceeds Z the minimum possible and writes this number.


The input may have, for example, the numbers ​​21 21 15 30. In this case, the number 21 is assumed for X, The numbers 21 and 15 must be ignored because they are smaller or equal to X. The number 30 is within the specification (greater than X) and is valid. So, the final result must be 2 for this test case, because the sum (21 + 22) is bigger than 30. 

"""

x = int(input(""))
z = 0
a = [0]
swap = 0

cnt =1
while(1):
    if(z <= x):
        z = int(input(""))
        a.append(z)
    else:
        break
    

sum = x
while(sum < a[-1]):
    
    swap = x+1
    sum = sum + swap
    x += 1
    cnt = cnt +1

print(cnt)

    
