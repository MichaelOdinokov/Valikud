#
from math import *
    

from math import *
print("Sisseloginine tahvel")
try:
    vanus=int(input("Kui vana sa oled? "))
    if vanus>=18:
        print("Kas te annate vanematele loa oma Tahvelit vaadata? ")
        o=(input("Jah või ei. "))
        if o.lower()=="jah": #upper() muutaja  sõnad surem
            print({o})
            print("See on ligipääs teie vanematele.")
            print("Tahvel on kini. ")
        elif o.upper()=="Ei":
            print("Siesepääs puudub. ")
            print("Tahvel on kinni")
    if 18>vanus:
        print("Juurdepääs vanematele on automaatselt antud. ")
except:
    print("Tahvel on kinni.")
print()




# minu ülesane 2
from math import *
print("Arvutage sinu normale pikkus.")
k=int(input("Mis on sinu kaal: "))
h=int(input("Mis on sinu kasv: "))
v=int(input("Mis on sinu vanus: "))
try:
    if h>0:
        n=h+10
    if n: 
        print(f"Sinu normale kasv {n} cm.")
except:
    print("Vale")






# minu ülesane 1
try:
    p=int(input("Mis päev täna on "))
except:
    print("Vale")
if  p==1:
    print("Täna on 6 tundi.")
elif p==2:
    print("Täna on 4 tundi.")
elif p==3:
    print("Täna on 9 tundi.")
elif p==4:
    print("Täna on 6 tundi.")
elif p==5:
    print("Täna on 7 tundi.")
elif p==6:
    print("Täna ei ole tundi, puhkate.")
elif p==7:
    print("Täna on 0 tundi. ")
print()

#
try:
    päev=int(input("Mis päev ja mitu tundi täana on ?"))
    if päev==1:
        n="Esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="Teisepäev"
        n="8 tundi"
    elif päev==3:
        n="Kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="Neljapäev"
        n="5 tundi"
    elif päev==5:
        n="Reede"
        n="7 tundi"
    elif päev==6:
        n="Laupäev"
        n="0 tundi"
    elif päev==7:
        n="Pühapäev"
        n=" 0 tundi"
    else:
        n="vale number"
    print(n) 
except:
    print("!!!")



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
