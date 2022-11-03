def lag_tekstfil(fil, liste):
    with open(fil, "w", 1, "UTF-8") as FILA:
        for index in range(len(liste)):
            FILA.writelines(liste[index].__repr__()+"\n")
            FILA.close()

def avtale_til_tekst(filn):
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
