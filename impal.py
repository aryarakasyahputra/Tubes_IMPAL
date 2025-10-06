import time

# ===============================
# Data Pengguna (Simulasi Database)
# ===============================
users = {
    "081234567890": {"balance": 50000, "history": []},
    "081298765432": {"balance": 20000, "history": []},
    "081355555555": {"balance": 10000, "history": []},
}


# Fungsi: Cek Pulsa
def cek_pulsa(nomor):
    if nomor not in users:
        print("Nomor tidak terdaftar dalam sistem.")
        return
    saldo = users[nomor]["balance"]
    print(f"\nPulsa Anda saat ini Rp {saldo:,}")
    users[nomor]["history"].append(
        {"time": time.strftime("%d-%m-%Y %H:%M"), "type": "Cek Pulsa", "amount": 0}
    )


# Fungsi: Transfer Pulsa
def transfer_pulsa(pengirim, penerima, jumlah):
    if pengirim not in users:
        print("Nomor pengirim tidak terdaftar.")
        return
    if penerima not in users:
        print("Nomor tujuan tidak ditemukan.")
        return
    if pengirim == penerima:
        print("Tidak dapat transfer ke nomor sendiri.")
        return
    if jumlah <= 0:
        print("Jumlah pulsa tidak valid.")
        return
    if users[pengirim]["balance"] < jumlah:
        print("Saldo tidak mencukupi untuk transfer.")
        return

    konfirmasi = input(f"Konfirmasi transfer Rp {jumlah:,} ke {penerima}? (y/n): ")
    if konfirmasi.lower() not in ["y", "yes"]:
        print("Transfer dibatalkan.")
        return

    users[pengirim]["balance"] -= jumlah
    users[penerima]["balance"] += jumlah

    waktu = time.strftime("%d-%m-%Y %H:%M")
    users[pengirim]["history"].append(
        {"time": waktu, "type": "Transfer Keluar", "amount": -jumlah, "to": penerima}
    )
    users[penerima]["history"].append(
        {"time": waktu, "type": "Transfer Masuk", "amount": jumlah, "from": pengirim}
    )

    print(f"\nTransfer berhasil!")
    print(f"Rp {jumlah:,} telah dikirim ke {penerima}")
    print(f"Saldo Anda sekarang Rp {users[pengirim]['balance']:,}")


# Program Utama (Menu Sederhana)
def main():
    print("=== SIMULASI *858# ===")
    nomor = input("Masukkan nomor HP Anda: ")

    if nomor not in users:
        print("Nomor tidak ditemukan dalam sistem.")
        return

    while True:
        print("\n=== MENU *858# ===")
        print("1. Cek Pulsa")
        print("2. Transfer Pulsa")
        print("0. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            cek_pulsa(nomor)
        elif pilih == "2":
            tujuan = input("Masukkan nomor tujuan: ")
            jumlah = int(input("Masukkan jumlah pulsa yang akan ditransfer: "))
            transfer_pulsa(nomor, tujuan, jumlah)
        elif pilih == "0":
            print("Terima kasih telah menggunakan layanan *858# Telkomsel.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()

