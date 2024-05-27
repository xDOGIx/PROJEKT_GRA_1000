

def splata_kredytu(self):
        if self.zadluzenie > 0:
            odsetki = int(self.zadluzenie * 0.30)  
            print("Do spłaty kredytu z odsetkami: $", self.zadluzenie + odsetki)
            while True:
                czy_splata = input("Czy chcesz spłacić cały kredyt wraz z odsetkami? (t/n): ")
                if czy_splata.lower() == 't':
                    self.stan_konta -= (self.zadluzenie + odsetki)
                    self.zadluzenie = 0
                    print("Spłaciłeś kredyt wraz z odsetkami.")
                    break
                elif czy_splata.lower() == 'n':
                    print("Nie masz wystarczającej ilości pieniędzy na spłatę kredytu.")
                    print("Spróbuj ponownie później.")
                    break
                else:
                    print("Niepoprawny wybór! Wpisz 't' lub 'n'.")


                    