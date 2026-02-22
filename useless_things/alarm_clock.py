import datetime
import time

# 10:10:10
# 01234567
alarm_time = input("Enter alarm time (HH:MM:SS): ").strip()

if len(alarm_time) != 8 or \
    not alarm_time.replace(":", "").isdigit() or \
    alarm_time[2]+alarm_time[5] != "::":
    print("Invalid format!")
    exit()

while str(datetime.datetime.now().time().replace(microsecond=0)) != alarm_time:
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)
else:
    print("WAKE UP!")