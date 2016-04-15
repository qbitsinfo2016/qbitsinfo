# -*- coding: utf-8 -*- 
"""El sistema de Facturación Electrónica impulsado por AFIP para Consumidor Final, 
obtiene el importe neto a pagar de la diferencia entre el importe total y los impuestos aplicados. 
Tener en cuenta las siguientes consideraciones: 1-Si el importe neto es 0 se debe informar un error
 2-Los impuestos no deben superar al importe total 3-Si el importe neto es >0, 
 y el importe total supera los $5000 se debe informar  “Monto  Superado  para  Consumidor  Final”.  
 Elabore  el  programa  correspondiente  que informe el importe neto y los mensajes que correspondan""" 


ImporTotal = float (input ("Ingrese el importe total "))
Impuesto = float (input ("Ingrese el impuesto "))
ImporNeto = float (ImporTotal - Impuesto)
if (ImporNeto == 0):
	print	"Error el importe neto no puede ser igual a cero"
if Impuesto > ImporTotal:
 	print "Erro no se puede calcular, el impuesto supera al importe total"
if ImporNeto > 0: 
	if ImporTotal > 5000:
 		print "Monto Superado para Consumidor Final"
print "El importe neto es $", ImporNeto