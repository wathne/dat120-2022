def skriv_til_tekstfil(fil, listen):


    avtale_liste = []
    avtale_liste.append(str(listen))
    with open(fil, "w", 1, "UTF-8") as ny_tekstfil:
        ny_tekstfil.writelines(avtale_liste)
        ny_tekstfil.close()
        while True:
            try:
                print("tekstfil laget")
            except ValueError:
                print("that is not a correct file name: type ""name"".txt")
            break
            
def lag_tekstfil(fil, listen):


    avtale_liste = []
    avtale_liste.append(str(listen))
    with open(fil, "w", 1, "UTF-8") as ny_tekstfil:
        for index in range(len(avtale_liste)):
            ny_tekstfil.writelines(avtale_liste[index].__repr__()+"\n")
            ny_tekstfil.close()
        while True:
            try:
                print("tekstfil laget")
            except ValueError:
                print("that is not a correct file name: type ""name"".txt")
            break

            
def fra_fil_til_liste(fil):

tekst = open(fil, "r")
liste = []
for linjer in tekst:
    linjer = linjer.rstrip()
    linjer = linjer.replace(' ','')
    linjer = linjer.split(',')
    liste.append(linjer)
summen = print(liste)
tekst.close()
return summen

        
            
def liste_med_avtaler_fra_tekst(fil):
    while True:
        try:
            with open(filnavn, "r", 1, "UTF-8") as AVTALE:
                pass
        except:
            print("Filen ikke funnet")
        with open(filnavn, "r", 1, "UTF-8") as AVTALE:
            for linje in AVTALE:
                tittel, sted, starttidspunkt, varighet = linje.split(",")
                tittel = tittel.strip()
                sted = sted.strip()
                starttidspunkt = starttidspunkt.strip()
                varighet = varighet.strip()
                liste_med_avtaler[tittel] = (tittel + ", " + sted + ", " + starttidspunkt + ", " + varighet)
            AVTALE.close()
            break
    return liste_med_avtaler

