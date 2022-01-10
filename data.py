import csv, datetime

dt = datetime.datetime.today()
month = dt.month
day = dt.day
year = dt.year
#print (type(month))

if month == 1:
    filename = "January.csv"
elif month == 2:
    filename = "February.csv"
elif month == 3:
    filename = "March.csv"
elif month == 4:
    filename = "April.csv"
elif month == 5:
    filename = "May.csv"
elif month == 6:
    filename = "June.csv"
elif month == 7:
    filename = "July.csv"
elif month == 8:
    filename = "August.csv"
elif month == 9:
    filename = "September.csv"
elif month == 10:
    filename = "October.csv"
elif month == 11:
    filename = "November.csv"
elif month == 12:
    filename = "December.csv"
else: 
    print("Month Value Error!")

with open(filename, newline='') as f:
    reader = csv.reader(f)
    csv_list = list(reader)
#print(csv_list)

prayer_list = csv_list[:]
prayer_list.pop(0)
#print(prayer_list)

if str(day) in (x[0] for x in prayer_list):
    today_times = prayer_list[day - 1]
#print(type(today_times))

fajr_adhan = today_times[1]
fajr_iqamah = today_times[2]
sunrise = today_times[3]
dhuhr_adhan = today_times[4]
dhuhr_iqamah = today_times[5]
asr_adhan = today_times[6]
asr_iqamah = today_times[7]
maghrib_adhan = today_times[8]
maghrib_iqamah = today_times[9]
isha_adhan = today_times[10]
isha_iqamah = today_times[11]

print("Fajr Adhan:", fajr_adhan)
print("Fajr Iqamah:", fajr_iqamah)
print("Sunrise:", sunrise)
print("Dhuhr Adhan:", dhuhr_adhan)
print("Dhuhr Iqamah:", dhuhr_iqamah)
print("Asr Adhan:", asr_adhan)
print("Asr Iqamah:", asr_iqamah)
print("Maghrib Adhan:", maghrib_adhan)
print("Maghrib Iqamah:", maghrib_iqamah)
print("Isha Adhan:", isha_adhan)
print("Isha Iqamah:", isha_iqamah)