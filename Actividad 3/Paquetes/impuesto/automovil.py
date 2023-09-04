
def clave1(nclave1):
    costo=float(input("Ingrese el costo del auto clave1:"))
    cu=(((nclave1/nclave1)*costo)*0.1)+costo
    costot_s=costo*nclave1
    costot_c=(costot_s*0.1)+costot_s
    print("Costo por cada auto con impuesto: "+str(cu))
    print("costo por lote de autos clave 1: " + str(costot_c))
    return costot_c

def clave2(nclave2):
    costo=float(input("Ingrese el costo del auto clave2:"))
    cu=(((nclave2/nclave2)*costo)*0.07)+costo
    costot_s=costo*nclave2
    costot_c=(costot_s*0.07)+costot_s
    print("Costo por cada auto con impuesto: "+str(cu))
    print("costo por lote de autos clave 2: " + str(costot_c))
    return costot_c

def clave3(nclave3):
    costo=float(input("Ingrese el costo del auto clave3:"))
    cu=(((nclave3/nclave3)*costo)*0.05)+costo
    costot_s=costo*nclave3
    costot_c=(costot_s*0.05)+costot_s
    print("Costo por cada auto con impuesto: "+str(cu))
    print("costo por lote de autos clave 3: " + str(costot_c))
    return costot_c