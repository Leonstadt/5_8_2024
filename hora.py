veinticuatro=input("Ingrese la hora en formato de 24 horas (HH:MM) ")    
partes=veinticuatro.split(":")
horas=int(partes[0])
minutos=int(partes[1])
doce="AM"
if horas >=12:
    doce="PM"
if horas >12:
    horas-=12
elif horas==12:
    horas =12
print(f"La hora en formato de 12 horas es {horas} : {minutos:02d}  {doce}")

