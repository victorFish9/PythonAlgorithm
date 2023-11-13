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

if __name__ == "__main__":
    #karkausvuosi()
    #lukujono()
    perakkaisetLuvut()