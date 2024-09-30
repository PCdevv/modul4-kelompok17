# Daftar buku tersedia di perpustakaan
buku_tersedia = ["Python Programming", "Data Science", "Machine Learning"]

# Function untuk menampilkan buku yang tersedia (Non-return type)
def tampilkan_buku():
    print("Daftar Buku Tersedia:")
    for buku in buku_tersedia:
        print(f"- {buku}")
    print()  # Spasi kosong untuk memperindah tampilan

# Function untuk menambahkan buku baru ke dalam daftar (Return type tanpa parameter)
def tambah_buku():
    buku_baru = input("Masukkan judul buku yang ingin ditambahkan: ")
    buku_tersedia.append(buku_baru)
    return buku_baru