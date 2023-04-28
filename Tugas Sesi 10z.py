def TabelHeader():
    print("="*90)
    print("NIM      \tNilai UTS   Nilai UAS\t   Total Nilai     Grade   Keterangan")
    print("="*90)
def PernyataanLulus():
    if grade in NilaiSiswa:
        print(MahasiswaNIM,end='\t')
        print(NilaiUTS,end='\t\t')
        print(NilaiUAS,end='\t\t')
        print(TotalNilai,end='\t\t')
        print(grade,end='\t')
        print('LULUS',end='\n')
        print("="*90)
    else:
        print(MahasiswaNIM,end='\t')
        print(NilaiUTS,end='\t')
        print(NilaiUAS,end='\t')
        print(TotalNilai,end='\t')
        print(grade,end='\t')
        print('TIDAK LULUS',end='\n')
        print("="*90)
ListSiswa = []
NilaiSiswa = ["A","B+","C+"]
JumlahMahasiswa = int(input("\nMasukkan Jumlah Data Mahasiswa : "))
print(f"Data ke - {JumlahMahasiswa}")
for i in range(JumlahMahasiswa):
    MahasiswaNIM = input("Masukkan NIM Mahasiswa : ")
    NilaiUTS = int(input("Masukkan Nilai UTS Mahasiswa : "))
    NilaiUAS = int(input("Masukkan Nilai UAS Mahasiswa : "))
    TotalNilai = ((NilaiUTS + NilaiUAS) / 2)
    if TotalNilai >= 90:
        grade = 'A'
    elif TotalNilai >= 80:
        grade = 'B+'
    elif TotalNilai >= 70:
        grade = 'B'
    elif TotalNilai >= 60:
        grade = 'C+'
    elif TotalNilai >= 50:
        grade = 'C'
    elif TotalNilai >= 40:
        grade = 'D'
    elif TotalNilai >= 30:
        grade = 'E'
    elif TotalNilai < 30:
        grade = 'F'
    else:
        print("Input yang kalian Masukkan Salah!!")
    TabelHeader()
    PernyataanLulus()