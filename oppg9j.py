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
    
# oppgave j) Lag en funksjon som tar inn ei liste med avtaler og en dato  
# og returnerer ei liste med alle avtalene som foregår på denne datoen. 
# Funksjonen trenger bare å sjekke om datoen stemmer med dato-delen av 
# starttidspunktet til avtalen.

def listetid(avtaleliste: list
             , tid: datetime):          
    tid_sok_resultat = []       #ny liste som skal returneres på slutten av søket
    for avtale in avtaleliste: # leser hver avtale...
        sjekk = avtale.starttidspunkt # lokalvariabel som kun har datetime info til hver avtale
        if sjekk == tid: # sjekker om tiden er akkurat likt det som søkes.
            print(avtale)       # ekstra sjekk slikk at den printer avtalen der datetime fantes, hele avtalen.
            tid_sok_resultat.append(avtale) # appender avtalen der den datetime finnes i avtalen datetime info
    return tid_sok_resultat     

if __name__ == "__main__": #eksempel på det at den søker samme dato som alle avtaletest er laget.

    # Lager først en tomt liste, slik at man får lage en Liste med Avtaler objekter slik hovedfilen har gjort
    # bare at hovedfilen har lagt en dictionary med avtaler istedetfor
    tester= []
    for i in range(24):
        avtaletest = Avtale(f"Test{i}","Sted",datetime.fromisoformat("2002-04-24 23:24:24"),15)
        tester.append(avtaletest)

    ggwp = listetid(tester,datetime.fromisoformat("2002-04-24 23:24:24"))
    