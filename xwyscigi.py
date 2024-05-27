import random
import time

def wyścigi_psów(self):
        print("=========================================================================")
        print("Witaj na wyścigach psów!")
        psy = [
            {"nazwa": "Azor", "szybkość": random.randint(10, 20), "pozycja": 30},
            {"nazwa": "Burek", "szybkość": random.randint(10, 20), "pozycja": 30},
            {"nazwa": "Cezar", "szybkość": random.randint(10, 20), "pozycja": 30},
            {"nazwa": "Dingo", "szybkość": random.randint(10, 20), "pozycja": 30},
            {"nazwa": "Eros", "szybkość": random.randint(10, 20), "pozycja": 30}
        ]

        psy.sort(key=lambda x: x["szybkość"], reverse=True)
        print("Dzisiaj biorą udział w wyścigu psy:")
        for i, pies in enumerate(psy):
            print(f'{i+1}. "{pies["nazwa"]}"')

        wybor_psa = int(input("Wybierz numer psa, na który chcesz postawić: "))
        if wybor_psa < 1 or wybor_psa > len(psy):
            print("Niepoprawny numer psa!")
            return

        stawka_kwota = int(input("Ile chcesz postawić? "))
        if stawka_kwota > self.stan_konta:
            print("Nie masz wystarczającej ilości pieniędzy!")
            return

        print("Zwierzakom... Gotowi... Start!")
        for i in range(5):
            time.sleep(1)
            print(f"Wyścig trwa...")

        odleglosc = 30
        while odleglosc > 0:
            time.sleep(0.5)
            for pies in psy:
                ruch = random.randint(1, 3)
                pies["pozycja"] = max(0, pies["pozycja"] - ruch)
                print(f"{pies['nazwa']}: {'-' * pies['pozycja']}>")

            psy.sort(key=lambda x: x["pozycja"])
            prowadzenie = psy[0]["nazwa"]
            print(f"Prowadzi: {prowadzenie}")
            odleglosc = min(pies["pozycja"] for pies in psy)

        print("\nPrędkości psów po wyścigu:")
        for pies in psy:
            print(f"{pies['nazwa']}: Prędkość: {pies['szybkość']} km/h")

        psy_po_kolejnosci = [pies["nazwa"] for pies in psy]
        print(f"\nKolejność dobiegnięcia do mety: ")
        for miejsce, pies in enumerate(psy_po_kolejnosci):
            print(f"Miejsce {miejsce+1}: 🐕 {pies}")

        zwyciezca = psy[0]["nazwa"]
        print(f"\nZwycięzcą jest... {zwyciezca}!")

        if psy[wybor_psa - 1]["nazwa"] == zwyciezca:
            wygrana = stawka_kwota * 5
            print(f"Gratulacje! Twój pies {zwyciezca} wygrał! Wygrywasz ${wygrana}.")
            self.stan_konta += wygrana
        else:
            print("Niestety, Twój pies nie wygrał tego wyścigu.")
            self.stan_konta -= stawka_kwota

        print(f"Aktualny stan konta: ${self.stan_konta}")


def losowanie_liczb(self):
        return random.sample(range(1, 51), 5)


def obstaw_stawke(self):
        while True:
            stawka = input("Podaj stawkę loterii (całkowita liczba większa od 0): ")
            if stawka.isdigit() and int(stawka) > 0:
                return int(stawka)
            else:
                print("Niepoprawna stawka! Podaj liczbę całkowitą większą od 0.")


def sprawdz_wynik(self, wybrane_liczby, wylosowane_liczby, stawka_kwota):
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