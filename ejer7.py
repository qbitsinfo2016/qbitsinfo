anio = int(input("Ingrese el anio que desea consultar: "))
if (anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0):  
 print ("El anio ", anio, " Si es bisiesto ")  
else:  
 print "El anio ", anio ," No es bisiesto "  