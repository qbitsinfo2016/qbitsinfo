var2 = float (input("ingrese el salario del empleado"))
print ("indique por si o por no si el empleado asistio todo el mes")
x = str (input(""))
print ("indique 1, 2 o 3 segun el rango horario que trabajo el empleado")
print ("1: entre 3 y 5 horas los domingos")
print ("2: entre 6 y 10 horas los domingos")
print ("3: entre 3 y 10 horas los domingos")
y = int (input (""))
if (x == "si") and (y ==1):
	var3 = var2 *0.03
	var2 = var2 + var3
	print ("el salario del empleado con su correspondiente adicional es de" , var2)
elif (x== "si") and (y==2):
	var3 = var2 *0.10
	var2=var2 + var3
	print ("el salario del empleado con su correspondiente adicional es de", var2)
elif (x == "no") and (y==3):
	var3 =var2 * 0.02
	var2 = var2 + var3
	print ( "el salario del empleado con su correspondiente adicional es de", var2)
else:
	print ("error los valores ingresados no son validos")
