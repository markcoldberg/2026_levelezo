# vezérlőszerkezetek és függvény:
# paramétert adni függvénynek és visszakapni

def korszamlalas (kor):
    while kor < 65:
        kor += 1
        if kor == 52:
            continue
        print(kor)
        kor += 1
        if kor == 55:
            break
    else:
        print('nyugger')
    print('Vége')
    return kor

# programfutás
kor = 56
print('nyugdíj: ', korszamlalas(kor))

felhasznalo_kora = 20 #int(input('Hány éves vagy: '))
if felhasznalo_kora < 18:
    print('gyerek')
elif felhasznalo_kora < 30:
    print('ifjú')
elif felhasznalo_kora < 65:
    print('felnőtt')
else:
    print('nyugger')

