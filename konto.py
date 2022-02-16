from moduleKsiegowy import Ksiegowy
import sys

k = Ksiegowy()
if k.Wczytaj_z_pliku(sys.argv[1]) == True:
	print("Stan konta: ", k.Stan_konta())
else:
	print("Niepoprawny plik wejściowy!!!")
