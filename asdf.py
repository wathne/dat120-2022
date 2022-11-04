"""Klasser og funksjoner for å lage avtaler.
"""

from datetime import datetime
from typing import Optional


_debug_enabled = True


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
        avtaleliste: list[Avtale]) -> list[Avtale]:
    """Lager en ny avtale og legger avtalen til i en avtaleliste.

    Vil interaktivt be brukeren om å oppgi:
        tittel: str,
        sted: str,
        starttidspunkt: datetime,
        varighet: int.

    En avtaleliste er mutable. Vi bevarer id(avtaleliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(avtaleliste) er identisk før og etter
    ny_avtale_til_avtaleliste().

    Args:
        avtaleliste: list[Avtale]

    Returns:
        avtaleliste: list[Avtale]

    Raises:
    """

    avtaleliste.append(ny_avtale())

    # DEBUG: ny_avtale_til_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: id(@ny_avtale_til_avtaleliste() avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def vis_avtaleliste(
        avtaleliste: list[Avtale],
        overskrift: Optional[str] = None) -> list[Avtale]:
    """Skriver ut ei liste med avtaler til skjermen.

    En avtaleliste er mutable. Vi bevarer id(avtaleliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(avtaleliste) er identisk før og etter vis_avtaleliste().

    Args:
        avtaleliste: list[Avtale]
        overskrift: Optional[str] = None

    Returns:
        avtaleliste: list[Avtale]

    Raises:
    """

    if overskrift is not None:
        print(overskrift)
    for i, avtale in enumerate(avtaleliste):
        print(f"[{i}]{avtale}")

    # DEBUG: vis_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: id(@vis_avtaleliste() avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def skriv_til_tekstfil(
        avtaleliste: list[Avtale],
        tekstfil: str = "./avtalebok.txt") -> list[Avtale]:
    """Lagrer ei liste med avtaler til ei tekstfil.

    En avtaleliste er mutable. Vi bevarer id(avtaleliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(avtaleliste) er identisk før og etter skriv_til_tekstfil().

    Args:
        avtaleliste: list[Avtale]
        tekstfil: str = "./avtalebok.txt"

    Returns:
        avtaleliste: list[Avtale]

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

    # DEBUG: skriv_til_tekstfil().
    if _debug_enabled:
        print(f"DEBUG: id(@skriv_til_tekstfil() avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def les_fra_tekstfil(
        avtaleliste: list[Avtale],
        tekstfil: str = "./avtalebok.txt") -> list[Avtale]:
    """Leser inn ei liste med avtaler fra ei tekstfil.

    En avtaleliste er mutable. Vi bevarer id(avtaleliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(avtaleliste) er identisk før og etter les_fra_tekstfil().

    Args:
        avtaleliste: list[Avtale]
        tekstfil: str = "./avtalebok.txt"

    Returns:
        avtaleliste: list[Avtale]

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

    # DEBUG: les_fra_tekstfil().
    if _debug_enabled:
        print(f"DEBUG: id(@les_fra_tekstfil() avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def slett_avtale_fra_avtaleliste(
        avtaleliste: list[Avtale]) -> list[Avtale]:
    """Sletter en avtale fra en avtaleliste.

    Vil interaktivt be brukeren om å velge en avtale som skal slettes.
    Brukeren får også et valg om å gå tilbake uten å slette en avtale.

    En avtaleliste er mutable. Vi bevarer id(avtaleliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(avtaleliste) er identisk før og etter
    slett_avtale_fra_avtaleliste().

    Args:
        avtaleliste: list[Avtale]

    Returns:
        avtaleliste: list[Avtale]

    Raises:
    """

    # To skip deletion, simply set: slett = len(avtaleliste).
    slett = len(avtaleliste)

    vis_avtaleliste(avtaleliste, "Slett en avtale fra avtalelisten:")
    print(f"[{len(avtaleliste)}]Gå tilbake uten å slette en avtale.")

    input_error = (f"\U0001F631 "
                   f"Skriv et heltall [0-{len(avtaleliste)}]")
    while True:
        try:
            slett = int(
                input("Slett[int]: "))
        except (TypeError, ValueError):
            print(input_error)
            continue
        if not slett and slett != 0:
            print(input_error)
            continue
        if not 0 <= slett <= len(avtaleliste):
            print(input_error)
            continue
        break

    # DEBUG: slett_avtale_fra_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: id(@slett_avtale_fra_avtaleliste() avtaleliste): "
              f"{id(avtaleliste)}")

    # Rebuild avtaleliste without breaking id(avtaleliste).
    # To skip deletion, simply set: slett = len(avtaleliste).
    temp_avtaleliste = []
    for i, avtale in enumerate(avtaleliste):
        if i != slett:
            temp_avtaleliste.append(avtale)
    avtaleliste.clear()
    for avtale in temp_avtaleliste:
        avtaleliste.append(avtale)

    # DEBUG: slett_avtale_fra_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: id(@slett_avtale_fra_avtaleliste() avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def endre_avtale_fra_avtaleliste(
        avtaleliste: list[Avtale]) -> list[Avtale]:
    """Endrer en avtale fra en avtaleliste.

    Vil interaktivt be brukeren om å velge en avtale som skal endres.
    Brukeren får også et valg om å gå tilbake uten å endre en avtale.

    En avtaleliste er mutable. Vi bevarer id(avtaleliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(avtaleliste) er identisk før og etter
    endre_avtale_fra_avtaleliste().

    Args:
        avtaleliste: list[Avtale]

    Returns:
        avtaleliste: list[Avtale]

    Raises:
    """

    # To skip change, simply set: endre = len(avtaleliste).
    endre = len(avtaleliste)

    vis_avtaleliste(avtaleliste, "Endre en avtale fra avtalelisten:")
    print(f"[{len(avtaleliste)}]Gå tilbake uten å endre en avtale.")

    input_error = (f"\U0001F631 "
                   f"Skriv et heltall [0-{len(avtaleliste)}]")
    while True:
        try:
            endre = int(
                input("Endre[int]: "))
        except (TypeError, ValueError):
            print(input_error)
            continue
        if not endre and endre != 0:
            print(input_error)
            continue
        if not 0 <= endre <= len(avtaleliste):
            print(input_error)
            continue
        break

    if endre != len(avtaleliste):
        print(f"{avtaleliste[endre]}")
        temp_avtale = ny_avtale()

    # DEBUG: endre_avtale_fra_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: id(@endre_avtale_fra_avtaleliste() avtaleliste): "
              f"{id(avtaleliste)}")

    # Rebuild avtaleliste without breaking id(avtaleliste).
    # To skip change, simply set: endre = len(avtaleliste).
    temp_avtaleliste = []
    for i, avtale in enumerate(avtaleliste):
        if i != endre:
            temp_avtaleliste.append(avtale)
        if i == endre:
            temp_avtaleliste.append(temp_avtale)
    avtaleliste.clear()
    for avtale in temp_avtaleliste:
        avtaleliste.append(avtale)

    # DEBUG: endre_avtale_fra_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: id(@endre_avtale_fra_avtaleliste() avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


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


def _test_slett_avtale_fra_avtaleliste() -> None:
    """Tester slett_avtale_fra_avtaleliste().

    Args:

    Returns:

    Raises:
    """

    pass


def _test_endre_avtale_fra_avtaleliste() -> None:
    """Tester endre_avtale_fra_avtaleliste().

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

    # TEST: slett_avtale_fra_avtaleliste().
    #_test_slett_avtale_fra_avtaleliste

    # TEST: endre_avtale_fra_avtaleliste().
    #_test_endre_avtale_fra_avtaleliste


