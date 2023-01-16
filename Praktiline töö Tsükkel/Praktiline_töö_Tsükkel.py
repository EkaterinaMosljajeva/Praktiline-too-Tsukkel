from math import *
from random import *
import string

#0
#print("while")
#print("Sa pead ära arvama juhuslikult mõistatatud arvu (1-100). 10 katsega")
#r=randint(1,100)
#n=1
#while n<=10:
#    o=int(input("Sisesta arv: "))
#    if o==r:
#        print(f"Sa arvasid, et sul läks {n} katset.")
#        break
#    elif r>o:
#        print("Liiga väike")
#    elif o>r:
#        print("Liiga suur")
#    n=n+1

#print("while True")
#print("Sa pead ära arvama juhuslikult mõistatatud arvu (1-100). 10 katsega")
#n=1
#r=randint(1,100)
#while True:
#    if n<=10:
#        o=int(input("Sisesta arv: "))
#        if o==r:
#            print(f"Sa arvasid, et sul läks {n} katset.")
#            break
#        elif r>o:
#            print("Liiga väike")
#        elif o>r:
#            print("Liiga suur")
#        n=n+1
#    else:
#        break
    
#print("for")
#print("Sa pead ära arvama juhuslikult mõistatatud arvu (1-100). 10 katsega")
#r=randint(1,100)
#for n in range(1,11):
#    o=int(input("Sisesta arv: "))
#    if o==r:
#        print(f"Sa arvasid, et sul läks {n} katset.")
#        break
#    elif r>o:
#        print("Liiga väike")
#    elif o>r:
#        print("Liiga suur")
#    n=n+1

#3
#try:
#    f=int(input("Mitu ülesandeid sa tahad? "))
#    for d in range (o,f,1):
#        print(f"ülesanne{g}: ")
#        a=randint(1,50)
#        b=randint(1,50)
#        c=a+b
#        for i in range(0,5,1):
#            answer=int(input(f"{a}+{b}=? "))
#            if answer == a+b:
#                print("see on õige")
#                break
#            else:
#                print("Proovi veel korra")
#                print()
#        g=g+1
#        print(f"õige on {c}")
#except:
#    print("See ei ole õige")


#9
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
#while x<=100:
#    if x%5==0:
#        print(x, end=" ")
#    x+=1

#13
#print("arv", "   ruut ", "   kuup")
#for i in range(1,11):
#    print(f" {i}    {i**2}     {i**3}")

#print("arv", "   ruut ", "   kuup")
#i=1
#while 1<11:
#    print(f" {i}    {i**2}     {i**3}")
#    i+=1
    
#16
#ans=random.randint(1,10)
#while True:
#    g=input("mis numbri ma arvasin?(1-10, mängu lõpetamiseks kirjutage *lõpp*) \n")
#    if g.lower()=="lõpp":
#        print("mäng on labi!")
#        break
#    if not g.isnumeric():
#        print("Vale andmetüüp!")
#    g=int(g)
#    if g == ans:
#        print("õige! sa arvasid ära")
#    if g>10 or g<1:
#        print("Vahemik on vale!")
#    elif g!=ans:
#        print("Vale! Proovi veel korra!")

#17
#try:
#    num_horiz=int(input("Sisesta ruutude arv horisontaalselt => \n"))
#except:
#    print("Value Error")
#    num_horiz=randint(1,20)
#try:
#    num_vert=int(input("Sisesta ruutude arv vertikaalselt => \n"))
#except:
#    print("Value Error")
#    num_vert=randint(1,20)

#for y in range(num_vert):
#    for x in range(num_horiz):
#        print(" ", end=" ")
#    print()


#######################
#import string
#print("Arva taht - Aa kuni Zz)")
#letter = random.choise(string.ascii_letters)

#while True:
#    answ = str(input("Teie oletus: "))
#    if letter == answ:
#        print("Tubli!")
#        break
#    else:
#        print("Provi uuesti")