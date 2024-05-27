class Gracz:
    def __init__(self, stan_konta=1001, zadluzenie=0):
        self.stan_konta = stan_konta
        self.zadluzenie = zadluzenie
        self.reka = []
        self.stawka = 0  

    def przegrana(self, kwota):
        self.stan_konta -= kwota


    def wygrana(self, kwota):
            self.stan_konta += kwota


    def sprawdz_stawke(self):
            return self.stan_konta >= self.stawka


    def dodaj_karte(self, karta):
            self.reka.append(karta)


    def usun_reke(self):
            self.reka = []


    def wyswietl_reke(self):
            print("Twoja ręka:")
            for karta in self.reka:
                print(f"{karta['wartosc']} {karta['kolor']}")


    def wyswietl_stan_konta(self):
            print(f"Stan konta: {self.stan_konta}")





