"""Klasse, metoder og funksjoner for avtaler."""

from datetime import datetime

from tier1_liste import vis_liste
from tier2_kategori import Kategori


_debug_enabled: bool = False


class Avtale:
    """Representerer en avtale.

    Attributes:
        tittel: str
        sted: str
        starttidspunkt: datetime
        varighet: int
        kategorier: list[Kategori]
    """

    def __init__(
        self,
        tittel: str,
        sted: str,
        starttidspunkt: datetime,
        varighet: int,
        kategorier: list[Kategori] | Kategori | None = None,
    ) -> None:
        self.tittel: str = tittel
        self.sted: str = sted
        self.starttidspunkt: datetime = starttidspunkt
        self.varighet: int = varighet
        self.kategorier: list[Kategori] = []
        if kategorier is not None:
            if isinstance(kategorier, Kategori):
                self.kategorier.append(kategorier)
            else:
                self.kategorier.extend(kategorier)

    #TODO(Issue 9e): Lag en finere return string.
    def __str__(self) -> str:
        return (
            f"tittel: {self.tittel}, "
            f"sted: {self.sted}, "
            f"starttidspunkt: {self.starttidspunkt}, "
            f"varighet: {self.varighet}, "
            f"kategorier: {', '.join(str(k) for k in self.kategorier)}.")

    def legg_til_kategori(
        self,
        kategori: Kategori
    ) -> None:
        """Legger til en kategori til avtalen.

        Args:
            kategori: Kategori

        Returns:

        Raises:
        """

        self.kategorier.append(kategori)


def legg_til_kategori_til_avtale(
    avtaleliste: list[Avtale],
    kategoriliste: list[Kategori],
) -> tuple[list[Avtale], list[Kategori]]:
    """Legger til kategori til avtale.

    Legger til en kategori fra en kategoriliste til en avtale fra en
    avtaleliste. Vil interaktivt be brukeren om å velge en avtale fra
    avtalelisten og velge en kategori fra kategorilisten.
    Brukeren får også et valg om å gå tilbake uten å endre en avtale.

    En liste er mutable. Vi bevarer id(liste).
    Det er ikke nødvendig å ta imot returverdien.
    id(liste) er identisk før og etter
    legg_til_kategori_til_avtale().

    Args:
        avtaleliste: list[Avtale]
        kategoriliste: list[Kategori]

    Returns:
        tuple[list[Avtale], list[Kategori]]

    Raises:
    """

    # To skip change, simply set: index = len(liste).
    index_a: int = len(avtaleliste)
    index_k: int = len(kategoriliste)

    vis_liste(avtaleliste, "Endre en avtale fra avtalelisten:")
    print(f"[{len(avtaleliste)}]Gå tilbake uten å endre en avtale.")

    a_input_error: str = (
        f"\U0001F631 "
        f"Skriv et heltall [0-{len(avtaleliste)}].")
    while True:
        try:
            index_a = int(
                input("Endre avtale [int]: "))
        except (TypeError, ValueError):
            print(a_input_error)
            continue
        if not index_a and index_a != 0:
            print(a_input_error)
            continue
        if not 0 <= index_a <= len(avtaleliste):
            print(a_input_error)
            continue
        break

    # Skip change.
    if index_a == len(avtaleliste):
        return (avtaleliste, kategoriliste)

    print(f"{avtaleliste[index_a]}")

    vis_liste(kategoriliste, "Legg til kategori til avtalen:")
    print(f"[{len(kategoriliste)}]Gå tilbake uten å endre avtalen.")

    k_input_error: str = (
        f"\U0001F631 "
        f"Skriv et heltall [0-{len(kategoriliste)}].")
    while True:
        try:
            index_k = int(
                input("Legg til kategori [int]: "))
        except (TypeError, ValueError):
            print(k_input_error)
            continue
        if not index_k and index_k != 0:
            print(k_input_error)
            continue
        if not 0 <= index_k <= len(kategoriliste):
            print(k_input_error)
            continue
        break

    # Skip change.
    if index_k == len(kategoriliste):
        return (avtaleliste, kategoriliste)

    avtaleliste[index_a].legg_til_kategori(kategoriliste[index_k])

    # DEBUG: legg_til_kategori_til_avtale().
    if _debug_enabled:
        print(f"DEBUG: @legg_til_kategori_til_avtale(): id(avtaleliste): "
              f"{id(avtaleliste)}")
        print(f"DEBUG: @legg_til_kategori_til_avtale(): id(kategoriliste): "
              f"{id(kategoriliste)}")

    return (avtaleliste, kategoriliste)


def ny_avtale() -> Avtale:
    """Lager en ny avtale.

    Vil interaktivt be brukeren om å oppgi:
        tittel: str
        sted: str
        starttidspunkt: datetime
        varighet: int

    Args:

    Returns:
        En Avtale med attributes:
            tittel: str
            sted: str
            starttidspunkt: datetime
            varighet: int
            kategorier: list[Kategori]

    Raises:
    """

    tittel: str
    sted: str
    starttidspunkt: datetime
    varighet: int
    kategorier: list[Kategori]

    # tittel
    tittel_input_error: str = (
        "\U0001F631 "
        "Skriv en gyldig tittel [string].")
    while True:
        try:
            tittel = str(
                input("Tittel [string]: "))
        except (TypeError, ValueError):
            print(tittel_input_error)
            continue
        if not tittel:
            print(tittel_input_error)
            continue
        break

    # sted
    sted_input_error: str = (
        "\U0001F631 "
        "Skriv et gyldig sted [string].")
    while True:
        try:
            sted = str(
                input("Sted [string]: "))
        except (TypeError, ValueError):
            print(sted_input_error)
            continue
        if not sted:
            print(sted_input_error)
            continue
        break

    # starttidspunkt
    starttidspunkt_input_error: str = (
        "\U0001F631 "
        "Skriv en gyldig dato [ÅÅÅÅ-MM-DD TT:MM:SS]. (ISO format.)")
    while True:
        try:
            starttidspunkt = datetime.fromisoformat(
                input("Starttidspunkt [ÅÅÅÅ-MM-DD TT:MM:SS]: "))
        except (TypeError, ValueError):
            print(starttidspunkt_input_error)
            continue
        if not starttidspunkt:
            print(starttidspunkt_input_error)
            continue
        break

    # varighet
    varighet_input_error: str = (
        "\U0001F631 "
        "Skriv et positivt heltall [int].")
    while True:
        try:
            varighet = int(
                input("Varighet [int]: "))
        except (TypeError, ValueError):
            print(varighet_input_error)
            continue
        if not varighet and varighet != 0:
            print(varighet_input_error)
            continue
        if varighet < 0:
            print(varighet_input_error)
            continue
        break

    # kategorier
    kategorier = []

    return Avtale(tittel, sted, starttidspunkt, varighet, kategorier)


def ny_avtale_til_avtaleliste(
    avtaleliste: list[Avtale],
) -> list[Avtale]:
    """Lager en ny avtale og legger den til i en avtaleliste.

    Vil interaktivt be brukeren om å oppgi:
        tittel: str
        sted: str
        starttidspunkt: datetime
        varighet: int

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
        print(f"DEBUG: @ny_avtale_til_avtaleliste(): id(avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def slett_avtale_fra_avtaleliste(
    avtaleliste: list[Avtale],
) -> list[Avtale]:
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
    slett: int = len(avtaleliste)

    vis_liste(avtaleliste, "Slett en avtale fra avtalelisten:")
    print(f"[{len(avtaleliste)}]Gå tilbake uten å slette en avtale.")

    input_error: str = (
        f"\U0001F631 "
        f"Skriv et heltall [0-{len(avtaleliste)}].")
    while True:
        try:
            slett = int(
                input("Slett [int]: "))
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
        print(f"DEBUG: @slett_avtale_fra_avtaleliste(): id(avtaleliste): "
              f"{id(avtaleliste)}")

    # Skip the rebuild. (See below.)
    if slett == len(avtaleliste):
        return avtaleliste

    # Rebuild avtaleliste without breaking id(avtaleliste).
    # To skip deletion, simply set: slett = len(avtaleliste).
    temp_avtaleliste: list[Avtale] = []
    i: int
    avtale: Avtale
    for i, avtale in enumerate(avtaleliste):
        if i != slett:
            temp_avtaleliste.append(avtale)
    avtaleliste.clear()
    for avtale in temp_avtaleliste:
        avtaleliste.append(avtale)

    # DEBUG: slett_avtale_fra_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: @slett_avtale_fra_avtaleliste(): id(avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def endre_avtale_fra_avtaleliste(
    avtaleliste: list[Avtale],
) -> list[Avtale]:
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
    endre: int = len(avtaleliste)

    vis_liste(avtaleliste, "Endre en avtale fra avtalelisten:")
    print(f"[{len(avtaleliste)}]Gå tilbake uten å endre en avtale.")

    input_error: str = (
        f"\U0001F631 "
        f"Skriv et heltall [0-{len(avtaleliste)}].")
    while True:
        try:
            endre = int(
                input("Endre [int]: "))
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

    # DEBUG: endre_avtale_fra_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: @endre_avtale_fra_avtaleliste(): id(avtaleliste): "
              f"{id(avtaleliste)}")

    # Skip the rebuild. (See below.)
    if endre == len(avtaleliste):
        return avtaleliste

    print(f"{avtaleliste[endre]}")
    temp_avtale: Avtale = ny_avtale()

    # Rebuild avtaleliste without breaking id(avtaleliste).
    # To skip change, simply set: endre = len(avtaleliste).
    temp_avtaleliste: list[Avtale] = []
    i: int
    avtale: Avtale
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
        print(f"DEBUG: @endre_avtale_fra_avtaleliste(): id(avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def _test_legg_til_kategori_til_avtale() -> None:
    """Tester legg_til_kategori_til_avtale().

    Args:

    Returns:

    Raises:
    """

    pass


def _test_ny_avtale_til_avtaleliste() -> None:
    """Tester ny_avtale_til_avtaleliste().

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

    # TEST: legg_til_kategori_til_avtale().
    #_test_legg_til_kategori_til_avtale()

    # TEST: ny_avtale_til_avtaleliste().
    #_test_ny_avtale_til_avtaleliste()

    # TEST: slett_avtale_fra_avtaleliste().
    #_test_slett_avtale_fra_avtaleliste

    # TEST: endre_avtale_fra_avtaleliste().
    #_test_endre_avtale_fra_avtaleliste


