from os import system
system("cls")

A=80000
B=75000
C=70000
D=10000
E=8500
F=7000

print("""INTERVIAJES

Oferta de destinos turísticos:
Opción A: Viaje a París: $80000
Opción B: Viaje a Roma: $75000
Opción C: Viaje a Lisboa: $70000

Oferta de excursiones:
Opción D: Tour por Berlín: $10000
Opción E: Tour por Madrid: $8500
Opción F: Tour por Ámsterdam: $7000""")
print("""""")

print()

destino=input("SELECCIONE SU DESTINO TURÍSTICO, ESCRIBIENDO UNA LETRA (A-C). PARA NO SELECCIONAR DESTINO TÚRÍSTICO, SOLAMENTE PRESIONE ESPACIO. LUEGO, PRESIONE ENTER: ")

print()

if destino!="A" and destino!= "B" and destino!= "C" and destino!= " ":
	print("USTED SELECCIONÓ MAL LA OPCIÓN. PRESIONE ENTER PARA SALIR")
	input()
	from os import system
	system("cls")
	exit()

print()

tour=input("SELECCIONE LA EXCURSIÓN QUE DESEA, ESCRIBIENDO UNA LETRA (D-F). PARA NO SELECCIONAR EXCURSIÓN, SOLAMENTE PRESIONE ESPACIO. LUEGO, PRESIONE ENTER: ")

if tour!="D" and tour!= "E" and tour!= "F" and tour!= " ":
	print("USTED SELECCIONÓ MAL LA OPCIÓN. PRESIONE ENTER PARA SALIR")
	input()
	from os import system
	system("cls")
	exit()

print()

print("""""")
print("Sus elecciones fueron:")
if destino=="A":
	print("Destino: París")
	preciodestino=A
elif destino=="B":
	print("Destino: Roma")
	preciodestino=B
elif destino=="C":
	print("Destino: Lisboa")
	preciodestino=C
elif destino==" ":
	print("No eligió destino")
	preciodestino=0

if tour=="D":
	print("Excursión: Berlín")
	preciotour=D
elif tour=="E":
	print("Excursión: Madrid")
	preciotour=E
elif tour=="F":
	print("Excursión: Ámsterdam")
	preciotour=F
elif tour==" ":
	print("No eligió excursión")
	preciotour=0

preciototal=preciodestino+preciotour

print("""""")

print()

if preciototal>0:
	print("El precio total es: $",preciototal)
	print("""""")
	print("""GRACIAS POR SU COMPRA EN INTERVIAJES. DISFRUTE SU PASEO. PRESIONE ENTER PARA SALIR""")
elif preciototal==0:
	print("""GRACIAS POR VISITAR LA PÁGINA DE INTERVIAJES. PRESIONE ENTER PARA SALIR""")
input()
from os import system
system("cls")
