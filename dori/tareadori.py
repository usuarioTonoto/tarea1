import datetime as d

hora = d.datetime.now()
h = hora.hour
m = hora.minute
if (h >= 0 and m <= 59) and (h <= 11 and m <= 59):
    print("Buenos dias")
elif (h >= 12 and m <= 59) and (h <= 18 and m <= 59):
    print("Buenas tardes")
else:
    print("Wuenas noshes")
