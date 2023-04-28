finish = False
while finish == False:
    NIMSiswa = []
    UTSSiswa = []
    UASSiswa = []
    NilaiSiswa = []
    GradeSiswa = []
    NilaiLulus = ["A","B","B+","C","C+"]
    JumlahMahasiswa = input("\nMasukkan Jumlah Data Mahasiswa : ")
    if JumlahMahasiswa.isdigit() == False:
        print("Jumlah yang dimasukan invalid (harap masukan angka saja)! Mohon diulang")
        continue
    JumlahMahasiswa = int(JumlahMahasiswa)
    for i in range(JumlahMahasiswa):  
        print(f"Data ke - {i+1}")
        MahasiswaNIM = input("Masukkan NIM Mahasiswa : ")
        NilaiUTS = int(input("Masukkan Nilai UTS Mahasiswa : "))
        NilaiUAS = int(input("Masukkan Nilai UAS Mahasiswa : "))
        TotalNilai = ((NilaiUTS + NilaiUAS) / 2)
        NIMSiswa.append(MahasiswaNIM)
        UTSSiswa.append(NilaiUTS)
        UASSiswa.append(NilaiUAS)
        NilaiSiswa.append(TotalNilai)
        if TotalNilai >= 90:
            grade = 'A'
            GradeSiswa.append(grade)
        elif TotalNilai >= 80:
            grade = 'B+'
            GradeSiswa.append(grade)
        elif TotalNilai >= 70:
            grade = 'B'
            GradeSiswa.append(grade)
        elif TotalNilai >= 60:
            grade = 'C+'
            GradeSiswa.append(grade)
        elif TotalNilai >= 50:
            grade = 'C'
            GradeSiswa.append(grade)
        elif TotalNilai >= 40:
            grade = 'D'
            GradeSiswa.append(grade)
        elif TotalNilai >= 30:
            grade = 'E'
            GradeSiswa.append(grade)
        else:
            TotalNilai < 30
            grade = 'F'
            GradeSiswa.append(grade)

    # Print Table Result
    print("="*100)
    print("NIM\t\t Nilai UTS\t   Nilai UAS\t   Total Nilai\t     Grade\t   Keterangan")
    print("="*100)
    for y in range(len(NIMSiswa)):
        print(NIMSiswa[y],end='\t\t')
        print(UTSSiswa[y],end='\t\t')
        print(UASSiswa[y],end='\t\t')
        print(NilaiSiswa[y],end='\t\t')
        print(GradeSiswa[y],end='\t\t')
        if GradeSiswa[y] in NilaiLulus:
            print('LULUS',end='\n')
        else:
            print('TIDAK LULUS',end='\n')
    print("="*100)

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