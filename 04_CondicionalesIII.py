print("Asignaturas optativas año 2023")
print("Asignaturas optativas: Informatica gráfica - Pruebas de Software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura elegida: ")
asignatura=opcion.lower()

if asignatura in ("informatica graficá", "pruebas de software", "usabilidad y accesibilidad"):
   print("asignatura elegida "+ asignatura)
   #En la linea 5 no es necesario pasar la variable a 
   ##tipo string ya que la variable ya es de tipo string
else:
	print("La asignatura elegida no esta contemplada.")
