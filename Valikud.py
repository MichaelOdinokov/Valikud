# 2 Ülesane
from math import *
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



# 1 Ülesane
k=int(input("Mis on sinu kaal: "))
h=int(input("Mis on sinu kasv: "))
v=int(input("Mis on sinu vanus: "))
if k>0 or h>0 or v>0:
    N=k+v/h
    N2=k+v/h
    if N>N2:
        print(f"Normaalne pikkus ja kaal {N}, kuni {N2} juures.")
    elif N2>N:
        print(f"Normaalne pikkus ja kaal {N2}, kuni {N} juures.")

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
