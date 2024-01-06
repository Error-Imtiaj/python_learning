############################### FOR LOOP #############################
# Porgramming sequence
# for "anythiung" in "Variable" : print()

name ="Imtaij"

for i in name: # i can be anything no value
    print(i)
print("end")
# =========================


# FOR LOOP IN LIST TYPE

name =["Imtaij","hasan"]

for i in name: # i can be anything no value and also can be a value
    print(i)
print("end")

# start loop like while loop


for i  in range(1, 10 + 1): # range(start , (stop  + 1) condition)
    print(i)


############ Another example ###############

for i in range(1, 100+1, 2): # here condition is 2 . 2 means 2 gap
    print(i, end=' ') # use end = ' ' to get output vertically


################ Example of a odd number ###################

for odd in range(2, 100 , 2):
    print(odd, end= ' ')
    


############ Total number loop ###########
totalNumber=0
for jor in range(1,100,2):
    totalNumber =totalNumber+jor
print(totalNumber)