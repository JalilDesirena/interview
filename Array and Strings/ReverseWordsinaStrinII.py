from os import stat
from random import randrange


s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
def reverse_strings(s, start, end):
    #start=0
    #end=len(s)-1
    aux=''
    while start<end:
        aux=s[end]
        s[end]=s[start]
        s[start]=aux
        start+=1
        end-=1


def reverse_word(l):
    end=start=0
    n=len(l)
    while start<n:
        while end<n and l[end]!=" ": # we are looking for the end of the word (black space)
            end+=1
        reverse_strings(s, start, end-1) # Call the function to reverse the word
        start=end +1 # Now the start of the followed word is the end +1 of the previous one
        end+=1

reverse_strings(s, 0, len(s)-1)
reverse_word(s)

print(s)

