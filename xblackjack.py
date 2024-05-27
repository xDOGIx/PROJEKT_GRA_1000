import random    

def blackjack(self):
        while True:
            print("Witaj w blackjacku!")
            karty = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
            random.shuffle(karty)
            reka_gracza = []
            reka_krupiera = []

            def punkty(reka):
                suma = sum(reka)
                liczba_asow = reka.count(11)
                while suma > 21 and liczba_asow:
                    suma -= 10
                    liczba_asow -= 1
                return suma

            def pokaz_karty(reka, ukryta_karta=False, czy_krupier=False):
                if czy_krupier:
                    if ukryta_karta:
                        print("Karty krupiera:")
                        print("Karta 1: ***")
                        print("Karta 2:", reka[1])
                    else:
                        print("Karty krupiera:", reka)
                else:
                    print("Twoje karty:", reka)

            def obstaw():
                while True:
                    stawka = input("Ile chcesz obstawić? (całkowita liczba większa od 0): ")
                    if stawka.isdigit() and int(stawka) > 0:
                        stawka_kwota = int(stawka)
                        if stawka_kwota > self.stan_konta:
                            print("Nie masz wystarczającej ilości pieniędzy!")
                        else:
                            return stawka_kwota
                    else:
                        print("Niepoprawna kwota obstawienia! Podaj liczbę całkowitą większą od 0.")

            stawka_kwota = obstaw()
            self.stan_konta -= stawka_kwota

            def graj():
                for _ in range(2):
                    reka_gracza.append(karty.pop())
                    reka_krupiera.append(karty.pop())

                pokaz_karty(reka_gracza)
                pokaz_karty(reka_krupiera, ukryta_karta=True, czy_krupier=True)

                while punkty(reka_gracza) < 21:
                    wybor = input("Czy chcesz dobrać kartę? (t/n): ")
                    if wybor.lower() == 't':
                        reka_gracza.append(karty.pop())
                        pokaz_karty(reka_gracza)
                    else:
                        break

                punkty_gracza = punkty(reka_gracza)
                if punkty_gracza > 21:
                    print("Przekroczyłeś 21! Przegrywasz!")
                    return -1
                else:
                    while punkty(reka_krupiera) < 17:
                        reka_krupiera.append(karty.pop())

                    pokaz_karty(reka_krupiera, czy_krupier=True)
                    punkty_krupiera = punkty(reka_krupiera)

                    if punkty_krupiera > 21 or punkty_gracza > punkty_krupiera:
                        print("Wygrałeś!")
                        return 1
                    elif punkty_gracza < punkty_krupiera:
                        print("Przegrałeś!")
                        return -1
                    else:
                        print("Remis!")
                        return 0

            wynik = graj()
            if wynik == 1:
                self.stan_konta += 2 * stawka_kwota
            elif wynik == 0:
                self.stan_konta += stawka_kwota
            
            if not zapytaj_czy_zagrac_ponownie():
                break


def zapytaj_czy_zagrac_ponownie():
        while True:
            decyzja = input("Czy chcesz zagrać ponownie? (t/n): ").lower()
            if decyzja == 't':
                return True
            elif decyzja == 'n':
                return False
            else:
                print("Niepoprawny wybór, wpisz 't' dla tak lub 'n' dla nie.")



