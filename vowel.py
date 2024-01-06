import re
a = input("")
vowel = "[aeiou]"
b = re.findall(vowel,a)
c = len(b)
print(c)
print(type(b))
i = 1
while i < c:
  print(b[i])
  i += 1
 
