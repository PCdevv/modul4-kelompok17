# Daftar buku tersedia di perpustakaan
buku_tersedia = ["Python Programming", "Data Science", "Machine Learning"]

# Function untuk menampilkan buku yang tersedia (Non-return type)
def tampilkan_buku():
    print("Daftar Buku Tersedia:")
    for buku in buku_tersedia:
        print(f"- {buku}")
    print()  # Spasi kosong untuk memperindah tampilan