import datetime
HoraActual=datetime.datetime.now().time()
if HoraActual.hour >= 12:
    print("Buenas Tardes")
else:
    print("Buenos Dias")