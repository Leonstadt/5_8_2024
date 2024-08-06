calificaciones=4
lista_calificacion=[]
for i in range(calificaciones):
    calificacion=int(input(f"Ingrese la calificacion # {i+1}: "))
    lista_calificacion.append(calificacion)
#print(lista_calificacion)
suma=sum(lista_calificacion)    
media=suma/calificaciones
print (f"La media es {media}")
if media >=90:
    print(f"La puntuacion es A")
elif media>=80:
    print(f"La puntuacion es B")
elif media>=70:
    print(f"La puntuacion es C")
elif media>=60:
    print(f"La puntuacion es D")
else:
    print("La puntuacion es E")    
