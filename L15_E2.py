import time
current_time = time.time()
print(current_time)
readable_time = time.ctime(current_time)
print(int(readable_time[11:13]))
if int(readable_time[11:13])<=12:
    print ("GM")
elif int(readable_time[11:13])<=17:
    print("GA")
else:
    print("GE")