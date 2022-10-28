from datetime import datetime

class Avtale:
    def __init__(   self,
                    tittel: str,
                    sted: str,
                    starttidspunkt: datetime,
                    varighet: int):
        self.tittel = tittel                    #str
        self.sted = sted                        #str
        self.starttidspunkt = starttidspunkt    #datetime
        self.varighet = varighet                #int
        
    def __str__(self) -> str:
        return str(
            "tittel: " + str(self.tittel) +
            ", sted: " + str(self.sted) +
            ", starttidspunkt: " + str(self.starttidspunkt) +
            ", varighet: " + str(self.varighet))
            
def ny_avtale() -> Avtale:
    tittel = str("-1")
    sted = str("-1")
    starttidspunkt = datetime.fromisoformat("0001-01-01 00:00:00")
    varighet = int(-1)
    
    #tittel
    ok = False
    while not ok:
        try:
            ok = True
            tittel = str(
                input("tittel[string]: "))
                
            #TODO lag en bedre input sjekk (midlertidig if-test nedenfor)
            if not tittel or 1 + 1 == 3 or "tekst" == "feil":
                raise ValueError
            #(midlertidig if-test ovenfor)
            
        except (TypeError, ValueError) as input_error:
            ok = False
            print("\U0001F631")
            
    #sted
    ok = False
    while not ok:
        try:
            ok = True
            sted = str(
                input("sted[string]: "))
                
            #TODO lag en bedre input sjekk (midlertidig if-test nedenfor)
            if not sted or 1 + 1 == 3 or "tekst" == "feil":
                raise ValueError
            #(midlertidig if-test ovenfor)
            
        except (TypeError, ValueError) as input_error:
            ok = False
            print("\U0001F631")
            
    #starttidspunkt
    ok = False
    while not ok:
        try:
            ok = True
            starttidspunkt = datetime.fromisoformat(
                input("starttidspunkt[ÅÅÅÅ-MM-DD TT:MM:SS]: "))
                
            #TODO lag en bedre input sjekk (midlertidig if-test nedenfor)
            if not starttidspunkt or 1 + 1 == 3 or "tekst" == "feil":
                raise ValueError
            #(midlertidig if-test ovenfor)
            
        except (TypeError, ValueError) as input_error:
            ok = False
            print("\U0001F631")
            
    #varighet
    ok = False
    while not ok:
        try:
            ok = True
            varighet = int(
                input("varighet[int]: "))
                
            #TODO lag en bedre input sjekk (midlertidig if-test nedenfor)
            if not varighet or 1 + 1 == 3 or "tekst" == "feil":
                raise ValueError
            #(midlertidig if-test ovenfor)
            
        except (TypeError, ValueError) as input_error:
            ok = False
            print("\U0001F631")
            
    return Avtale(tittel, sted, starttidspunkt, varighet)
    
if __name__ == "__main__":
    pass
    #test
    print(ny_avtale())
    
