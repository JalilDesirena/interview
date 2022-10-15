   
s = ["H","a","n","n","a","h"]
aux=''
# We will have two pointers one pointing to the begining 
# and the other one pointing to the end
"""i=0
j=len(s)-1 
while i<j:
    aux=s[j]
    s[j]=s[i]
    s[i]=aux
    i+=1
    j-=1
"""
i=0
j=len(s)-1
aux=''
while i<j:
    aux=s[j]
    s[j]=s[i]
    s[i]=aux
    i+=1
    j-=1
print(s)