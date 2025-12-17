import csv
import os

FILE_DATA = "data_mahasiswa.csv"

# ================= CLASS =================
class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.tugas = 0
        self.uts = 0
        self.uas = 0
        self.hadir = 0
        self.total_pertemuan = 0

    def nilai_akhir(self):
        hitung = lambda t, u1, u2: 0.3*t + 0.35*u1 + 0.35*u2
        return hitung(self.tugas, self.uts, self.uas)

    def persentase_hadir(self):
        if self.total_pertemuan == 0:
            return 0
        return (self.hadir / self.total_pertemuan) * 100


# ================= DATA =================
mahasiswa = []


def load_data():
    if not os.path.exists(FILE_DATA):
        return
    with open(FILE_DATA, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            m = Mahasiswa(row[0], row[1])
            m.tugas = float(row[2])
            m.uts = float(row[3])
            m.uas = float(row[4])
            m.hadir = int(row[5])
            m.total_pertemuan = int(row[6])
            mahasiswa.append(m)


def save_data():
    with open(FILE_DATA, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for m in mahasiswa:
            writer.writerow([
                m.nim, m.nama,
                m.tugas, m.uts, m.uas,
                m.hadir, m.total_pertemuan
            ])


def cari_mahasiswa(nim):
    for m in mahasiswa:
        if m.nim == nim:
            return m
    return None


# ================= MENU FITUR =================
def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    if cari_mahasiswa(nim):
        print("NIM sudah ada.")
        return
    nama = input("Masukkan Nama: ")
    mahasiswa.append(Mahasiswa(nim, nama))
    print("Mahasiswa berhasil ditambahkan.")


def input_nilai():
    nim = input("Masukkan NIM: ")
    m = cari_mahasiswa(nim)
    if not m:
        print("Mahasiswa tidak ditemukan.")
        return
    m.tugas = float(input("Nilai Tugas (0-100): "))
    m.uts = float(input("Nilai UTS (0-100): "))
    m.uas = float(input("Nilai UAS (0-100): "))
    print("Nilai berhasil diinput.")


def input_presensi():
    pertemuan = int(input("Pertemuan ke-: "))
    jenis = "Teori" if pertemuan % 2 == 1 else "Praktikum"
    print("Jenis pertemuan:", jenis)

    for m in mahasiswa:
        status = input(f"{m.nama} (Hadir/Alpha/Izin): ").lower()
        m.total_pertemuan += 1
        if status == "hadir":
            m.hadir += 1


def tampilkan_data():
    print("\n================ DATA MAHASISWA ================")
    print("NIM | Nama | Nilai Akhir | Grade | Kehadiran")
    print("-" * 55)

    konversi_grade = lambda n: (
        "A" if n >= 85 else
        "B" if n >= 70 else
        "C" if n >= 55 else
        "D" if n >= 40 else "E"
    )

    for m in mahasiswa:
        akhir = m.nilai_akhir()
        print(f"{m.nim} | {m.nama} | {akhir:.2f} | "
              f"{konversi_grade(akhir)} | {m.persentase_hadir():.2f}%")
    print("=" * 55)


# ================= MENU UTAMA =================
def menu():
    load_data()
    while True:
        print("""
===== MENU =====
1. Tambah Mahasiswa
2. Input Nilai
3. Input Presensi
4. Tampilkan Data
5. Simpan & Keluar
""")
      
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_mahasiswa()
        elif pilih == "2":
            input_nilai()
        elif pilih == "3":
            input_presensi()
        elif pilih == "4":
            tampilkan_data()
        elif pilih == "5":
            save_data()
            print("Data disimpan. Program selesai.")
            break
        else:
            print("Menu tidak valid.")


menu()