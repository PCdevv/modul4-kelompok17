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

# Method untuk meminjam buku (Non-return type)
class Perpustakaan:
    def _init_(self, nama_anggota):
        self.nama_anggota = nama_anggota
        self.buku_dipinjam = []

    # Method non-return type untuk meminjam buku
    def pinjam_buku(self, judul_buku):
        if judul_buku in buku_tersedia:
            buku_tersedia.remove(judul_buku)
            self.buku_dipinjam.append(judul_buku)
            print(f"{self.nama_anggota} telah meminjam buku '{judul_buku}'.\n")
        else:
            print(f"Maaf, buku '{judul_buku}' tidak tersedia.\n")

    # Method return type dengan parameter
    def kembalikan_buku(self, judul_buku):
        if judul_buku in self.buku_dipinjam:
            self.buku_dipinjam.remove(judul_buku)
            buku_tersedia.append(judul_buku)
            return f"Buku '{judul_buku}' telah dikembalikan oleh {self.nama_anggota}.\n"
        else:
            return f"{self.nama_anggota} tidak meminjam buku berjudul '{judul_buku}'.\n"