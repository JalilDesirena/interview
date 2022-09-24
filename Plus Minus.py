arr = [1, 1, 0, -1, -1]
t = len(arr)
p = 0
ng = 0
z = 0

for e in arr:
    if e > 0:
        p += 1
    if e < 0:
        ng += 1
    if e == 0:
        z += 1
print(p/t)
print(ng/t)
print(z/t)
