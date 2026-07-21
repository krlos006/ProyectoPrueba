#Hola Mundo en Python
print("¡Hola, desde Visual Studio Code!")
print("¡Estamos avanzando!")

#Calculo de edad
from datetime import datetime
hoy = datetime.now()
meses = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)
nombre_mes = meses[hoy.month - 1]
print("hoy es:", hoy.day, "de", nombre_mes, "de", hoy.year)
nombre = input("Ingrese su nombre: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
mes_nacimiento = int(input("Ingrese su mes de nacimiento (1-12): "))
dia_nacimiento = int(input("Ingrese su día de nacimiento (1-31): "))
año_actual = hoy.year
mes_actual = hoy.month
dia_actual = hoy.day
#Calculo años desde nacimiento hasta la fecha actual
edad = año_actual - año_nacimiento
#Valido si ya paso su mes/dia de nacimiento para restar un año si no ha pasado
if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    edad -= 1
#Muestro el resultado
print(f"La edad de {nombre} es: {edad} años")

if edad < 40:
    print(f"Felicidades {nombre} aun eres joven")
else:
    print(f"PFF TIENES {edad} años, Here lies your youth")