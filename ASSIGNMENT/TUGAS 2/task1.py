import datetime

# Dapatkan tanggal saat ini
tanggal_sekarang = datetime.date.today()

# Jumlah hari yang akan ditambahkan ke tanggal saat ini
jumlah_hari = 5

# Hitung tanggal
tanggal_baru = tanggal_sekarang + datetime.timedelta(days=jumlah_hari)

formatted_date = tanggal_baru.strftime("%A, %d %B %Y")

# Cetak tanggal yang telah diformat
print(formatted_date)