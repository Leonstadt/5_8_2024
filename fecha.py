meses={"enero":1, "febrero":2, "marzo":3,  
"abril":4, "mayo":5, "junio":6,
 "julio":7, "agosto":8, "septiembre":9,
 "octubre":10, "noviembre": 11, "diciembre":12 }
fecha=input("Introduce una fecha: ")
formato1=fecha.replace(",", "")
formato2=formato1.split(" ")
print(formato2)
dia=int(formato2[0])
mes=(formato2[1]).lower()
año=int(formato2[2])
numeromes=meses[mes]
print(f"{dia} {numeromes} {año}")

