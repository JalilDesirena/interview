from xml.dom.minidom import Element


s = "())"
map = {")":"(", "}":"{", "]":"["}
stack=[]
for c in s:
    if c in map:
        top_element = stack.pop() if stack else "#"
        if map[c] != top_element:
            print("False")
    else:
        stack.append(c)

print('True')


s='([{())}])'
#s="["
def isValid(s):
    stack=[]
    map={"(":")", "[":"]", "{":"}"}
    for c in s:
        if c in map:
            stack.append(c)
        else:
            if not stack:
                return False
            sp=stack.pop()
            if c != map[sp]:
                return False
    return not stack
a=isValid(s)
print(a)