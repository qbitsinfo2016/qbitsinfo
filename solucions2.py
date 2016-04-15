precioSinIva = float (input ("Ingrese el precio sin iva: "))
#precioConIva = precioSinIva + precioSinIva * 0.21
IVA = precioSinIva * 0.21
precioConIva = precioSinIva + IVA
print "El precio con IVA incluido sera ", precioConIva