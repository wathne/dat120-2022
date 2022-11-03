def lag_tekstfil(filnavn):
    with open(filnavn, "w", 1, "UTF-8") as FILA:
        for index in range(len(Intern_liste)):
            FILA.writelines(Intern_liste[index].__repr__()+"\n")
            FILA.close()

def avtale_til_tekst(filnavn):
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
                Intern_liste[tittel] = (tittel + ", " + sted + ", " + starttidspunkt + ", " + varighet)
            AVTALE.close()
            break
    return Intern_liste
