def tampilkan_genre():
    print("Daftar Genre:")
    print("1. Aksi")
    print("2. Komedi")
    print("3. Drama")
    print("4. Horor")
    print("5. Romance")

def tampilkan_jenis_film(genre):
    if genre == 1:
        print("Jenis Film: Aksi")
    elif genre == 2:
        print("Jenis Film: Komedi")
    elif genre == 3:
        print("Jenis Film: Drama")
    elif genre == 4:
        print("Jenis Film: Horor")
    elif genre == 5:
        print("Jenis Film: Romance")
    else:
        print("Genre tidak valid")

    print("Harga Tiket:")
    print("Minggu: 50")
    print("Sabtu: 35")
    print("Hari lain: 40")

def hitung_harga(genre, hari, jumlah_tiket):
    if hari == "Minggu":
        harga_tiket = 50
    elif hari == "Sabtu":
        harga_tiket = 35
    else:
        harga_tiket = 40

    harga_total = harga_tiket * jumlah_tiket
    print("Total Harga:", harga_total)

def tampilkan_detail(nama, umur, genre, hari, jumlah_tiket):
    print("Detail Pembelian:")
    print("1. Nama:", nama)
    print("2. Umur:", umur)
    print("3. Genre:", genre)
    print("4. Hari Menonton:", hari)
    print("5. Jumlah Tiket:", jumlah_tiket)

def beli_tiket():
    nama = input("Masukkan nama: ")
    if not nama:
        return False

    umur = input("Masukkan umur: ")
    if not umur:
        return False

    tampilkan_genre()
    genre = int(input("Pilih genre (1-5): "))
    if genre < 1 or genre > 5:
        print("Genre tidak valid")
        return False

    tampilkan_jenis_film(genre)

    hari = input("Hari menonton (Minggu/Sabtu/Hari lain): ")
    if hari not in ["Minggu", "Sabtu", "Hari lain"]:
        print("Hari tidak valid")
        return False

    jumlah_tiket = int(input("Jumlah tiket yang ingin dibeli: "))
    if jumlah_tiket <= 0:
        print("Jumlah tiket tidak valid")
        return False

    hitung_harga(genre, hari, jumlah_tiket)

    konfirmasi = input("Konfirmasi pembelian (y/n): ")
    if konfirmasi.lower() == "y":
        tampilkan_detail(nama, umur, genre, hari, jumlah_tiket)
        return True
    else:
        return False

while True:
    lanjutkan = beli_tiket()
    if not lanjutkan:
        break
