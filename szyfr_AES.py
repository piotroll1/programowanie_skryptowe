#import biblioteki z modulu crypto.cihper
from Crypto.Cipher import AES

#uzytkownik wpisuje nazwe pliku ktory chce zaszfyrowac
plik=input("wpisz plik, ktory chcesz zaszyfrowac: ")
#wydobrebniona nazwa potrzebna do utworzenia kopii pliku
t=plik.split(".")[0]

def szyfr_AES(plik):
    #zapisuje do zmiennej plaintext czysty tekst z pliku podanego przez uzytkownika
    with open(plik,'r') as f:
        plaintext=f.read()
    #zapisanie klucza (AES-128)
    klucz = b"ToJest16Bajtklcz"
    szyfr=AES.new(klucz,AES.MODE_EAX)
    #zapisanie nonce czyli informacji jak zaszyfrowalismy ten plik (pomoze w odszyfrowaniu)
    klucz_nonce = szyfr.nonce
    ciphertext=szyfr.encrypt(plaintext.encode("UTF-8"))
    return ciphertext,klucz_nonce
    #funkcja zwraca dwie wartosci, zaszyfrowana tresc oraz nonce

#warunek jezeli program jest odpalany z "glownej strony"
if __name__ == '__main__':
    szyfr, nonce = szyfr_AES(plik)
    #nonce jest w formie zaszfyrowanej, zmieniamy aby bylo w formacie hex
    nonce_tekst=nonce.hex()
    wynik=t+"_"+nonce_tekst+"_zaszyfrowany.txt"
    #zapisanie szyfru do kopii naszego pliku
    with open(wynik,'wb') as f:
        f.write(szyfr)
