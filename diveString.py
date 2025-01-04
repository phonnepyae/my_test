str1 = 'hello'
str2 = 'hello'

print(id(str1) , id(str2))

str3 = str1 is str2

print(str3)

if str1 == str2:
  print("They are same value")  