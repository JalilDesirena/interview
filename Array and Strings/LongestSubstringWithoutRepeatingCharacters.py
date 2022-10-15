#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#1. Recorrer el string
    #1.2 Crear una lista y verificar si la letra ya se encuentra en la lista si no anadirla, si ya existe resetiar la lista y guardar el tamano de lista

from operator import index


s = "abcacbb"
s = "pwwkew"
s = "bbbbb"
s = " "
s = "abcadcbb"
list_chart=[]
longest = 0
index = 0
for e in s:
    if e not in list_chart:
        list_chart.append(e)
    else:
        longest = max(len(list_chart), longest)
        cut = list_chart.index(e)
        list_chart = list_chart[cut+1:]
        list_chart.append(e)
print(longest)


ans = 0
sub = ''
for char in s:
    if char not in sub:
        sub += char
        ans = max(ans, len(sub))
    else:
        cut = sub.index(char)
        sub = sub[cut+1:] + char
print (ans)
