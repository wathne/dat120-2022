from datetime import datetime


class Avtale:
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
            
def ny_avtale() -> Avtale:
    # Initialiserer variabler.
    tittel = str("-1")
    sted = str("-1")
    starttidspunkt = datetime.fromisoformat("0001-01-01 00:00:00")
    varighet = int(-1)
    
    # Sjekker input for variabel: tittel
    # TODO(Issue 9f): Oppdater input sjekk.
    while True:
        try:
            tittel = str(
                input("tittel[string]: "))
        except (TypeError, ValueError) as input_error:
            print(
                f"\U0001F631"
                f" {input_error}")
            continue
            
        if not tittel:
            input_error = "En midlertidig feilmelding."
            print(
                f"\U0001F631"
                f" {input_error}")
            continue
            
        break
        
    # Sjekker input for variabel: sted
    # TODO(Issue 9f): Oppdater input sjekk.
    while True:
        try:
            sted = str(
                input("sted[string]: "))
        except (TypeError, ValueError) as input_error:
            print(
                f"\U0001F631"
                f" {input_error}")
            continue
            
        if not sted:
            input_error = "En midlertidig feilmelding."
            print(
                f"\U0001F631"
                f" {input_error}")
            continue
            
        break
        
    # Sjekker input for variabel: starttidspunkt
    # TODO(Issue 9f): Oppdater input sjekk.
    while True:
        try:
            starttidspunkt = datetime.fromisoformat(
                input("starttidspunkt[ÅÅÅÅ-MM-DD TT:MM:SS]: "))
        except (TypeError, ValueError) as input_error:
            print(
                f"\U0001F631"
                f" {input_error}")
            continue
            
        if not starttidspunkt:
            input_error = "En midlertidig feilmelding."
            print(
                f"\U0001F631"
                f" {input_error}")
            continue
            
        break
        
    # Sjekker input for variabel: varighet
    # TODO(Issue 9f): Oppdater input sjekk.
    while True:
        try:
            varighet = int(
                input("varighet[int]: "))
        except (TypeError, ValueError) as input_error:
            print(
                f"\U0001F631"
                f" {input_error}")
            continue
            
        if not varighet:
            input_error = "En midlertidig feilmelding."
            print(
                f"\U0001F631"
                f" {input_error}")
            continue
            
        break
        
    return Avtale(tittel, sted, starttidspunkt, varighet)
    
    
if __name__ == "__main__":
    pass
    # TEST: ny_avtale().
    print(ny_avtale())
    
    
