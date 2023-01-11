from math import *
from random import *

#0
print("while")
print("Sa pead ära arvama juhuslikult mõistatatud arvu (1-100). 10 katsega")
r=randint(1,100)
n=1
while n<=10:
    o=int(input("Sisesta arv: "))
    if o==r:
        print(f"Sa arvasid, et sul läks {n} katset.")
        break
    elif r>o:
        print("Liiga väike")
    elif o>r:
        print("Liiga suur")
    n=n+1

print("while True")
n=1
r=randint(1,100)
while True:
    if n<=10:
        o=int(input("Sisesta arv: "))
        if o==r:
            print(f"Sa arvasid, et sul läks {n} katset.")
            break
        elif r>o:
            print("Liiga väike")
        elif o>r:
            print("Liiga suur")
        n=n+1
    else:
        break
    
print("for")
print("Sa pead ära arvama juhuslikult mõistatatud arvu (1-100). 10 katsega")
r=randint(1,100)
for n in range(1,11):
    o=int(input("Sisesta arv: "))
    if o==r:
        print(f"Sa arvasid, et sul läks {n} katset.")
        break
    elif r>o:
        print("Liiga väike")
    elif o>r:
        print("Liiga suur")
    n=n+1



#9----------
print("for")
for i in range(1,11):
    x=5*i
    print(f"5x{i}={x}")

print("while")
n=1
while n<=10:
    x=5*n
    print(f"5x{n}={x}")
    n=n+1

print("while True")
n=1
while True:
    if n<=10:
        x=5*n
        print(f"5x{n}={x}")
        n=n+1
    else:
        break

#10
while x<=100:
    if x%5==0:
        print(x, end=" ")
    x+=1

#17
try:
    num_horiz=int(input("Sisesta ruutude arv horisontaalselt => \n"))
except:
    print("Value Error")
    num_horiz=randint(1,20)
try:
    num_vert=int(input("Sisesta ruutude arv vertikaalselt => \n"))
except:
    print("Value Error")
    num_vert=randint(1,20)

for y in range(num_vert):
    for x in range(num_horiz):
        print(" ", end=" ")
    print()