presion = float (input("Ingrese la presion: "))
volumen = float (input("Ingrese el volumen: "))
temperautura = float (input("Ingrese la temperautura: "))
masa = (presion * volumen) / (0.37 * (temperautura + 460))
print "La masa sera ", masa