s1 = 'and'
s2 = 'art'
def two_strings(s1,s2):
    for e in s1:
        for e2 in s2:
            if e==e2:
                return 'YES'
print(two_strings(s1,s2))

