print ("Elija una opcion")
print ("1: Calcular el area de un triangulo")
print ("2: Calcular el area de un circulo")
x = int (input (" ")) 
if (x) == (1):
	print ("Ingrese primero la base del triangulo y luego la altura")
	BT= int (input (" "))
	AT= int (input (" "))
	Area= BT * AT
	print "El area del triangulo es: ", Area
elif (x) == (2):
	print "Ingrese el radio del circulo"
	RC= int (input (" "))
	Area= float(3.14 * (RC ** 2))
	print "El area del circulo es: ", Area
else:
	print "No ingreso una respuesta valida"