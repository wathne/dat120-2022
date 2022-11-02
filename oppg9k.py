# -*- coding: utf-8 -*-

# FRA HOVED FILEN...
from datetime import datetime

class Avtale:
    """Representerer en avtale.

    Attributes:
        tittel: str
        sted: str
        starttidspunkt: datetime
        varighet: int
    """

    def __init__(
            self,
            tittel: str,
            sted: str,
            starttidspunkt: datetime,
            varighet: int):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet

    #TODO(Issue 9e): Lag en finere return string.
    def __str__(self) -> str:
        return (
            f"tittel: {self.tittel}, "
            f"sted: {self.sted}, "
            f"starttidspunkt: {self.starttidspunkt}, "
            f"varighet: {self.varighet}")
# Lager først en tomt liste, slik at man får lage en Liste med Avtaler objekter slik hovedfilen har gjort
# bare at hovedfilen har lagt en dictionary med avtaler istedetfor
tester= []
for i in range(24):
    avtaletest = Avtale(f"Test{i}","Sted",datetime.fromisoformat("2002-04-24 23:24:24"),15)
    tester.append(avtaletest)


# oppgave k:
# Lag en funksjon som tar inn ei liste med avtaler og en streng, og
# returnerer ei liste med alle avtaler hvor tittelen inneholder strengen. 
# Dere kan bruke find-metoden for strenger til å finne en delstreng i en større streng.
# https://www.w3schools.com/python/ref_string_find.asp
# https://www.w3schools.com/python/python_iterators.asp

def listestr(avtaleliste: list
             , string: str):
    str_sok_resultat = []       #ny liste som skal returneres på slutten av søket
    for avtale in avtaleliste: # leser hver avtale...
        sjekk = avtale.tittel # lokalvariabel som kun har tittel info til hver avtale
        if sjekk.find(string) >= 0: # sjekker om str finnes i hver avtale tittel, -1 : finnes ikke
            print(avtale)       # ekstra sjekk slikk at den printer avtalen der str fantes, hele avtalen.
            str_sok_resultat.append(avtale) # appender avtalen der den str finnes i avtalen tittelen
    return str_sok_resultat     

if __name__ == "__main__": #eksempel på det at den søker kun str-tallet "2"
    ggwp = listestr(tester,"2")
    

# fra asdf.py : - en dictionary blir lagt som "liste" av avtaler.
# liste_over_avtaler[1]
# Out[...]: <__main__.Avtale at 0x16c56f7d970>

# print(liste_over_avtaler[1])
# tittel: Test0, sted: Sted, starttidspunkt: 2002-04-24 23:24:24, varighet: 15