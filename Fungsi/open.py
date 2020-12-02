from syntax import lab6

print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||------------------||Program Input Nilai||------------------||")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

data = {}

while True:
    print("\n")
    tabel = input("(L) Lihat, (T) Tambah, (U) Ubah, (H) Hapus, (C) Cari, (K) Keluar: ")
    print("\n")

    if tabel.lower() == 'k':
        print("Keluar")
        break

    elif tabel.lower() == 'l':
        lab6.lihat()

    elif tabel.lower() == 't':
        lab6.tambah()
        
    elif tabel.lower() == 'u':
        lab6.ubah()

    elif tabel.lower() == 'c':
        lab6.cari()

    elif tabel.lower() == 'h':
        lab6.hapus()
        
