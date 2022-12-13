# 1 Ülesane
from math import *
print("Arvutage sinu normale pikkus.")
k=int(input("Mis on sinu kaal: "))
h=int(input("Mis on sinu kasv: "))
v=int(input("Mis on sinu vanus: "))
if h>0:
    n=h+10
    n2=h+10
    if n>n2: 
        print(f"Normale kasv {n}.")
    elif n2>n: 
        print(f"Normale kasv {n2}.")
    else:
        print(f"Sinu normale kasv on {n} cm.")
print()


# 2 Ülesane
try:
    p=int(input("Mis päev täna on "))
except:
    print("Vale")
if  p==1:
    print("Täna on 6 tundid.")
elif p==2:
    print("Täna on 4 tundid.")
elif p==3:
    print("Täna on 9 tundid.")
elif p==4:
    print("Täna on 6 tundid.")
elif p==5:
    print("Täna on 7 tundid.")
elif p==6:
    print("Täna ei ole tundid, puhkate.")
elif p==7:
    print("Täna on vimane päev kuni uus töönädala")
print()
    

#13.12.22
from random import *
r=randint(-100, 100)
a=randint(-100, 100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr: 
        print(f"Ruudu pindala {Skv} on suurem ringi pindala {Skr} m^2")
    elif Skr>Skv: 
        print(f"Ruudu pindala {Skv} on suurem ruudu pindala {Skr} m^2")
    else:
        print("Pindala on võrdsed. {Skr} m^2")
else:
    print(f"{a} ja {r} peavad > kui 0 olla")
print()
