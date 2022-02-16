from moduleKsiegowy import Ksiegowy
import sys

k = Ksiegowy()
if k.Wczytaj_z_pliku(sys.argv[1]) == True:
	for operacja in k.operacje:
		print(operacja.Info())
else:
	print("Niepoprawny plik wejściowy!!!")

