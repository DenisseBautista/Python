 
print("Programa de evaluacion de notas de alumno")
 #FUNCION A LA CUAL SE LE LLAMARA EVALUACIÓN
nota_alumno=input("Introduce la nota del alumno:")


def evaluacion(nota): 
 	
 	  valoracion="aprobado"
 	  if nota<5:
 	  	  valoracion="Suspenso"
 	  return valoracion
#print(evaluacion(4))
#llamda a la función
print(evaluacion(int(nota_alumno)))
#Programa desde nota introducida por teclado.


