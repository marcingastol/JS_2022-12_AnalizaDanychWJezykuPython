import sys

# sprawdzenie kodowania
#print(sys.getdefaultencoding())

sciezka1 = "python1.txt"
sciezka2 = "python2.txt"
sciezka3 = "python3.txt"

# otwarcie pliku
plik = open(sciezka1, encoding="utf-8").read().splitlines()

#for linia in plik:
#    print(linia)

# zapis pliku
with open(sciezka2, mode="w") as operacje:
    operacje.writelines("1,2,3,4,5")

with open(sciezka2) as czytanie:
    linia = czytanie.readlines()

# sprawdzenie read()
plik = open(sciezka1, mode="rb")
print(plik.read())