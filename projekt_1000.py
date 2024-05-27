import random
import time
import xklasa
import xruletka 
import xblackjack
import xautomaty
import xkości
import xwyscigi
import xloteria
import xpoker
import xkredyty
import xkredyts
import xpokazstan





def kasyno():
    print("=========================================================================")
    print("Witaj w naszym kasynie!")
    gracz = xklasa.Gracz() 


    while True:
        print("=========================================================================")
        print("Twój stan konta: $", gracz.stan_konta)
        print("Twoje zadłużenie: $", gracz.zadluzenie)
        print("\nWybierz opcję:")
        print("1. Zagraj w ruletkę")
        print("2. Zagraj w blackjacka")
        print("3. Zagraj w automaty do gier")
        print("4. Zagraj w kości")
        print("5. Wyścigi psów")
        print("6. Loteria")
        print("7. Zagraj w pokera")
        print("8. Zaciągnij kredyt")
        print("9. Spłać kredyt")
        print("10. Pokaż stan konta")
        print("11. Zakończ")


        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            xruletka.ruletka(gracz)
        elif wybor == "2":
            xblackjack.blackjack(gracz)
        elif wybor == "3":
            xautomaty.automaty(gracz)
        elif wybor == "4":
            xkości.kosci(gracz)
        elif wybor == "5":
            xwyscigi.wyścigi_psów(gracz)
        elif wybor == "6":
            xloteria.loteria(gracz)
        elif wybor == "7":
            xpoker.gra_poker(gracz)
        elif wybor == "8":
            xkredyty.zaciagnij_kredyt(gracz)
        elif wybor == "9":
            xkredyts.splata_kredytu(gracz)
        elif wybor == "10":
            xpokazstan.pokaz_stan_konta(gracz)
        elif wybor == "11":
            print("Dziękujemy za grę!")
            break
        else:
            print("Niepoprawny wybór!")

        if wybor == "cheat":
            gracz.stan_konta += 1000000
            print("Zostałeś właścicielem kasyna")


if __name__ == "__main__":
    kasyno()


print("dziękuje za zagranie w moją gre. licze na jakąś pozytywną ocene.")


