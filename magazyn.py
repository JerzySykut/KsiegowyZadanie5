from moduleKsiegowy import Ksiegowy
import sys

k = Ksiegowy()
if k.Wczytaj_z_pliku(sys.argv[1]) == True:
    for i in range(2, len(sys.argv)):
        indentyfikator = sys.argv[i]
        print(indentyfikator + " stan: " + str(k.towary[indentyfikator]))
else:
	print("Niepoprawny plik wejściowy!!!")
