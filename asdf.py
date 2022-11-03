"""Klasser og funksjoner for å lage avtaler.
"""

from datetime import datetime
from typing import Optional


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


def ny_avtale() -> Avtale:
    """Lager en ny Avtale.

    Vil interaktivt be brukeren om å oppgi:
        tittel: str,
        sted: str,
        starttidspunkt: datetime,
        varighet: int.

    Args:

    Returns:
        En Avtale med attributes:
            tittel: str,
            sted: str,
            starttidspunkt: datetime,
            varighet: int.

    Raises:
    """

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


# oppg. g:

# Initialliserer variabler
liste_over_avtaler = list()

def vis_avtaleliste(avtaleliste,overskrift = "Liste over Avtaler"):
    #Overskrift
    print(overskrift)
    index = 1
    for x in avtaleliste:
        print(f"{index}: {x}")
        index += 1

# Testinput for lang liste med avtaler med samme tid, men (litt) forskjellig tittel
for i in range(24):
    avtaletest = Avtale(f"Test{i}",f"Sted{i}",datetime.fromisoformat("2002-04-24 23:24:24"),15+i)
    liste_over_avtaler.append(avtaletest)

vis_avtaleliste(liste_over_avtaler)

# # TODO(Issue g): vis_avtaleliste().
# def vis_avtaleliste(
#         avtaleliste: list,
#         overskrift: str = None) -> None:
#     """Skriver ut ei liste med avtaler til skjermen.

#     Args:
#         avtaleliste: list[Avtale]
#         overskrift: Optional[str] = None

#     Returns:

#     Raises:
#     """

#     if overskrift is None:
#         pass  # Placeholder.
#     else:
#         pass  # Placeholder.


def _test_avtaleliste() -> None:
    """Tester vis_avtaleliste().

    Args:

    Returns:

    Raises:
    """

    sample_avtaleliste = []

    vis_avtaleliste(sample_avtaleliste)


if __name__ == "__main__":
    pass

    # TEST: ny_avtale().
    #test_avtale = ny_avtale()
    #print(test_avtale)

    # TEST: vis_avtaleliste().
    _test_avtaleliste()


