from moduleKsiegowy import Ksiegowy
import sys

k = Ksiegowy()
if k.Wczytaj_z_pliku(sys.argv[1]) == True:
	if k.Dopisz_zakup(sys.argv[2], int(sys.argv[3]), int(sys.argv[4])) == True:
		k.Zapisz_do_pliku(sys.argv[1])
	else:
		print("za mało środków")
else:
	print("Niepoprawny plik wejściowy!!!")
