import random

def utworz_karte(kolor, wartosc):
        return {"kolor": kolor, "wartosc": wartosc}

def utworz_talie():
    talia = []
    kolory = ['♥', '♦', '♣', '♠']
    wartosci = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for kolor in kolory:
        for wartosc in wartosci:
            talia.append(utworz_karte(kolor, wartosc))
    return talia

def tasuj_talie(talia):
    random.shuffle(talia)

def rozdaj_karte(talia):
    return talia.pop()

def dobierz_karte(self, talia):
            karta = rozdaj_karte(talia)
            self.reka.append(karta)




def dobierz_poczatkowe_karty(self, talia):
            dobierz_karte(self, talia)
            dobierz_karte(self, talia)


def dobierz_ostatnia_karte(self, talia):
            print("Dobieranie ostatniej karty...")
            dobierz_karte(self,talia)
            dobierz_karte(self,talia)
            dobierz_karte(self,talia)


def obstawanie(gracz, stawka):
    while True:
        print(f"Twój aktualny stan konta: {gracz.stan_konta}")
        print(f"Stawka na stole: {gracz.stawka}")
        print("Czy chcesz zagrać za stawkę? (tak/nie)")
        odpowiedz = input().lower()
        if odpowiedz == 't' or odpowiedz == 'tak':
            try:
                if gracz.sprawdz_stawke():
                    gracz.przegrana(gracz.stawka)
                    return True
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            except ValueError:
                print("Podana wartość musi być liczbą całkowitą.")
        elif odpowiedz == 'n' or odpowiedz == 'nie':
            return False
        else:
            print("Nieprawidłowa odpowiedź. Proszę odpowiedzieć 'tak' lub 'nie'.")


def sprawdz_reke(gracz):
    karty = sorted(gracz.reka, key=lambda x: x["wartosc"], reverse=True)
    wartosci_kart = [karta["wartosc"] for karta in karty]

    if len(set([karta["kolor"] for karta in karty])) == 1:
        return "Kolor"

    wartosci = [wartosci_kart[karty.index(karta)] for karta in karty]
    if len(set(wartosci)) == 5 and (max(wartosci) - min(wartosci) == 4):
        return "Strit"

    for wartosc in wartosci_kart:
        if wartosci_kart.count(wartosc) == 4:
            return "Kareta"
        if wartosci_kart.count(wartosc) == 3:
            if "Para" in [wartosci_kart.count(w) for w in wartosci_kart]:
                return "Full"
            else:
                return "Trójka"
        if wartosci_kart.count(wartosc) == 2:
            if "Para" in [wartosci_kart.count(w) for w in wartosci_kart]:
                return "Dwie Pary"
            else:
                return "Para"

    return "Nic"


def nowa_runda(gracz, talia, stawka, wyniki):
    dobierz_poczatkowe_karty(gracz,talia)
    gracz.wyswietl_reke()
    gracz.stawka = stawka  
    obstawienie = obstawanie(gracz, stawka)
    if obstawienie:
        podbicie = czy_podbic_stawke(gracz, stawka)
        if podbicie:
            dobierz_ostatnia_karte(gracz,talia)
            gracz.wyswietl_reke()
            if obstawanie(gracz, stawka):
                dobierz_ostatnia_karte(gracz,talia)
                gracz.wyswietl_reke()
                wynik = sprawdz_reke(gracz)
                wyswietl_wynik(wynik)
                if wynik != "Nic":
                    wygrana_kwota = stawka * wyniki[wynik]
                    gracz.wygrana(wygrana_kwota)
                    print(f"Wygrałeś! Zdobywasz {wygrana_kwota} żetonów!")
                else:
                    print("Przegrałeś!")
        else:
            print("Nie chcesz podbić stawki.")
            if obstawanie(gracz, stawka):
                dobierz_ostatnia_karte(gracz,talia)
                gracz.wyswietl_reke()
                wynik = sprawdz_reke(gracz)
                wyswietl_wynik(wynik)
                if wynik != "Nic":
                    wygrana_kwota = stawka * wyniki[wynik]
                    gracz.wygrana(wygrana_kwota)
                    print(f"Wygrałeś! Zdobywasz {wygrana_kwota} żetonów!")
                else:
                    print("Przegrałeś!")
    else:
        print("Nie chcesz postawić stawki.")
        if obstawanie(gracz, stawka):
            dobierz_ostatnia_karte(gracz,talia)
            gracz.wyswietl_reke()
            wynik = sprawdz_reke(gracz)
            wyswietl_wynik(wynik)
            if wynik != "Nic":
                wygrana_kwota = stawka


def czy_podbic_stawke(gracz, stawka, min_podbij_stawke=2, max_podbij_stawke=5):
    while True:
        print("Czy chcesz podbić stawkę? (tak/nie)")
        odpowiedz = input().lower()
        if odpowiedz == 'tak':
            print("Podaj kwotę do podbicia:")
            try:
                podbicie = int(input())
                if podbicie >= min_podbij_stawke and podbicie <= max_podbij_stawke:
                    if podbicie <= gracz.stan_konta:
                        gracz.przegrana(podbicie)
                        gracz.stawka += podbicie  
                        print(f"Stawka została podbita o {podbicie}. Nowa stawka: {gracz.stawka}")
                        return True
                    else:
                        print("Nie masz wystarczająco pieniędzy.")
                else:
                    print(f"Podbicie musi być pomiędzy {min_podbij_stawke} a {max_podbij_stawke}.")
            except ValueError:
                print("Podana wartość musi być liczbą całkowitą.")
        elif odpowiedz == 'nie':
            return False
        else:
            print("Nieprawidłowa odpowiedź. Proszę odpowiedzieć 'tak' lub 'nie'.")


def wyswietl_wynik(wynik):
    print("Twój układ to:", wynik)


def gra_poker(gracz):
 
    talia = utworz_talie()
    tasuj_talie(talia)

    stawka = 50
    wyniki = {"Nic": 0, "Para": 1, "Dwie Pary": 2, "Trójka": 3, "Strit": 5, "Kolor": 8, "Full": 10, "Kareta": 20}

    print("Witaj w grze Poker!")
    while True:
        gracz.reka = []
        nowa_runda(gracz, talia, stawka, wyniki)
        gracz.wyswietl_stan_konta()
        if gracz.stan_konta <= 0:
            print("Nie masz już pieniędzy! Koniec gry!")
            break
        print("Czy chcesz zagrać jeszcze raz? (tak/nie)")
        odpowiedz = input().lower()
        if odpowiedz != 'tak':
            print("Dziękujemy za grę!")
            break