class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data = []  # List untuk menyimpan data mahasiswa

    def tambah(self, nama, nilai):
        """Menambahkan data mahasiswa."""
        self.data.append({'nama': nama, 'nilai': nilai})
        print(f"Data {nama} berhasil ditambahkan.")

    def tampilkan(self):
        """Menampilkan daftar data mahasiswa."""
        if not self.data:
            print("Daftar nilai kosong.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for index, mahasiswa in enumerate(self.data, start=1):
                print(f"{index}. Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        for mahasiswa in self.data:
            if mahasiswa['nama'].lower() == nama.lower():
                self.data.remove(mahasiswa)
                print(f"Data {nama} berhasil dihapus.")
                return
        print(f"Data dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        """Mengubah data mahasiswa berdasarkan nama."""
        for mahasiswa in self.data:
            if mahasiswa['nama'].lower() == nama.lower():
                mahasiswa['nilai'] = nilai_baru
                print(f"Data {nama} berhasil diubah.")
                return
        print(f"Data dengan nama {nama} tidak ditemukan.")


# Contoh penggunaan class
daftar_nilai = DaftarNilaiMahasiswa()

# Menambahkan data
daftar_nilai.tambah("cindy", 90)
daftar_nilai.tambah("reva", 85)

# Menampilkan data
daftar_nilai.tampilkan()

# Mengubah data
daftar_nilai.ubah("cindy", 90)

# Menampilkan data setelah diubah
daftar_nilai.tampilkan()

# Menghapus data
daftar_nilai.hapus("reva")

# Menampilkan data setelah dihapus
daftar_nilai.tampilkan()
