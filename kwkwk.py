import datetime

books = []
students = []
loans = []

def input_book():
  title = input("Masukkan judul buku: ")
  author = input("Masukkan penulis buku: ")
  book = {
    "title": title,
    "author": author
  }
  books.append(book)
  print("Buku baru berhasil ditambahkan.")

def input_student():
  name = input("Masukkan nama mahasiswa: ")
  student_id = input("Masukkan nomor identitas mahasiswa: ")
  student = {
    "name": name,
    "student_id": student_id
  }
  students.append(student)
  print("Mahasiswa baru berhasil ditambahkan.")

def input_loan():
  student_id = input("Masukkan nomor identitas mahasiswa peminjam: ")
  book_title = input("Masukkan judul buku yang dipinjam: ")
  due_date = input("Masukkan tanggal harus dikembalikan (dd/mm/yyyy): ")
  due_date = datetime.datetime.strptime(due_date, "%d/%m/%Y").date()

  student = None
  book = None
  for s in students:
    if s["student_id"] == student_id:
      student = s
      break

  for b in books:
    if b["title"] == book_title:
      book = b
      break
  
  if student is None:
    print("Mahasiswa tidak ditemukan.")
  elif book is None:
    print("Buku tidak ditemukan.")
  else:
    loan = {
      "student": student,
      "book": book,
      "due_date": due_date
    }
    loans.append(loan)
    print("Peminjaman buku berhasil.")

def calculate_late_fee(loan):
  today = datetime.date.today()
  delta = today - loan["due_date"]
  if delta.days > 0:
    return 2000 * delta.days
  else:
    return 0

def main():
  while True:
    print("Pilih menu:")
    print("1. Input data buku baru")
    print("2. Input data mahasiswa anggota perpustakaan")
    print("3. Input data peminjaman buku")
    print("4. Tampilkan data peminjaman buku")
    print("5. Keluar")
    choice = int(input("Masukkan pilihan: "))

    if choice == 1:
      input_book()
    elif choice == 2:
      input_student()
    elif choice == 3:
      input_loan()
    elif choice == 4:
      for loan in loans:
        late_fee = calculate_late_fee(loan)
        print("Nama Data Peminjam Buku")
    else:
      choice == 5
      break
