from moduleKsiegowy import Ksiegowy
import sys

k = Ksiegowy()
if k.Wczytaj_z_pliku(sys.argv[1]) == True:
	k.Dopisz_saldo(int(sys.argv[2]), sys.argv[3])
	k.Zapisz_do_pliku(sys.argv[1])
else:
	print("Niepoprawny plik wej�ciowy!!!")
