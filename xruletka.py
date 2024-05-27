import random

KOLORKI = {
    "czerwony": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
    "czarny": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
}

def spin_ruletka():
        return random.randint(1,36)

def ruletka(self):
        while True:
            print("=========================================================================")
            print("Witaj w ruletce!")
            print("Twój stan konta: $", self.stan_konta)
            print("=========================================================================")
            print("Wybierz opcję:")
            print("1. Obstaw na liczbę (1-36)")
            print("2. Obstaw na kolor (Cze(r)wony/(C)zarny)")
            print("3. Wyjdź z gry")

            wybor_ruletka = input("Wybierz opcję: ")
            if wybor_ruletka == "1":
                obstaw_liczbe(self)
            elif wybor_ruletka == "2":
                obstaw_kolor(self)
            elif wybor_ruletka == "3":
                print("Dziękujemy za grę! Twój ostateczny stan konta: $", self.stan_konta)
                break
            else:
                print("Niepoprawny wybór, spróbuj ponownie.")


def obstaw_liczbe(self):
        while True:
            stawka = input("Postaw na jedną liczbę (1-36): ")
            if not stawka.isdigit() or int(stawka) < 1 or int(stawka) > 36:
                print("Niepoprawna liczba! Wybierz liczbę od 1 do 36.")
                continue
            try:
                stawka_kwota = int(input("Ile chcesz postawić? "))
                if stawka_kwota <= 0:
                    print("Kwota stawki musi być większa niż zero.")
                    continue
            except ValueError:
                print("Niepoprawna kwota stawki!")
                continue

            if stawka_kwota > self.stan_konta :
                print("Nie masz wystarczającej ilości pieniędzy!")
                return

            self.stan_konta -= stawka_kwota
            wynik = spin_ruletka()
            print("Kulka zatrzymała się na:", wynik)
            if int(stawka) == wynik:
                wygrana = stawka_kwota * 35
                self.stan_konta += wygrana
                print("Gratulacje! Wygrałeś $", wygrana)
            else:
                print("Niestety, przegrałeś $", stawka_kwota)
            print("Twój aktualny stan konta: $", self.stan_konta)
            break


def obstaw_kolor(self):
        while True:
            kolor = input("Wybierz kolor (Cze(r)wony/(C)zarny): ").lower()
            if kolor == 'r':
                kolor = 'czerwony'
            elif kolor == 'c':
                kolor = 'czarny'
            else:
                print("Niepoprawny kolor! Wybierz 'Cze(r)wony' lub '(C)zarny'.")
                continue
            try:
                stawka_kwota = int(input("Ile chcesz postawić? "))
                if stawka_kwota <= 0:
                    print("Kwota stawki musi być większa niż zero.")
                    continue
            except ValueError:
                print("Niepoprawna kwota stawki!")
                continue

            if stawka_kwota > self.stan_konta:
                print("Nie masz wystarczającej ilości pieniędzy!")
                return

            self.stan_konta -= stawka_kwota
            wynik = spin_ruletka()
            if wynik in KOLORKI[kolor]:
                print("Kulka zatrzymała się na:", wynik, kolor)
                wygrana = stawka_kwota * 2
                self.stan_konta += wygrana
                print("Gratulacje! Wygrałeś $", wygrana)
            else:
                print("Kulka zatrzymała się na:", wynik, "Czerwonym" if wynik in KOLORKI["czerwony"] else "Czarnym")
                print("Niestety, przegrałeś $", stawka_kwota)
            print("Twój aktualny stan konta: $", self.stan_konta)
            break