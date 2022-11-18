"""Klasse, metoder og funksjoner for kategorier."""

from tier1_liste import vis_liste


_debug_enabled: bool = False


class Kategori:
    """Representerer en kategori.

    Attributes:
        id_: int
        navn: str
        prioritet: int
    """

    _prioritet_string: tuple[None, str, str, str] = (
        None,
        "Vanlig",
        "Viktig",
        "Svært viktig")

    def __init__(
        self,
        id_: int,
        navn: str,
        prioritet: int = 1,
    ) -> None:
        self.id_: int = id_
        self.navn: str = navn
        self.prioritet: int = prioritet

    #TODO(Issue 10c): Lag en finere return string.
    def __str__(self) -> str:
        return (
            f"id_: {self.id_}, "
            f"navn: {self.navn}, "
            f"prioritet: {self.prioritet} "
            f"({self._prioritet_string[self.prioritet]}).")


def ny_kategori() -> Kategori:
    """Lager en ny kategori.

    Vil interaktivt be brukeren om å oppgi:
        id_: int
        navn: str
        prioritet: int

    Args:

    Returns:
        En Kategori med attributes:
            id_: int
            navn: str
            prioritet: int

    Raises:
    """

    id_: int
    navn: str
    prioritet: int

    # id_
    id_input_error: str = (
        "\U0001F631 "
        "Skriv et positivt heltall [int].")
    while True:
        try:
            id_ = int(
                input("ID [int]: "))
        except (TypeError, ValueError):
            print(id_input_error)
            continue
        if not id_ and id_ != 0:
            print(id_input_error)
            continue
        if id_ < 0:
            print(id_input_error)
            continue
        break

    # navn
    navn_input_error: str = (
        "\U0001F631 "
        "Skriv et gyldig navn [string].")
    while True:
        try:
            navn = str(
                input("Navn [string]: "))
        except (TypeError, ValueError):
            print(navn_input_error)
            continue
        if not navn:
            print(navn_input_error)
            continue
        break

    # prioritet
    prioritet_input_error: str = (
        "\U0001F631 "
        "Skriv et positivt heltall [1-3]"
        "(1: Vanlig, 2: Viktig, 3: Svært viktig).")
    while True:
        try:
            prioritet = int(
                input("Prioritet [int]: "))
        except (TypeError, ValueError):
            print(prioritet_input_error)
            continue
        if not prioritet and prioritet != 0:
            print(prioritet_input_error)
            continue
        if not 1 <= prioritet <= 3:
            print(prioritet_input_error)
            continue
        break

    return Kategori(id_, navn, prioritet)


def ny_kategori_til_kategoriliste(
    kategoriliste: list[Kategori],
) -> list[Kategori]:
    """Lager en ny kategori og legger den til i en kategoriliste.

    Vil interaktivt be brukeren om å oppgi:
        id_: int
        navn: str
        prioritet: int

    En kategoriliste er mutable. Vi bevarer id(kategoriliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(kategoriliste) er identisk før og etter
    ny_kategori_til_kategoriliste().

    Args:
        kategoriliste: list[Kategori]

    Returns:
        kategoriliste: list[Kategori]

    Raises:
    """

    kategoriliste.append(ny_kategori())

    # DEBUG: ny_kategori_til_kategoriliste().
    if _debug_enabled:
        print(f"DEBUG: @ny_kategori_til_kategoriliste(): id(kategoriliste): "
              f"{id(kategoriliste)}")

    return kategoriliste


def slett_kategori_fra_kategoriliste(
    kategoriliste: list[Kategori],
) -> list[Kategori]:
    """Sletter en kategori fra en kategoriliste.

    Vil interaktivt be brukeren om å velge en kategori som skal slettes.
    Brukeren får også et valg om å gå tilbake uten å slette en kategori.

    En kategoriliste er mutable. Vi bevarer id(kategoriliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(kategoriliste) er identisk før og etter
    slett_kategori_fra_kategoriliste().

    Args:
        kategoriliste: list[Kategori]

    Returns:
        kategoriliste: list[Kategori]

    Raises:
    """

    # To skip deletion, simply set: slett = len(kategoriliste).
    slett: int = len(kategoriliste)

    vis_liste(kategoriliste, "Slett en kategori fra kategorilisten:")
    print(f"[{len(kategoriliste)}]Gå tilbake uten å slette en kategori.")

    input_error: str = (
        f"\U0001F631 "
        f"Skriv et heltall [0-{len(kategoriliste)}].")
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
        if not 0 <= slett <= len(kategoriliste):
            print(input_error)
            continue
        break

    # DEBUG: slett_kategori_fra_kategoriliste().
    if _debug_enabled:
        print(f"DEBUG: @slett_kategori_fra_kategoriliste(): id(kategoriliste): "
              f"{id(kategoriliste)}")

    # Skip the rebuild. (See below.)
    if slett == len(kategoriliste):
        return kategoriliste

    # Rebuild kategoriliste without breaking id(kategoriliste).
    # To skip deletion, simply set: slett = len(kategoriliste).
    temp_kategoriliste: list[Kategori] = []
    i: int
    kategori: Kategori
    for i, kategori in enumerate(kategoriliste):
        if i != slett:
            temp_kategoriliste.append(kategori)
    kategoriliste.clear()
    for kategori in temp_kategoriliste:
        kategoriliste.append(kategori)

    # DEBUG: slett_kategori_fra_kategoriliste().
    if _debug_enabled:
        print(f"DEBUG: @slett_kategori_fra_kategoriliste(): id(kategoriliste): "
              f"{id(kategoriliste)}")

    return kategoriliste


def endre_kategori_fra_kategoriliste(
    kategoriliste: list[Kategori],
) -> list[Kategori]:
    """Endrer en kategori fra en kategoriliste.

    Vil interaktivt be brukeren om å velge en kategori som skal endres.
    Brukeren får også et valg om å gå tilbake uten å endre en kategori.

    En kategoriliste er mutable. Vi bevarer id(kategoriliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(kategoriliste) er identisk før og etter
    endre_kategori_fra_kategoriliste().

    Args:
        kategoriliste: list[Kategori]

    Returns:
        kategoriliste: list[Kategori]

    Raises:
    """

    # To skip change, simply set: endre = len(kategoriliste).
    endre: int = len(kategoriliste)

    vis_liste(kategoriliste, "Endre en kategori fra kategorilisten:")
    print(f"[{len(kategoriliste)}]Gå tilbake uten å endre en kategori.")

    input_error: str = (
        f"\U0001F631 "
        f"Skriv et heltall [0-{len(kategoriliste)}].")
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
        if not 0 <= endre <= len(kategoriliste):
            print(input_error)
            continue
        break

    # DEBUG: endre_kategori_fra_kategoriliste().
    if _debug_enabled:
        print(f"DEBUG: @endre_kategori_fra_kategoriliste(): id(kategoriliste): "
              f"{id(kategoriliste)}")

    # Skip the rebuild. (See below.)
    if endre == len(kategoriliste):
        return kategoriliste

    print(f"{kategoriliste[endre]}")
    temp_kategori: Kategori = ny_kategori()

    # Rebuild kategoriliste without breaking id(kategoriliste).
    # To skip change, simply set: endre = len(kategoriliste).
    temp_kategoriliste: list[Kategori] = []
    i: int
    kategori: Kategori
    for i, kategori in enumerate(kategoriliste):
        if i != endre:
            temp_kategoriliste.append(kategori)
        if i == endre:
            temp_kategoriliste.append(temp_kategori)
    kategoriliste.clear()
    for kategori in temp_kategoriliste:
        kategoriliste.append(kategori)

    # DEBUG: endre_kategori_fra_kategoriliste().
    if _debug_enabled:
        print(f"DEBUG: @endre_kategori_fra_kategoriliste(): id(kategoriliste): "
              f"{id(kategoriliste)}")

    return kategoriliste


def _test_ny_kategori_til_kategoriliste() -> None:
    """Tester ny_kategori_til_kategoriliste().

    Args:

    Returns:

    Raises:
    """

    pass


def _test_slett_kategori_fra_kategoriliste() -> None:
    """Tester slett_kategori_fra_kategoriliste().

    Args:

    Returns:

    Raises:
    """

    pass


def _test_endre_kategori_fra_kategoriliste() -> None:
    """Tester endre_kategori_fra_kategoriliste().

    Args:

    Returns:

    Raises:
    """

    pass


if __name__ == "__main__":
    pass

    # TEST: ny_kategori_til_kategoriliste().
    #_test_ny_kategori_til_kategoriliste()

    # TEST: slett_kategori_fra_kategoriliste().
    #_test_slett_kategori_fra_kategoriliste

    # TEST: endre_kategori_fra_kategoriliste().
    #_test_endre_kategori_fra_kategoriliste


