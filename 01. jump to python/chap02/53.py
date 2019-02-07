a = "201901300915-0175440.002"
year = a[0:4]
month = a[4:6]
day = a[6:8]
time = a[8:10]
minute = a[10:12]
temp = a[12:15]
dust = a[15:17]
u_dust = a[17:19]
ozon = a[19:]

print("year="+year+"\n" + "month="+month+"\n" + "day="+day+"\n" 
     + "time="+time+"\n"+ "minute="+minute+"\n" + "temp="
     +temp+"\n" + "dust="+dust+"\n" + "u_dust="+u_dust+"\n" + "ozon="+ozon)
