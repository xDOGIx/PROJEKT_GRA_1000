import time
import random


def loteria(self):
        print("Witaj w loterii!")
        print("Zasady gry: Wybierz od 1 do 10 liczb od 1 do 50.")
        print("Jeśli trafisz wszystkie wybrane liczby, wygrywasz główną nagrodę!")
        print("Masz także szansę na mniejsze nagrody za trafienie części liczb.")
        print("=========================================================================")

        ilosc_liczb = int(input("Wybierz ilość liczb do obstawienia (od 1 do 10): "))
        if ilosc_liczb < 1 or ilosc_liczb > 10:
            print("Niepoprawna ilość liczb!")
            return

        wybrane_liczby = []
        for i in range(ilosc_liczb):
            while True:
                liczba = input(f"Wybierz liczbę {i + 1}: ")
                if liczba.isdigit() and 1 <= int(liczba) <= 50:
                    if int(liczba) not in wybrane_liczby:
                        wybrane_liczby.append(int(liczba))
                        break
                    else:
                        print("Ta liczba została już wybrana. Wybierz inną.")
                else:
                    print("Niepoprawna liczba! Wybierz liczbę od 1 do 50.")

        print("Twoje wybrane liczby:", wybrane_liczby)
        stawka_kwota = obstaw_stawke()
        print(f"Obstawiona stawka: ${stawka_kwota}")
        print("Losowanie liczby...")
        time.sleep(2)
        wylosowane_liczby = losowanie_liczb()
        print("Wylosowane liczby to:", wylosowane_liczby)
        wynik = sprawdz_wynik(wybrane_liczby, wylosowane_liczby, stawka_kwota)
        print(wynik)

        if "Niestety" in wynik:
            self.stan_konta -= stawka_kwota

def obstaw_stawke():
        while True:
            stawka = input("Podaj stawkę loterii (całkowita liczba większa od 0): ")
            if stawka.isdigit() and int(stawka) > 0:
                return int(stawka)
            else:
                print("Niepoprawna stawka! Podaj liczbę całkowitą większą od 0.")

def losowanie_liczb():
        return random.sample(range(1, 51), 5)

def sprawdz_wynik(wybrane_liczby, wylosowane_liczby, stawka_kwota):
        trafione_liczby = set(wybrane_liczby) & set(wylosowane_liczby)
        ilosc_trafien = len(trafione_liczby)
        nagroda = 0
        if ilosc_trafien == 5:
            nagroda = stawka_kwota * 1000  
            return f"Jackpot! Wygrałeś główną nagrodę w wysokości ${nagroda}!"
        elif ilosc_trafien == 4:
            nagroda = stawka_kwota * 100  
            return f"Gratulacje! Wygrałeś nagrodę za trafienie 4 liczb w wysokości ${nagroda}!"
        elif ilosc_trafien == 3:
            nagroda = stawka_kwota * 10  
            return f"Świetnie! Wygrałeś nagrodę za trafienie 3 liczb w wysokości ${nagroda}!"
        elif ilosc_trafien == 2:
            nagroda = stawka_kwota * 5  
            return f"Dobra robota! Wygrałeś nagrodę za trafienie 2 liczb w wysokości ${nagroda}!"
        elif ilosc_trafien == 1:
            nagroda = stawka_kwota * 2  
            return f"Masz szczęście! Wygrałeś nagrodę za trafienie 1 liczby w wysokości ${nagroda}!"
        else:
            return "Niestety, nie udało ci się wygrać. Spróbuj ponownie!"