#from curses.ascii import isalnum


from unicodedata import digit
from unittest import result



input = "2147483648"
sing = 1
result = 0
index=0
n=len(input)
#Discart all the whitespace in the begining of the string
while index < n and input[index] == ' ':
            index += 1
if index<n and input[index] =='+':
    sing=1
    index+=1
elif index<n and input[index] == '-':
    sing=-1
    index+=1
  
# Traverse next digits of input and stop if it is not a digit. 
# End of string is also non-digit character.
while index < n and input[index].isdigit():
    digit = int(input[index])
    result =10 * result + digit
    index+=1
result = sing * result
if result>=2**31:
    result = (2**31)-1
elif result<=-2**31:
    result = -2**31

print(result)
