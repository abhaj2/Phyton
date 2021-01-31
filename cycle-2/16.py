str1=input("Enter your first string\n")

str2=input("Enter your second string\n")

def chars(a, b):
  a1 = str2[:2] + str1[2:]
  a2 = str1[:2] + str2[2:]

  return a1 + ' ' + a2
print(chars(str1,str2))