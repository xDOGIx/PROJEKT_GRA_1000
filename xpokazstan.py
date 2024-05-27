import random


def pokaz_stan_konta(self):
        print("=========================================================================")
        print("Twój aktualny stan konta: $", self.stan_konta)
        print("Twoje zadłużenie: $", self.zadluzenie)
        print("=========================================================================")


def rzut_kostka(self):
        return random.randint(1, 6)
