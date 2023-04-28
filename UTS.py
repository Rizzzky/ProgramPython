masuk = True
while masuk == True:
    print("===================================================\n"
    "::::===>>>Menu Kalkulator Matematika<<<===:::\n"
    "A.Menghitung Ruang Datar\n"
    "B.Menghitung Ruang Bangun\n")
    pilih = input("Pilih A/B : ")
    if pilih == "A":
        print("===================================================\n"
        "Menu Ruang Datar\n"
        "1. Menghitung Luas dan Keliling Persegi\n"
        "2. Menghitung Luas dan Keliling Persegi Panjang\n"
        "3. Menghitung Luas dan Keliling Jajar Genjang\n"
        "4. Menghitung Luas dan Keliling Segitiga\n"
        "5. Menghitung Luas dan Keliling Belah Ketupat\n"
        "6. Menghitung Luas dan Keliling Layang-layang\n"
        "7. Menghitung Luas dan Keliling Trapesium\n"
        "8. Menghitung Luas dan Keliling Lingkaran\n"
        "9. Kembali\n")
        choise = input("Pilih Ruang Datar: ")
        if choise == "1":
            print("A. Luas Persegi\n"
            "B. Keliling Persegi\n")
            lk =input("Pilih A/B: ")
            if lk == "A":
                s = float(input("Masukan Sisi Persegi: "))
                l = s*s
                print("Luas Persegi Adalah= ",l)
            else:
                lk == "B"
                s = float(input("Masukan Sisi Persegi: "))
                k = 4*s
                print("Keliling Persegi Adalah: ",k)
        elif choise == "2":
            print("A. Luas Persegi Panjang\n"
            "B. Keliling Persegi Panjang\n")
            lk = input("Pilih A/B: ")
            if lk == "A":
                p = float(input("Masukan Panjang: "))
                l = float(input("Masukan Lebar: "))
                l = p*l
                print("Luas Persegi Panjang Adalah: ",l)
            else:
                lk == "B"
                p = float(input("Masukan Panjang: "))
                l = float(input("Masukan Lebar: "))
                k = (2*p)+(2*l)
                print("Keliling Persegi Panjang Adalah: ",k)
        elif choise == "3":
            print("A. Luas Jajar Genjang\n"
            "B. Keliling Jajar Genjang\n")
            lk = input("Pilih A/B: ")
            if lk == "A":
                a = float(input("Masukan Alas: "))
                t = float(input("Masukan Tinggi: "))
                l = a*t
                print("Luas Jajar Genjang Adalah: ",l)
            else:
                lk == "B"
                a = float(input("Masukan Alas: "))
                b = float(input("Masukan Sisi Miring: "))
                k = (2*a)+(2*b)
                print("keliling Jajar Genjang Adalah: ",k)
        elif choise == "4":
            print("A. Luas Segitiga\n"
            "B. Keliling Segitiga\n")
            lk = input("Pilih A/B: ")
            if lk == "A":
                a = float(input("Masukan Alas: "))
                t = float(input("Masukan Tinggi: "))
                l = 0.5*a*t
                print("Luas Segitiga Adalah: ",l)
            else:
                s == "B"
                a = float(input("Masukan Sisi Miring A: "))
                b = float(input("Masukan Sisi Miring B: "))
                c = float(input("Masukan Sisi Miring C: "))
                k = a+b+c
                print("Keliling Segitiga Adalah: ",k)
        elif choise == "5":
            print("A. Luas Belah Ketupat\n"
            "B. Keliling Belah Ketupat\n")
            lk = input("Pilih A/B: ")
            if lk == "A":
                d1 = float(input("Masukan Diagonal Ke 1: "))
                d2 = float(input("Masukan Diagonal Ke 2: "))
                l = 0.5*d1*d2
                print("Luas Belah Ketupat Adalah: ",l)
            else:
                lk == "B"
                s = float(input("Masukan Sisi Belah Ketupat: "))
                k = 4*s
                print("Keliling Belah Ketupat Adalah: ",k)
        elif choise == "6":
            print("A. Luas Layang-layang\n"
            "B. Keliling Layang-layang\n")
            lk = input("Pilih A/B: ")
            if lk == "A":
                d1 = float(input("Masukan Diagonal Ke 1: "))
                d2 = float(input("Masukan Diagonal Ke 2: "))
                l = 0.5*d1*d2
                print("Luas Layang-layang Adalah: ",l)
            else:
                lk == "B"
                a = float(input("Masukan Sisi A: "))
                b = float(input("Masukan Sisi B: "))
                c = float(input("Masukan Sisi C: "))
                d = float(input("Masukan Sisi D: "))
                k = a+b+c+d
                print("Keliling Layang-layang Adalah: ",k)
        elif choise == "7":
            print("A. Luas Trapesium\n"
            "B. Keliling Trapesium\n")
            lk = input("Pilih A/B: ")
            if lk == "A": 
                a = float(input("Masukan Alas A: "))
                b = float(input("Masukan Alas B: "))
                t = float(input("Masukan Tinggi Trapesium: "))
                l = 0.5*(a+b)*t
                print("Luas Trapesium Adalah: ",l)
            else:
                lk == "B"
                a = float(input("Masukan Sisi A: "))
                b = float(input("Masukan Sisi B: "))
                c = float(input("Masukan Sisi C: "))
                d = float(input("Masukan Sisi D: "))
                k = a+b+c+d
                print("Keliling Trapesium Adalah: ",k)
        elif choise == "8":
            print("A. Luas Lingkaran\n"
            "B. Keliling Lingkaran\n")
            lk = input("Pilih A/B: ")
            if lk == "A": 
                r = float(input("Masukan Jari-jari: "))
                l = 3.14*r**2
                print("Luas Lingkaran Adalah: ",l)
            else:
                lk == "B"
                r = float(input("Masukan Jari-jari: "))
                k = 2*3.14*r
                print("Keliling Lingkaran Adalah: ",k)
        else:
            choise == "9"
            masuk = True
    else:
        pilih == "B"
        print("===================================================\n"
        "Menu Ruang Bangun\n"
        "1. Menghitung Luas dan Volume Kubus\n"
        "2. Menghitung Luas dan Volume Balok \n"
        "3. Menghitung Luas dan Volume Prisma Segitiga \n"
        "4. Menghitung Luas dan Volume Limas Segiempat \n"
        "5. Menghitung Luas dan Volume Limas Segtiga \n"
        "6. Menghitung Luas dan Volume Tabung \n"
        "7. Menghitung Luas dan Volume Kerucut \n"
        "8. Menghitung Luas dan Volume Bola \n"
        "9. Kembali\n")
        milih = input("Pilih Ruang Bangun: ")
        if milih == "1":
            print("A. Menghitung Luas Kubus\n"
            "B. Menghitung Volume Kubus\n")
            vl = input("Pilih A/B: ")
            if vl == "A":
                r = float(input("Masukan Rusuk Kubus: "))
                l = 6*r**2
                print("Luas Kubus Adalah: ",l)
            else:
                vl == "B"
                s = float(input("Masukan Sisi Kubus: "))
                v = s**3
                print("Volume Kubus Adalah: ",v)
        elif milih == "2":
            print("A. Menghitung Luas Balok\n"
                "B. Menghitung Volume Balok\n")
            vl = input("Pilih A/B: ")
            if vl =="A":
                p = float(input("Masukan Panjang: "))
                l = float(input("Masukan Lebar: "))
                t = float(input("Masukan Tinggi: " ))
                luas = (2*p*l)+(2*p*t)+(2*l*t)
                print("Luas Balok Adalah: ",luas)
            else:
                vl == "B"
                p = float(input("Masukan Panjang: "))
                l = float(input("Masukan Lebar: "))
                t = float(input("Masukan Tinggi: " ))
                v = p*l*t
                print("Volume Balok Adalah: ",v)
        elif milih == "3":
            print("A. Menghitung Luas Prisma Segitiga\n"
                "B. Menghitung Volume Prisma Segitiga\n")
            vl = input("Pilih A/B: ")
            if vl =="A":
                la = float(input("Masukan Luas Alas: "))
                ka = float(input("Masukan Keliling Alas: "))
                tp = float(input("Masukan Tinggi Prisma: "))
                l= (2 * la)+(ka * tp)
                print("Luas Prisma Segitiga Adalah: ",l)              
            else:
                vl == "B"
                la = float(input("Masukan Luas Alas: "))
                tp = float(input("Masukan Tinggi Prisma: "))
                v = la * tp
                print("Volume Kubus Adalah: ",v)
        elif milih == "4":
            print("A. Menghitung Luas Limas SegiEmpat\n"
                "B. Menghitung Volume Limas SegiEmpat\n")
            vl = input("Pilih A/B: ")
            if vl =="A":
                s = float(input("Masukan Sisi Alas: "))
                t = float(input("Masukan Tinggi: "))
                ls = float(input("Masukan Luas Sisi Tegak: "))
                l = (s*s) + (4*ls)
                print("Luas Limas SegiEmpat Adalah: ",l)
            else:
                vl == "B"
                s = float(input("Masukan Sisi Alas: "))
                t = float(input("Masukan Tinggi: "))
                v = (1/3) * (s*s) * t
                print("Volume Kubus Adalah: ",v)
        elif milih == "5":
            print("A. Menghitung Luas Limas SegiTiga\n"
                "B. Menghitung Volume Limas SegiTiga\n")
            vl = input("Pilih A/B: ")
            if vl =="A":
                la = float(input("Masukan Luas Alas: "))
                ls = float(input("Masukan Luas Sisi Tegak: "))
                l = la + ls
                print("Luas Limas SegiTiga Adalah: ",l)
            else:
                vl == "B"
                la = float(input("Masukan Luas Alas: "))
                t = float(input("Masukan Tinggi: "))
                v = (1/3) * (la * t)
                print("Volume Limas SegiTiga Adalah: ",v)
        elif milih == "6":
            print("A. Menghitung Luas Tabung\n"
                "B. Menghitung Volume Tabung\n")
            vl = input("Pilih A/B: ")
            if vl =="A":
                t = float(input("Masukan Tinggi: "))
                d = float(input("Masukan Diameter: "))
                r = float(input("Masukan Jari-Jari: "))
                l = (3.14 * r * r) + (2 * 3.14 * r * t)
                print("Luas Tabung Adalah: ",l)
            else:
                vl == "B"
                r = float(input("Masukan Jari-Jari: "))
                t = float(input("Masukan Tinggi: "))
                v = 3.14*r*r*t
                print("Volume Tabung Adalah: ",v)
        elif milih == "7":
            print("A. Menghitung Luas Kerucut\n"
                "B. Menghitung Volume Kerucut\n")
            vl = input("Pilih A/B: ")
            if vl =="A":
                r = float(input("Masuka Jari-jari: "))
                s = float(input("Masukan Garis Pelukis Kerucut: "))
                l = (3.14*r*s) + (3.14*r*r)
                print("Luas Kerucut Adalah: ",l)
            else:
                vl == "B"
                t = float(input("Masuka Tinggi: "))
                r = float(input("Masukan Jari-Jari: "))
                v =  1/3 * 3.14 * r * r * t
                print("Volume Keurcut Adalah: ",v)
        elif milih == "8":
            print("A. Menghitung Luas Bola\n"
                "B. Menghitung Volume Bola\n")
            vl = input("Pilih A/B: ")
            if vl =="A":
                r = float(input("Masukan Jari-Jari: "))
                l = 4*3.14*r*r
                print("Luas Bola Adalah: ",l)
            else:
                vl == "B"
                r = float(input("Masukan Jari-Jari: "))
                v = (4/3)*3.14*r*r*r
                print("Volume Bola Adalah: ",v)
        else:
            milih == "9"
            masuk = True
            continue

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