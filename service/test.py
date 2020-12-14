
s = "t3"
s1 = (s[1:])

t = "1,2"
t1 = t.split(",")

if s1 in t1:
    print(1111)
else:
    print(222)


time_str = "23:30"
import datetime
import time
date_p = datetime.datetime.now().date()
str_p = str(date_p)
print(str_p)
s_time = str_p + " " + time_str
print(s_time)
dateTime_p = datetime.datetime.strptime(s_time,'%Y-%m-%d %H:%M')
print(dateTime_p)
new = dateTime_p+datetime.timedelta(minutes=5)
print(new)
new_str = new.strftime("%Y-%m-%d %H:%M:%S")
ts = time.mktime(time.strptime(new_str,"%Y-%m-%d %H:%M:%S"))
print(ts)
n_ts=time.time()
print(n_ts)
if ts<n_ts:
    print("chidao")