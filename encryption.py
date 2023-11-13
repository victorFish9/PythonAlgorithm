def encrypt(s):
    salattu = ""
    for i, y in enumerate(s):
        distance = i + 1 
        if ord(y) + distance > ord('z'):
            new_y = chr(ord(y) + distance - 26)
        else:
            new_y = chr(ord(y) + distance)
        salattu += new_y
    
    return salattu


if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde