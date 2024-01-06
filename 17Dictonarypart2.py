our = {
    "name" : "pappu dey",
    "Roll" : 21,
    "Class": 5,
    "Department":"Science",
    "Institiute name" : "Fatehabad Model Multilateral High School",
}

ourFamily = our.copy()# TO COPY A DICTONARY

print(ourFamily)

################################### NESTED DICTONARY #########################

#   CREATE A DICTONARY INSIDE A DICTONARY IS A NESTED DICTONARY

ourg = {
    "name" : "pappu dev",
    "Roll" : 21,
    "Class": 5,
    "Department":"Science",
    "Institiute name" : "Fatehabad Model Multilateral High School",
    "Subdic" : { "namef" : "Mohammad Imtiaj", "Age" : 16, }
}
print(ourg)