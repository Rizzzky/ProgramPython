import datetime

# Data Buku
books = []

# Data Mahasiswa
students = []

# Data Peminjaman
borrowed_books = {}

def add_book(title, author):
  books.append({
    "title": title,
    "author": author
  })

def add_student(name, student_id):
  students.append({
    "name": name,
    "student_id": student_id
  })

def borrow_book(student_id, book_title, due_date):
  # Mendapatkan data mahasiswa
  student = None
  for s in students:
    if s["student_id"] == student_id:
      student = s
      break
  
  if student is None:
    raise Exception("Mahasiswa tidak ditemukan")
  
  # Mendapatkan data buku
  book = None
  for b in books:
    if b["title"] == book_title:
      book = b
      break
  
  if book is None:
    raise Exception("Buku tidak ditemukan")
  
  # Menambahkan data peminjaman
  borrowed_books[student_id] = {
    "student": student,
    "book": book,
    "due_date": due_date
  }

def return_book(student_id):
  # Mendapatkan data peminjaman
  borrowed_book = borrowed_books.get(student_id)
  if borrowed_book is None:
    raise Exception("Data peminjaman tidak ditemukan")
  
  # Menghitung denda
  today = datetime.datetime.now().date()
  due_date = borrowed_book["due_date"]
  if due_date < today:
    delta = today - due_date
    fine = 2000 * delta.days
    print(f"Mahasiswa harus membayar denda sebesar Rp. {fine}")
  
  # Menghapus data peminjaman
  del borrowed_books[student_id]
  print("Buku berhasil dikembalikan")

# Contoh penggunaan program
add_book("Belajar Python", "OpenAI")
add_student("Andi", "12345")

try:
  borrow_book("12345", "Belajar Python", datetime.date(2023, 2, 1))
  print("Buku berhasil dipinjam")
except Exception as e:
  print(e)

try:
  return_book("12345")
except Exception as e:
  print(e)
