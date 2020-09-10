#Definición del tipo registro Empleado

class Empleado:
    pass


e1 = Empleado()
e1.legajo = 1
e1.nombre = "Stefania"
e1.sueldo = 250

print("El empleado es:",e1.legajo,"-",e1.nombre,"-",e1.sueldo)

e2 = Empleado()
e2.legajo = 2
e2.nombre = "Juan"
e2.sueldo = 350

print("El empleado es:",e2.legajo,"-",e2.nombre,"-",e2.sueldo)

#ejemplo de copia
a = 2
b = 3
print("valore de a y b simples:",a,b)
b = a
print("valore de a y b simples:",a,b)

#copia de registros
e1 = e2
print("El empleado es:",e1.legajo,"-",e1.nombre,"-",e1.sueldo)
print("El empleado es:",e2.legajo,"-",e2.nombre,"-",e2.sueldo)
e1.sueldo = 400
print("El empleado es:",e1.legajo,"-",e1.nombre,"-",e1.sueldo)
print("El empleado es:",e2.legajo,"-",e2.nombre,"-",e2.sueldo)