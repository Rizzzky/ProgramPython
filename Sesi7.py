
masuk = True
while masuk == True:
    print("))===>>>Program Kalkulator Sederhana<<<===((")
    print("Menu")
    print("1. Hitung Luas Segitiga")
    print("2. Hitung Luas Persegi Panjang")
    print("3. Tentukan Number Ganjil atau Genap")
    print("4. Quit")
    pilih = input("Pilih Menu: ")
    if pilih == "1":
        a = float(input("Masukan Alas: "))
        t = float(input("Masukan Tinggi: "))
        lsegi = 0.5*a*t
        print("Luas Segi Tiga adala = ",str(lsegi))
    elif pilih == "2":
        p = float(input("Masukan Panjang: "))
        l = float(input("Masukan Lebar: "))
        lpanjang = p*l
        print("Luas Persegi Panjang adalah = ",str(lpanjang))
    elif pilih == "3":
        x = int(input("Masukan Number Bilangan: "))
        print("Number Bilangan Tersebut Adalah","Genap" if (x % 2 == 0) else "Ganjil")
    else: 
        pilih == "4"
        print("Quit")
        break
    valid = False
    while valid == False:
        repeat = input("Ingin mengulang proses ? (Y/N) : ")
        if repeat.isdigit() == True:
            print ("Jawab Y/N")
            continue
        if repeat.upper() == "Y":
            valid = True
        if repeat.upper() == "N":
            masuk = False
            valid = True
            print(":: Program Selesai ::")