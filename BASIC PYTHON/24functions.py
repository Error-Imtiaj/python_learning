############## Function ##############
# def functionname(variable):

def cal(number, number2):
    result = number + number2
    print(result)

cal(int(input("Enter : ")),int(input("Enter : ")))

################################# another easy way to decrease code line ###########################

def calnam(*numb): # *variable to decrease code line
    rest = numb[0] - numb[1]
    print(rest)

calnam(int(input("Enter : ")),int(input("Enter : ")))
    