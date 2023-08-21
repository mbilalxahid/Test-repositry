import active

x=0
while active:
    print(x)
    a=x
    x += 2
    if x>6:
        active=False

print(a)


