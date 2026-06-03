from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

#Generujemy klucze
klucz=RSA.generate(1024)
prywatny=klucz
publiczny=klucz.publickey()

#zapisywanie klucza publicznego, jest potrzebny aby zweryfikowac pozniej czy nasz dokument podpisany pochodzi od osoby ktora go podpisala
with open("klucz_publiczny.pem", "wb") as f:
    f.write(publiczny.exportKey("PEM"))

#odczytywanie oraz hashowanie danych w naszym glownym pliku
with open("dokument.txt", "rb") as f:
    dane=f.read()
hash=SHA256.new(dane)

#tworzymy obiekt ktory bedzie podpisywal nasz plik
obiekt_podpisujacy = pss.new(prywatny)
podpis = obiekt_podpisujacy.sign(hash)

#zapisujemy nasz podpis do pliku .sig
with open("dokument.txt.sig", "wb") as f:
    f.write(podpis)

print("Utworzono plik podpisu: dokument.txt.sig. Klucz publiczny zapisano jako klucz_publiczny.pem")