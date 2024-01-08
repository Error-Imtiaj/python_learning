#################### CONDITIONS ##################

## equals a == b
## Not Equals a != b
## Less THAN A < B
## GREATER THN A > B
## LESS THAN OR EQUAL TO A <= B
## GREATER THAN OR EQUALS TO A >= B


########################### if else syntax ########################

# if condition : 
    # print ( "Result : anything ")
  #else:
    # print("anything")

############################### Bwsaic If Statement ######################

#   if 10 == 5:
    #   print("True")
#   else:
    #   print("False")

################################ END BASIC IF STATEMENT #################

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

if a == b:
    print("They are Equal")
elif a < b:
    print(" 1st number is less than 2nd number")
elif a > b:
    print("1st number is greater than 2nd number")


###############################################################################

#                       Student Corner 

###############################################################################


print("WELCOME TO STUDENT CORNER \nPlease write down you name in small letter")

Student_Name = str(input("Enter your name : "))

if Student_Name == "pappu":
    print("Your classroom number is 103")
elif Student_Name == "imtiaj":
    print("Your classroom number is 109")
elif Student_Name == "rashed":
    print("Your classroom number is 101")
else:
    print("Please contact registry Office we didn't find your name and CLASSES")


########################################################################################


a = int(input("Enter first number"))
b = int(input("Enter Second number"))
c = int(input("Enter Third number"))


if a < b and a < c:
    print("First number is the smallest number")
elif a < b and a > c:
    print("First number is less than 2nd number but greater than 2nd number")
elif a > b and a < c:
    print("First number is greater than 2nd number but less than 2nd number")
elif b > a and b > c:
     print("2nd number is greater than both number")
elif c > a and c > b:
     print("2nd number is greater than both number")
else:
    print("First number is bigger than any other number")