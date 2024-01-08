# Tuple and list are similar but they have some difference

x = ("codex", "devware") # Start tuple with first bracket
y = ("Software", "Developer")
d = list("apply") # creatre list
f = list(x) # convert tuple to list


print(x)
print(x+y)
print(d)
print(f)

##  YOU CAN'T ADD DATA TO TUPLE SO WE HAVE TO CONVERT TUPLE TO LIST THEN CONVERT LIST TO TUPLE

n = ("rashede", "Mia", "Rahul", "Devraj")

k = list(n)
k.append("Jakku")
n = tuple(k)

print(n)