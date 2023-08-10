'''--------------------------------------------------------Programa 1---------------------------------------------------------'''
'''La campaña de autobuses "La curva loca" requiere
determinar el costo que tendrá el boleto de un viaje sencillo, esto 
basado en los kilometros por recorrer y en el 
costo por kilometro'''

print("La curva loca")

kilometros=int(input("Ingrese los kilometros a recorrer:"))
costo=2.5*kilometros
print("El costo por kilometro es de $2.5.")
print("Costo total del boleto:"+ str(costo))

'''-----------------------------------------------Programa 2--------------------------------------------------------------------'''
'''Se requiere determinar el costo que tendrá realizar una llamada telefonica con base en el 
tiempo que dura la llamada y en el costo por minuto'''
print("Generador de tarifa telefonica.")
minutos=int(input("Ingrese los minutos de la llamada:"))
costo=0.1*minutos
print("El cobro es de "+ str(costo) + " por " + str(minutos)+" minutos")
'''-----------------------------------------------Programa 3--------------------------------------------------------------------'''
'''Realice un programa que determine el promedio que obtendra un alumno considerando que realizara tres examenes, 
de los cuales el primero y el segundo tiene una poderacion de 25%
mientras que el tercero tiene de 50%'''

print("Calculadora de promedios.")
primero=float(input("Ingrese  el puntaje obtenido en la primer evaluacion:"))
segundo=float(input("ingrese el puntaje obtenido en la segunda evaluacion:"))
tercero=float(input("Ingrese el puntaje obtenido en la tercera evaluación:"))
primero=primero*0.25
segundo=segundo*0.25
tercero=tercero*0.50


print("Porcentaje obtenido primera evaluación:"+str(primero))
print("Porcentaje obtenido segunda evaluación:"+str(segundo))
print("Porcentaje obtenido tercer evaluación:"+str(tercero))
print("Promedio final--->"+ str(primero+segundo+tercero))

'''----------------------------------------------------------Programa 4-----------------------------------------------------------'''
'''El dueño de un estacionamiento requiere un programa en Python que le permita determinar
 cuánto debe cobrar por el uso del estacionamiento asus clientes. Las tarifas que se tienen 
 son las siguientes:  Las dos primeras horas a $5.00 c/u. o Las siguientes tres a $4.00 c/u.
 o Las cinco siguientes a $3.00 c/u. o Después de diez horas el costo por cada una es de dos pesos. '''
print("Tarifa de cobro estacionamiento")
print("Tarifa de estacionamiento.")
print("Ingrese datos de entradaEntrada.")
hora_E=int(input("Hora:"))*60
minutos_E=int(input("Minutos:"))
print(" Salida.")
hora_S=int(input("Hora:"))*60
minutos_S=int(input("Minutos:"))
tiempo=((hora_S+minutos_S)-(hora_E+minutos_E))/60
if tiempo<=2:
   tarifa=tiempo*2;
   print("Tu tarifa es de:"+str(tarifa))
elif  tiempo>=3 and tiempo<=4:
   tarifa=tiempo*4
   print("Tu tarifa es de:"+str(tarifa))
elif tiempo>=5 and tiempo<10:
    tarifa=tiempo*3
    print("Tu tarifa es de:"+str(tarifa))
else:
   tarifa=tiempo*2
   print("Tu tarifa es de:"+str(tarifa)+" Pesos.")

'''------------------------------------------------------------Programa 5------------------------------------------------------------------------'''
#Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años.
# ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? 
print("Calculadora de salarios.")
salario=(1*12)
incremento=0.1
salario_b=0
for i in range(2):
    
    salario=salario*incremento+salario
    salario_b=salario_b+salario

    print("Salario año "+ str(i+1)+ "="+ str(salario))
print("Salario percibido en "+ str(i+1)+" años:"+ str(salario_b))