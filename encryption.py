"""def encrypt(s):
    salattu = ""
    for i, y in enumerate(s):
        distance = i + 1 
        if ord(y) + distance > ord('z'):
            new_y = chr(ord(y) + distance - 26)
        else:
            new_y = chr(ord(y) + distance)
        salattu += new_y
    
    return salattu"""

def encrypt(s):
    salattu_merkkijono = ""

    for i, merkki in enumerate(s):
        siirto = i + 1  # Siirrettävä etäisyys kasvaa yhdellä jokaisella iteraatiolla
        uusi_merkki = chr((ord(merkki) - ord('a' if merkki.islower() else 'A') + siirto) % 26 + ord('a' if merkki.islower() else 'A'))

        salattu_merkkijono += uusi_merkki

    return salattu_merkkijono



if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("wocuuaqydurylxfuoronwiavagkhkwtyapehyicejeninplaczwez")) # bcdefghijklmnopqrstuvwxyzabcde