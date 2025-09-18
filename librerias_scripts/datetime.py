from datetime import datetime, timedelta
# Fecha y hora actual
ahora = datetime.now()
print(ahora) # 2023-10-25 15:30:45.123456
# Operaciones con fechas
mañana = ahora + timedelta(days=1)
print(mañana)
# Formateo de fechas
print(ahora.strftime("%d/%m/%Y %H:%M"))