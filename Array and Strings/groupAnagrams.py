from unittest import result


strs = ["eat","tea","tan","ate","nat","bat"]
#strs = [""]
adict={}
result=[]
for e in strs:
    st=''.join(sorted(e))
    if st not in adict:# Added as akey
        adict[st]=[]
        adict[st].append(e)

    else:
        adict[st].append(e) # Added in the key
for k in adict: # Append all the anagrams in a list
    result.append(adict[k])