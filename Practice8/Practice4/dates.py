from datetime import datetime, timedelta, timezone
import pytz

# 1️⃣ Current date and time
now = datetime.now()
print("Now:", now)

# 2️⃣ Specific date
birthday = datetime(2005, 5, 15)
print("Birthday:", birthday)

# 3️⃣ Formatting dates
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))

# 4️⃣ Adding and subtracting time
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)

# 5️⃣ Time difference
difference = now - birthday
print("Days lived:", difference.days)

# 6️⃣ UTC time
utc_now = datetime.now(timezone.utc)
print("UTC time:", utc_now)

# 7️⃣ Different timezone
try:
    almaty_tz = pytz.timezone("Asia/Almaty")
    almaty_time = datetime.now(almaty_tz)
    print("Almaty time:", almaty_time)
except:
    print("pytz not installed, skipping timezone example")
#EXAMPLES FROM THE TASK4
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current date:", current_date)
print("5 days ago:", new_date)

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

now = datetime.now()
without_microseconds = now.replace(microsecond=0)
print("With microseconds:", now)
print("Without microseconds:", without_microseconds)
date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 2, 12, 0, 0)
difference = date2 - date1
print("Difference in seconds:", difference.total_seconds())