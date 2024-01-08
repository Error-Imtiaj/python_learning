################################ SET ###############################

# SET RULES 
# SET TAKE DUPLICATE VALUE ONLY ONE TIME
# WE CAN'T GET SPECIFIC VALUE BY USING NAME[0] BECAUSE SET IS UNORDERED

name = {"rashede", "Mia", "Rahul", "Devraj"}  # TO START SET WE HAVE TO USE CURLY BRACKETS
y = list(name)

print(type(y)) # To check type
print(y)


############################# SET METHOD ########################################

l = {"progreamming", "School", "Software", "Devware", "Rashed"}
#l.add("hola") # To add data in SET

j = [1,2,3,45,5,6]
l.update(j) # TO ADD DATA FROM ANY LIST OR TUPLE OR SET USE UPDATE FUNCTION
l.remove(2) # TO REMOVE DATA FROM SET USE THE DETAILS OF THE DATA 
l.discard("ello") # USE DISCARD not to get any error if we use remove function and the specific data is not available in the set then Tewrminal wuill give an error so we use discard function to remove something without getting any error

print(l)


