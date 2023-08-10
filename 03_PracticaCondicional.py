salario_presidente=int(input("Introduce el salario presidente:"))
print("Salario presidente:"+ str(salario_presidente))

salario_director=int(input("Introduce el salario director:"))
print("Salario presidente:"+ str(salario_director))

salario_jefe_area=int(input("Introduce el salario jefe de area:"))
print("Salario presidente:"+ str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario administrativo:"))
print("Salario presidente:"+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")

else: 
	print("Algo no funciona en esta empresa")