print (":: Nilai Predikat ::")
finish = False
while finish == False:
    skor = input("Skor Yang Di Dapat : ")
    if skor.isdigit() == False:
        print("Skor yang dimasukan invalid (harap masukan angka saja)! Mohon diulang")
        continue
    skor = int(skor)
    if skor > 100:
        print("Skor yang dimasukan invalid (harap masukan dari 0 sampai 100) ! Mohon diulang")
        continue
    if skor >= 90:
        variabel = "Nilai Huruf A Predikat Dengan Pujian"
    elif skor >= 80:
        variabel = "Nilai Huruf B Predikat Sangat Memusakan"
    elif skor >= 70:
        variabel = "Nilai Huruf C Predikat Memuaskan"
    elif skor >= 60:
        variabel = "Nilai Huruf D Predikat Tidak Memuaskan"
    else:
        skor < 59
        variabel = "Nilai Huruf F Predikat Tidak LLULUS"
    print ("Skor",skor,variabel)
    valid = False
    while valid == False:
        repeat = input("Ingin mengulang proses ? (Y/N) : ")
        if repeat.isdigit() == True:
            print ("Jawab Y/N")
            continue
        if repeat.upper() == "Y":
            valid = True
        if repeat.upper() == "N":
            finish = True
            valid = True
            print(":: Program Selesai ::")