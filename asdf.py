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
    """Lager en ny avtale.

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


def ny_avtale_til_avtaleliste(
        avtaleliste: list[Avtale]) -> None:
    """Lager en ny avtale og legger avtalen til i en avtaleliste.

    Vil interaktivt be brukeren om å oppgi:
        tittel: str,
        sted: str,
        starttidspunkt: datetime,
        varighet: int.

    Args:

    Returns:

    Raises:
    """

    avtaleliste.append(ny_avtale())


def vis_avtaleliste(
        avtaleliste: list[Avtale],
        overskrift: Optional[str] = None) -> None:
    """Skriver ut ei liste med avtaler til skjermen.

    Args:
        avtaleliste: list[Avtale]
        overskrift: Optional[str] = None

    Returns:

    Raises:
    """

    if overskrift is None:
        pass
    else:
        print(overskrift)
    for i, avtale in enumerate(avtaleliste):
        print(f"[{i}]{avtale}")


def skriv_til_tekstfil(
        avtaleliste: list[Avtale],
        tekstfil: str = "./avtalebok.txt") -> None:
    """Lagrer ei liste med avtaler til ei tekstfil.

    Args:
        avtaleliste: list[Avtale]
        tekstfil: str = "./avtalebok.txt"

    Returns:

    Raises:
    """

    with open(tekstfil, mode="w", encoding="utf-8") as txt_file:
        txt_file.truncate(0)
        for avtale in avtaleliste:
            txt_file.write(
                f"{avtale.tittel};"
                f"{avtale.sted};"
                f"{avtale.starttidspunkt};"
                f"{avtale.varighet}")
            txt_file.write("\n")
        txt_file.close()


def les_fra_tekstfil(
        avtaleliste: list[Avtale],
        tekstfil: str = "./avtalebok.txt") -> None:
    """Leser inn ei liste med avtaler fra ei tekstfil.

    Args:
        avtaleliste: list[Avtale]
        tekstfil: str = "./avtalebok.txt"

    Returns:

    Raises:
    """

    with open(tekstfil, mode="r", encoding="utf-8") as txt_file:
        avtaleliste.clear()
        for line in txt_file:
            line = line.strip("\n")
            line = line.split(";")
            tittel = line[0]
            sted = line[1]
            starttidspunkt = line[2]
            varighet = line[3]
            avtaleliste.append(
                Avtale(tittel, sted, starttidspunkt, varighet))
        txt_file.close()


def _test_vis_avtaleliste() -> None:
    """Tester vis_avtaleliste().

    Args:

    Returns:

    Raises:
    """

    pass

    #sample_avtaleliste = []

    #vis_avtaleliste(sample_avtaleliste)


def _test_skriv_til_tekstfil() -> None:
    """Tester skriv_til_tekstfil().

    Args:

    Returns:

    Raises:
    """

    pass


def _test_les_fra_tekstfil() -> None:
    """Tester les_fra_tekstfil().

    Args:

    Returns:

    Raises:
    """

    pass


if __name__ == "__main__":
    pass

    # TEST: ny_avtale().
    #test_avtale = ny_avtale()
    #print(test_avtale)

    # TEST: vis_avtaleliste().
    #_test_vis_avtaleliste()

    # TEST: skriv_til_tekstfil().
    #_test_skriv_til_tekstfil()

    # TEST: les_fra_tekstfil().
    #_test_les_fra_tekstfil()


