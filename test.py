

a = []
x='wrfwrf'

while x!='':
    c= input("please enter a type")
    a.append(c)
    if c=='':
        a.pop()
    x = c

print(a)