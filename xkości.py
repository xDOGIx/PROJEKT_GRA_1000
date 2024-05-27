import random

def kosci(self):
        print("=========================================================================")
        print("Witaj w grze w kości (Craps)!")
        print("Zasady gry: Gracz stawia zakłady na wynik rzutu dwiema kostkami.")
        print("Jeśli wyrzucisz sumę 7 lub 11 w pierwszym rzucie, wygrywasz.")
        print("Jeśli wyrzucisz sumę 2, 3 lub 12 w pierwszym rzucie, przegrywasz.")
        print("Jeśli wyrzucisz inną sumę, ta suma staje się twoim 'punktem', a teraz musisz wyrzucić tę samą sumę ponownie, zanim wyrzucisz sumę 7, aby wygrać.")
        print("=========================================================================")

        def rzut_kosci():
            return random.randint(1, 6) + random.randint(1, 6)

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

        print("Naciśnij enter, aby rzucić kością...")
        input()

        pierwszy_rzut = rzut_kosci()
        print("Pierwszy rzut:", pierwszy_rzut)

        if pierwszy_rzut in (7, 11):
            wygrana = stawka_kwota * 2 
            print("Gratulacje, wygrałeś w pierwszym rzucie! Twoja wygrana wynosi $", wygrana)
            self.stan_konta += wygrana
        elif pierwszy_rzut in (2, 3, 12):
            print("Niestety, przegrałeś w pierwszym rzucie!")
        else:
            punkt = pierwszy_rzut
            print("Twój punkt to:", punkt)
            print("Teraz spróbuj wyrzucić swoją sumę punktów ponownie, zanim wyrzucisz sumę 7.")

            while True:
                print("Naciśnij enter, aby rzucić kością...")
                input()
                kolejny_rzut = rzut_kosci()
                print("Kolejny rzut:", kolejny_rzut)
                if kolejny_rzut == punkt:
                    wygrana = stawka_kwota * 2  
                    print("Gratulacje, udało ci się wyrzucić swoją sumę punktów ponownie! Wygrywasz!")
                    print("Twoja wygrana wynosi $", wygrana)
                    self.stan_konta += wygrana
                    break
                elif kolejny_rzut == 7:
                    print("Niestety, wyrzuciłeś sumę 7, co oznacza, że przegrywasz.")
                    break