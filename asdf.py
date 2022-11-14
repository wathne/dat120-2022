"""Klasser og funksjoner for å lage avtaler."""

from collections.abc import Generator
from contextlib import contextmanager
from datetime import datetime
from typing import Any
from typing import IO


_debug_enabled: bool = True


class Avtale:
    """Representerer en avtale.

    Attributes:
        tittel: str
        sted: str
        starttidspunkt: datetime
        varighet: int
    """

    tittel: str
    sted: str
    starttidspunkt: datetime
    varighet: int

    def __init__(
        self,
        tittel: str,
        sted: str,
        starttidspunkt: datetime,
        varighet: int,
    ) -> None:
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

    tittel: str
    sted: str
    starttidspunkt: datetime
    varighet: int

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

    return Avtale(tittel, sted, starttidspunkt, varighet)


def ny_avtale_til_avtaleliste(
    avtaleliste: list[Avtale],
) -> list[Avtale]:
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
    overskrift: str | None = None,
) -> list[Avtale]:
    """Skriver ut en liste med avtaler til skjermen.

    En avtaleliste er mutable. Vi bevarer id(avtaleliste).
    Det er ikke nødvendig å ta imot returverdien.
    id(avtaleliste) er identisk før og etter vis_avtaleliste().

    Args:
        avtaleliste: list[Avtale]
        overskrift: str | None = None

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


@contextmanager
def _opened_txt_file(
    filepath: str,
    mode: str,
) -> Generator[tuple[IO[Any] | None, OSError | None], None, None]:
    """A "with" statement context manager for opening a .txt file.

    For internal use.
    Handles OSError when opening a .txt file in a "with" statement.

    Args:
        filepath: str
        mode: str

    Yields:
        tuple[IO[Any] | None, OSError | None]

    Raises:
    """

    txt_file: IO[Any] | None = None
    txt_file_error: OSError | None = None

    try:
        txt_file = open(filepath, mode, encoding="utf-8", newline=None)
    except OSError as txt_file_error:
        yield (None, txt_file_error)
    else:
        try:
            yield (txt_file, None)
        except OSError as txt_file_error:
            yield (None, txt_file_error)
        finally:
            txt_file.close()


def skriv_til_tekstfil(
    avtaleliste: list[Avtale],
    tekstfil: str = "./avtalebok.txt",
) -> list[Avtale]:
    """Lagrer en liste med avtaler til en tekstfil.

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

    with _opened_txt_file(
        filepath=tekstfil,
        mode="wt",
    ) as (txt_file, txt_file_error):
        if txt_file_error:
            print(f"OSError: {txt_file_error}")
        elif txt_file is not None:
            txt_file.truncate(0)
            for avtale in avtaleliste:
                txt_file.write(
                    f"{avtale.tittel};"
                    f"{avtale.sted};"
                    f"{avtale.starttidspunkt};"
                    f"{avtale.varighet}")
                txt_file.write("\n")

    # DEBUG: skriv_til_tekstfil().
    if _debug_enabled:
        print(f"DEBUG: id(@skriv_til_tekstfil() avtaleliste): "
              f"{id(avtaleliste)}")

    return avtaleliste


def les_fra_tekstfil(
    avtaleliste: list[Avtale],
    tekstfil: str = "./avtalebok.txt",
) -> list[Avtale]:
    """Leser inn en liste med avtaler fra en tekstfil.

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

    with _opened_txt_file(
        filepath=tekstfil,
        mode="rt",
    ) as (txt_file, txt_file_error):
        if txt_file_error:
            print(f"OSError: {txt_file_error}")
        elif txt_file is not None:
            avtaleliste.clear()
            for line in txt_file:
                line_strip: str = line.strip("\n")
                line_split: list[str] = line_strip.split(";")
                tittel: str = str(line_split[0])
                sted: str = str(line_split[1])
                starttidspunkt: datetime = datetime.fromisoformat(line_split[2])
                varighet: int = int(line_split[3])
                avtaleliste.append(
                    Avtale(tittel, sted, starttidspunkt, varighet))

    # DEBUG: les_fra_tekstfil().
    if _debug_enabled:
        print(f"DEBUG: id(@les_fra_tekstfil() avtaleliste): "
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

    vis_avtaleliste(avtaleliste, "Slett en avtale fra avtalelisten:")
    print(f"[{len(avtaleliste)}]Gå tilbake uten å slette en avtale.")

    input_error: str = (
        f"\U0001F631 "
        f"Skriv et heltall [0-{len(avtaleliste)}].")
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

    # Skip the rebuild. (See below.)
    if slett == len(avtaleliste):
        return avtaleliste

    # Rebuild avtaleliste without breaking id(avtaleliste).
    # To skip deletion, simply set: slett = len(avtaleliste).
    temp_avtaleliste: list[Avtale] = []
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

    vis_avtaleliste(avtaleliste, "Endre en avtale fra avtalelisten:")
    print(f"[{len(avtaleliste)}]Gå tilbake uten å endre en avtale.")

    input_error: str = (
        f"\U0001F631 "
        f"Skriv et heltall [0-{len(avtaleliste)}].")
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

    # DEBUG: endre_avtale_fra_avtaleliste().
    if _debug_enabled:
        print(f"DEBUG: id(@endre_avtale_fra_avtaleliste() avtaleliste): "
              f"{id(avtaleliste)}")

    # Skip the rebuild. (See below.)
    if endre == len(avtaleliste):
        return avtaleliste

    print(f"{avtaleliste[endre]}")
    temp_avtale: Avtale = ny_avtale()

    # Rebuild avtaleliste without breaking id(avtaleliste).
    # To skip change, simply set: endre = len(avtaleliste).
    temp_avtaleliste: list[Avtale] = []
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


