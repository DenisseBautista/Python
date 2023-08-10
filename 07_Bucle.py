#La variable email guarda el valor de email
email=input("Introduce tu email, por favor:")
for i in email:
    #I RECORRE EMAIL
    if i=="@":
        #Si i es == @ ENTONCES es verdader
        arroba=True

        break;#rompe el ciclo 
else:#Recorre todo el arreglo y manda a arroba con valor a false
    arroba=False
print(arroba)#imprime el valor de @