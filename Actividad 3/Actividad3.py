from Paquetes.sueldo.Sueldo_Trabajador import *
from Paquetes.cubo.cubo import *
from Paquetes.tablaMultiplicar.tabla import*
from Paquetes.anual.porcentaje import*
from Paquetes.impuesto.automovil import*
'''---------------------------------------Actividad 1----------------------------------------------------------------------------------------------
Realice un programa que determine el sueldo semanal de N trabajadores considerando que se les descuenta 5% de su sueldo si ganan entre 0 y 150
pesos. Se les descuenta  7% si ganan más de 150 pero menos de 300, y 9% si ganan más de 300 pero menos de 450. Los datos son horas trabajadas,
sueldo por hora y nombre de cada trabajador.---------------------------------------------------------------------------------------------------- '''
'''print("Calculadora de sueldos:")
numero_t=int(input("Ingrese el numero de salarios a calcular:"))
for i in range(numero_t):
    nombre=input("Ingrese nombre del trabajador:")
    horas_t=float(input("Ingrese horas trabajadas:"))
    sueldo_hora=float(input("Sueldo por hora:"))
    sueldo_SinD=horas_t*sueldo_hora
    print("Nombre trabajador "+ str(i+1)+":"+str(nombre))
    if sueldo_hora<150:
       sueldo_u(sueldo_SinD)
    elif sueldo_hora>=150 and sueldo_hora<300:
       sueldo_d(sueldo_SinD)
    elif sueldo_hora>=300 and sueldo_hora<450:
       sueldo_t(sueldo_SinD)
    else:
        print("Sueldo incorrecto.")'''
        
        
    


'''---------------------------------------Actividad 2----------------------------------------------------------------------------------------------
Realice un programa, dado un grupo de números naturales positivos, calcule e imprima el cubo de estos números.------------------------------------- '''
'''numero=int(input("Ingrese un numero natural positivo :"))

if numero>0:
    cubo(numero)
else:
    print("Su numero es negativo")'''
     


'''---------------------------------------Actividad 3----------------------------------------------------------------------------------------------
Realice un programa para obtener la tabla de multiplicar de un entero X y genere los múltiplos comenzando desde el 1 hasta el 10.------------------ '''
'''print("TABLAD DE MULTIPLICAR.")
numero=int(input("Ingrese un numero:"))
multiplica(numero)'''



'''---------------------------------------Actividad 4----------------------------------------------------------------------------------------------
En 1961, una persona vendió las tierras de su abuelo al gobierno por la cantidad de $1500. Suponga que esta persona ha colocado 
el dinero en una cuenta de ahorros que paga 15% anual. ¿Cuánto vale ahora su inversión? P(1+i)n.------------------------------------------------ '''

'''print("CUENTA DE AHORROS.")
año_v=1961
año_a=int(input("Ingrese año actual:"))
años(año_v,año_a)'''




'''---------------------------------------Actividad 5----------------------------------------------------------------------------------------------
El gerente de una compañía automotriz desea determinar el impuesto que va a pagar por cada uno de los automóviles que posee, además del total 
que va a pagar por cada categoría y por todos los vehículos, basándose en la siguiente clasificación: * Los vehículos con clave 1 pagan 10% de
 su valor. * Los vehículos con clave 2 pagan 7% de su valor. * Los vehículos con clave 3 pagan 5% de su valor. ---------------------------------'''
print("Compañia automotriz.")

nClave1=int(input("Ingrese el numero de autos con clave 1:"))
nClave2=int(input("Ingrese el numero de autos con clave 2:"))
nClave3=int(input("Ingrese el numero de autos con clave 3:"))
print("---------------------------------------AUTOMOVIL CLAVE 1-----------------------------------------------------------------------")
clave1t=clave1(nClave1)
print("---------------------------------------AUTOMOVIL CLAVE 1-----------------------------------------------------------------------")
clave2t=clave2(nClave2)
print("---------------------------------------AUTOMOVIL CLAVE 1-----------------------------------------------------------------------")
clave3t=clave3(nClave3)
print("---------------------------------------COSTO TOTAL----------------------------------------------------------1-------------------")
totalfin=clave1t+clave2t+clave3t
print("El total final es:"+str(totalfin))
