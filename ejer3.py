A = int (input ("Ingrese un numero: "))
B = int (input ("Ingrese un numero: "))
C = int (input ("Ingrese un numero: "))
if (A>B) and (B>C):
	print ("El mayor es ", A, "el del medio es ",B, "el menor es ", C) 
elif  (A>C) and (C>B):
	print ("El mayor es ", A, "el del medio es ",C, "el menor es ", B)
elif (B>A) and (A>C):
	print ("El mayor es ", B, "el del medio es ",A, "el menor es ", C) 
elif  (B>C) and (C>A):
	print ("El mayor es ", B, "el del medio es ",C, "el menor es ", A)
elif (C>A) and (A>B):
	print ("El mayor es ", C, "el del medio es ",A, "el menor es ", B) 
elif  (C>B) and (B>A):
	print ("El mayor es ", C, "el del medio es ",B, "el menor es ", A)
else: