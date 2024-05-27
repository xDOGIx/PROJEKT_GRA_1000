import time
import random

def automaty(self):
        print("=========================================================================")
        print("Witaj w automatach do gier!")
        print("Zasady gry: Aby wygrać, potrzebujesz uzyskać trzy takie same symbole.")
        print("Dostępne symbole: 🍒  🍊  🍋  🍎  🍇  🍉")
        print("=========================================================================")

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

        print("=========================================================================")
        input("Naciśnij enter, aby kręcić automatem...")
        print("=========================================================================")

        symbole = []
        for _ in range(3):
            symbole.append(random.choice(["🍒", "🍊", "🍋", "🍎", "🍇", "🍉"]))
            print("Wypadły symbole:", symbole)
            time.sleep(1)  

        if symbole[0] == symbole[1] == symbole[2]:
            wygrana = stawka_kwota * 10  
            print("Brawo! Wygrałeś! Twój wygrany stan konta wynosi $", wygrana)
            self.stan_konta += wygrana

        else:
            print("Niestety, nie udało się wygrać.")
