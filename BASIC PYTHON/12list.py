name = ["codex" , "imtiaj" , "sanjida" , "kawser"]

#print(name[0 : 4])
print(name.append("codex"))


#########################      Data ADD and Remove IN LIST5  #################################

name1 = ["codex" , "imtiaj" , "sanjida" , "kawser"]

#print(name[0 : 4])
name1.append("jossy") #  ADD DATA
name1.insert(1, "bossy") # TO ADD DATA ON SPECIFIC POSITION
name1.remove("codex") # To delete or remove an data
del name1[0] # Delete data by writing its position


print(name1.index("jossy")) # To check DATA POSITION
print(name1)


######################## List Sort ######################################


number = [1,2,5,6,7,3,4,8,9]
#number.sort() # To organize data first to last
#number.reverse() # only for revise no sorting or organize data
#number.sort(reverse=True) #To organize data last to fast if false then first to last
numberCopy = number.copy() # To import number variable data to another variable

print(number)
