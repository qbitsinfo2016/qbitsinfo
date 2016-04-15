Inversor1 = float (input("Ingrese la suma que invirtio el primer inversor: "))
Inversor2 = float (input("Ingrese la suma que invirtio el segundo inversor: "))
Inversor3 = float (input("Ingrese la suma que invirtio el tercer inversor: "))

totalInversion = Inversor1 + Inversor2 + Inversor3
print "EL total de la inversion es de: ", totalInversion," pesos"

porcInversor1 =  Inversor1 / totalInversion * 100
porcInversor2 = Inversor2 / totalInversion * 100
porcInversor3 = Inversor3 / totalInversion * 100
#Se puede redondear a 2 decimales con round directamente sobre la formula porcentual
#porcInversor1 = round( (Inversor1 / totalInversion * 100),2)
#porcInversor2 = round( (Inversor2 / totalInversion * 100),2)
#porcInversor3 = round( (Inversor3 / totalInversion * 100),2)

#Tambien se puede redondear creando otras variables que convertiran (ejemplo) esto "78.3487636453" en esto "78.34"
porcRedon1 = round(porcInversor1,2)
porcRedon2 = round(porcInversor2,2)
porcRedon3 = round(porcInversor3,0) 

print "El porcentaje que invirtio el primer inversor fue de ", porcRedon1,"%"
print "El porcentaje que invirtio el segundo inversor fue de ", porcRedon2,"%"
print "El porcentaje que invirtio el tercer inversor fue de ", porcRedon3,"%"