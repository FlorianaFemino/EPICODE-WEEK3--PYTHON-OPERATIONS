import math


scelta = input ("Benvenuto! Quale perimetro vuoi calcolare?\n\n1. Quadrato\n2. Circonferenza\n3. Rettangolo\n\n")


if scelta == '1':

	lato = int (input ("\nInserisci la lunghezza del lato: "))
	print ("\nIl perimetro è", lato * 4)
	
elif scelta == '2':

	raggio = int (input ("\nInserisci la misura del raggio: "))
	circonferenza = raggio * math.pi * 2 
	print ("\nLa circonferenza è",circonferenza)

elif scelta == '3':

	base = int (input ("\nInserisci la base: "))
	altezza = int (input ("Inserisci l'altezza: "))
	
	print ("\nIl perimetro è", base * altezza)