class Ksiegowy():
    def __init__(self):
        self.operacje = []      #opercje do wydruku/zapisu do nowego pliku
        self.towary = dict()    #operacje "magazyn" , stany towarów
        self.konto = 0          #operacje "konto", ile kasy jest na koncie
    def Wczytaj_z_pliku(self, nazwa_pliku):
        plik_poprawny = True
        plik = open(nazwa_pliku)
        kontynuuj = True
        while kontynuuj:
            argument = plik.readline().strip()
            if argument == "saldo":        #funkcja saldo
                saldo = Saldo()
                saldo.Wczytaj_z_pliku(plik)
                self.operacje.append(saldo)
                self.konto += saldo.kwota
            elif argument == "zakup":
                zakup = Zakup()
                zakup.Wczytaj_z_pliku(plik)
                if self.konto < zakup.Wartosc():
                    plik_poprawny = False
                    return plik_poprawny
                else:
                    self.operacje.append(zakup)
                    if zakup.identyfikator in self.towary:
                        self.towary[zakup.identyfikator] += zakup.ilosc
                    else:
                        self.towary[zakup.identyfikator] = zakup.ilosc
                    self.konto -= zakup.Wartosc()
            elif argument =="sprzedaż":
                sprzedaz = Sprzedaz()
                sprzedaz.Wczytaj_z_pliku(plik)
                if self.towary[sprzedaz.identyfikator] < sprzedaz.ilosc:
                    plik_poprawny = False
                    return plik_poprawny
                else:
                    self.operacje.append(sprzedaz)
                    self.towary[sprzedaz.identyfikator] -= sprzedaz.ilosc
                    self.konto += sprzedaz.Wartosc()
            elif argument == "stop":
                #operacje.append(argument)
                kontynuuj = False
            else:
                kontynuuj = False
        plik.close()
        return plik_poprawny
    def Zapisz_do_pliku(self, nazwa_pliku):
        plik = open(nazwa_pliku, "w")
        for operacja in self.operacje:
            operacja.Zapisz_do_pliku(plik)
        plik.write("stop")
        plik.close();
    def Dopisz_saldo(self, wartosc, komentarz):
        saldo = Saldo()
        saldo.kwota = wartosc
        saldo.komentarz = komentarz
        self.operacje.append(saldo)
        self.konto += saldo.kwota
    def Dopisz_sprzedaz(self, identyfikator, cena, ilosc):
        if identyfikator not in self.towary or self.towary[identyfikator] < ilosc:
            return False
        else:
            sprzedaz = Sprzedaz()
            sprzedaz.identyfikator = identyfikator
            sprzedaz.cena = cena
            sprzedaz.ilosc = ilosc
            self.operacje.append(sprzedaz)
            if identyfikator in self.towary:
                self.towary[identyfikator] -= ilosc
            else:
                self.towary[identyfikator] = ilosc
            self.konto += sprzedaz.Wartosc()
            return True
    def Dopisz_zakup(self, identyfikator, cena, ilosc):
        if cena * ilosc <= self.konto:
            zakup = Zakup()
            zakup.identyfikator = identyfikator
            zakup.cena = cena
            zakup.ilosc = ilosc

            self.operacje.append(zakup)
            if identyfikator in self.towary:
                self.towary[identyfikator] += ilosc
            else:
                self.towary[identyfikator] = ilosc
            self.konto -= zakup.Wartosc()
            return True
        else:
            return False
    def Stan_konta(self):
        return self.konto

class Sprzedaz:
    def __init__(self):
        self.identyfikator = None
        self.ilosc = 0
        self.cena = 0

    def Wczytaj_z_pliku(self, plik):
        self.identyfikator = str(plik.readline().strip())
        self.cena = int(plik.readline().strip())
        self.ilosc = int(plik.readline().strip())

    def Zapisz_do_pliku(self, plik):
        plik.write("sprzedaż\n")
        plik.write(self.identyfikator + "\n")
        plik.write(str(self.cena) + "\n")
        plik.write(str(self.ilosc) + "\n")

    def Wartosc(self):
        return self.cena * self.ilosc

    def Info(self):
        return "Sprzedaż " + self.identyfikator + " ilość:" + str(self.ilosc) + " cena:" + str(self.cena)

class Zakup:
    def __init__(self):
        self.identyfikator = None
        self.ilosc = 0
        self.cena = 0

    def Wczytaj_z_pliku(self, plik):
        self.identyfikator = str(plik.readline().strip())
        self.cena = int(plik.readline().strip())
        self.ilosc = int(plik.readline().strip())

    def Zapisz_do_pliku(self,plik):
        plik.write("zakup\n")
        plik.write(self.identyfikator + "\n")
        plik.write(str(self.cena) + "\n")
        plik.write(str(self.ilosc) + "\n")

    def Wartosc(self):
        return self.cena * self.ilosc

    def Info(self):
        return "Zakup " + self.identyfikator + " ilość:" + str(self.ilosc) + " cena:" + str(self.cena)
class Saldo:
    def __init__(self):
        self.kwota = 0
        self.komentarz = None

    def Wczytaj_z_pliku(self, plik):
        self.kwota = int(plik.readline().strip())
        self.komentarz = str(plik.readline().strip())

    def Zapisz_do_pliku(self, plik):
        plik.write("saldo\n")
        plik.write(str(self.kwota) + "\n")
        plik.write(self.komentarz + "\n")
    def Info(self):
        return "Saldo kwota:" + str(self.kwota) + " komentarz:" + self.komentarz