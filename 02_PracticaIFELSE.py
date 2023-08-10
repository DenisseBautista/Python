print("Verificación de acceso:")
nota_alumno=int(input("Introduce tu nota:"))
if nota_alumno<5:
	print("¡No aprobo.!")
elif nota_alumno<6:
	print("Aprobado")
elif nota_alumno<7:
    print("Bien")
elif nota_alumno<9:
    print("Excelente")
else:
    print("Sobresaliente")