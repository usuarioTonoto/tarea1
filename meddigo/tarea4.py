from datetime import time, datetime
hora_local=datetime.now()
hora_local=[hora_local.hour,hora_local.minute,hora_local.second]
print(hora_local)
if hora_local[0]>12:
    print("buenas tardes")
else:
    print("Buenos dias")

