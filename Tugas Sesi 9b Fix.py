
import sys

daftar_huruf = [] # Untuk Menampung huruf
for i in range(0,10): # mengulang dari 1 hingga 10
    vocal_huruf = input(f"Ketikkan huruf ke-{i+1}: ").lower()
    if not len(vocal_huruf) < 2:
        print("Maaf, Input SALAH!!! Cukup 1 huruf setiap baris. Program Ditutup")
        sys.exit()
    daftar_huruf.append(vocal_huruf)
list_vocal = [vocal_huruf for vocal_huruf in daftar_huruf if vocal_huruf in "aiueo"]
vocal = len(list_vocal)
not_vocal = len(daftar_huruf) - vocal
print(f"Jadi, vokal ada {vocal} dan huruf konsonan ada {not_vocal}")