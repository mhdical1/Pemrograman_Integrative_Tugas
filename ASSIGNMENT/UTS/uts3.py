#Muhammad Faisal Hamzah 211402132
# Mengambil Angka Hari ke (Int)
import datetime

num_days = int(input("Masukkan Angka (hari ke-): "))

# Menentukan tanggal 

date_now = datetime.datetime.now()
date_later = date_now + datetime.timedelta(days=num_days)

# Mencetak tanggal dalam format yang diinginkan

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("{} on {} {} ".format(weekdays[date_later.weekday()], date_later.day, date_later.strftime("%B %Y")))
