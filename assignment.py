def karkausvuosi():
    for vuosi in range(1800, 2201):
        if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
            print(vuosi)

def lukujono():
    lukujono = []
    luku = 1

    for i in range(1, 101):
        for j in range(1, i + 1):
            lukujono.append(j)
            
    for luku in lukujono[:100]:
        print(luku)
def perakkaisetLuvut():
    for luku in range(2, 101, 2):
        print(luku)
        print(luku - 1)

def tulosta_portaikko(askelma):
    for i in range(1, askelma * 2, 2):
        print("#" * i)
def aapelin_ika():
    for a in range(1, 100):
        if (a + 2) * (a + 1) * a == 42840:
            print("Aapeli on", a, " vuotta vanha")
            break
def vainion_ika():
    for a in range(1, 100):
        v = 2 * a
        if (2 * a - 20) == 3 * (a - 20):
            print(a)
            break

def pienin_positiivinen_kokonaisluku():
    i = 1
    while True:
        if i % 12 == 0 and i % 34 == 0 and i % 56 == 0:
            return i
        i += 1
        
        
pienin_luku = pienin_positiivinen_kokonaisluku()
print("Pienin positiivinen kokonaisluku, joka on jaollinen luvuilla 12, 34 ja 56, on:", pienin_luku)

if __name__ == "__main__":
    
    pienin_positiivinen_kokonaisluku()