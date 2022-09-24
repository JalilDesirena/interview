"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
s = "abcabcbb"
#s = "bbbbbbbb"

subs = []
su = []
len_aux =0
i = 0
while i < len(s):
    j=i
    su = []
    for j in range(j,len(s)):
        if s[j] in su:
            break
        su.append(s[j])
    if len(su) > len_aux:
        result = su
    len_aux = len(su)
    i += 1
print(''.join(result))
