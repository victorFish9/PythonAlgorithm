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

def mahdollinen_koodi():
    x = 0
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    if a * b * c * d == 252:
                        x += 1
                        print(f"Mahdollinen koodi: {a}{b}{c}{d}")
    print(x)

def mahdollinen_koodi2():
    x = 0
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    
                    x += 1
                        #print(f"Mahdollinen koodi: {a}{b}{c}{d}")
    print(x)
def mahdollinen_koodi3():
    x = 0
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        x += 1
                        #print(f"Mahdollinen koodi: {a}{b}{c}{d}")
    print(x)

def nopanheitto():
    x = 0

    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                for d in range(1, 7):
                    for e in range(1, 7):
                        if a + b + c + d + e == 15:
                            x += 1
    print(x)

def pythogora():
    x = 0

    for a in range(1, 51):
        for b in range(a, 51):  
            c_squared = a**2 + b**2
            c = int(c_squared**0.5)  # Tarkistetaan, että c on kokonaisluku
            if c_squared == c**2 and c <= 50:
                x += 1

    print(x)

def shakki():
    count = 0

    for q1_row in range(8):
        for q1_col in range(8):
            for q2_row in range(8):
                for q2_col in range(8):
                    if (q1_row, q1_col) != (q2_row, q2_col) and \
                    (q1_row != q2_row and q1_col != q2_col and \
                        abs(q1_row - q2_row) != abs(q1_col - q2_col)):
                        count += 1

    print("Tapojen määrä 8x8-shakkilaudalla:", count)
if __name__ == "__main__":
    shakki()
    