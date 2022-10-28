from datetime import datetime

class Avtale:
    def __init__(   self,
                    tittel,
                    sted,
                    starttidspunkt,
                    varighet):
        self.tittel = tittel                    #string
        self.sted = sted                        #string
        self.starttidspunkt = starttidspunkt    #datetime
        self.varighet = varighet                #int
        
    def __str__(self):
        return str(
            "tittel: " + str(self.tittel) +
            ", sted: " + str(self.sted) +
            ", starttidspunkt: " + str(self.starttidspunkt) +
            ", varighet: " + str(self.varighet))
            
def ny_avtale():
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
        except:
            ok = False
            print("\U0001F631")
            
    #sted
    ok = False
    while not ok:
        try:
            ok = True
            sted = str(
                input("sted[string]: "))
        except:
            ok = False
            print("\U0001F631")
            
    #starttidspunkt
    ok = False
    while not ok:
        try:
            ok = True
            starttidspunkt = datetime.fromisoformat(
                input("starttidspunkt[ÅÅÅÅ-MM-DD TT:MM:SS]: "))
        except:
            ok = False
            print("\U0001F631")
            
    #varighet
    ok = False
    while not ok:
        try:
            ok = True
            varighet = int(
                input("varighet[int]: "))
        except:
            ok = False
            print("\U0001F631")
            
    return Avtale(tittel, sted, starttidspunkt, varighet)
    
if __name__ == "__main__":
    pass
    #test
    print(ny_avtale())
    
