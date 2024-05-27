

def zaciagnij_kredyt(self):
        while True:
            czy_kredyt = input("Czy chcesz zaciągnąć kredyt? (t/n): ")
            if czy_kredyt.lower() == 't':
                while True:
                    kwota_kredytu = input("Podaj kwotę kredytu do zaciągnięcia: ")
                    if kwota_kredytu.isdigit() and int(kwota_kredytu) > 0:
                        self.stan_konta += int(kwota_kredytu)
                        self.zadluzenie += int(kwota_kredytu)
                        print("Zaciągnąłeś kredyt na kwotę $", kwota_kredytu)
                        break
                    else:
                        print("Niepoprawna kwota kredytu! Podaj liczbę całkowitą większą od 0.")
                break
            elif czy_kredyt.lower() == 'n':
                break
            else:
                print("Niepoprawny wybór! Wpisz 't' lub 'n'.")


# # =====================================================================================================================================================

