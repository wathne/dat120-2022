"""Funksjoner for å lese/skrive avtaler og kategorier fra/til tekstfil."""

from collections.abc import Generator
from contextlib import contextmanager
from datetime import datetime
from typing import Any
from typing import IO

from tier2_kategori import Kategori
from tier3_avtale import Avtale


_debug_enabled: bool = False


@contextmanager
def _opened_txt_file(
    file_path: str,
    mode: str,
) -> Generator[tuple[IO[Any] | None, OSError | None], None, None]:
    """A "with" statement context manager for opening a .txt file.

    For internal use.
    Handles OSError when opening a .txt file in a "with" statement.

    Args:
        file_path: str
        mode: str

    Yields:
        tuple[IO[Any] | None, OSError | None]

    Raises:
    """

    txt_file: IO[Any] | None = None
    txt_file_error: OSError | None = None

    try:
        txt_file = open(file_path, mode, encoding="utf-8", newline=None)
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
    liste: list[Avtale | Kategori],
    liste_type: str,
    tekstfil: str,
) -> list[Avtale | Kategori]:
    """Lagrer en liste med avtaler eller kategorier til en tekstfil.

    En liste er mutable. Vi bevarer id(liste).
    Det er ikke nødvendig å ta imot returverdien.
    id(liste) er identisk før og etter skriv_til_tekstfil().

    Args:
        liste: list[Avtale | Kategori]
        liste_type: str = "Avtale" | "Kategori"
        tekstfil: str

    Returns:
        liste: list[Avtale | Kategori]

    Raises:
    """

    with _opened_txt_file(
        file_path=tekstfil,
        mode="wt",
    ) as (txt_file, txt_file_error):
        if txt_file_error:
            print(f"OSError: {txt_file_error}")
        elif txt_file is not None and liste_type == "Avtale":
            txt_file.truncate(0)
            for avtale in (x for x in liste if isinstance(x, Avtale)):
                txt_file.write(
                    f"{avtale.tittel};"
                    f"{avtale.sted};"
                    f"{avtale.starttidspunkt};"
                    f"{avtale.varighet}")
                    # TODO(wathne): kategorier
                txt_file.write("\n")
        elif txt_file is not None and liste_type == "Kategori":
            txt_file.truncate(0)
            for kategori in (x for x in liste if isinstance(x, Kategori)):
                txt_file.write(
                    f"{kategori.id_};"
                    f"{kategori.navn};"
                    f"{kategori.prioritet}")
                txt_file.write("\n")

    # DEBUG: skriv_til_tekstfil().
    if _debug_enabled:
        print(f"DEBUG: @skriv_til_tekstfil(): id(liste): "
              f"{id(liste)}")

    return liste


def les_fra_tekstfil(
    liste: list[Avtale | Kategori],
    liste_type: str,
    tekstfil: str,
) -> list[Avtale | Kategori]:
    """Leser inn en liste med avtaler eller kategorier fra en tekstfil.

    En liste er mutable. Vi bevarer id(liste).
    Det er ikke nødvendig å ta imot returverdien.
    id(liste) er identisk før og etter les_fra_tekstfil().

    Args:
        liste: list[Avtale | Kategori]
        liste_type: str = "Avtale" | "Kategori"
        tekstfil: str

    Returns:
        liste: list[Avtale | Kategori]

    Raises:
    """

    with _opened_txt_file(
        file_path=tekstfil,
        mode="rt",
    ) as (txt_file, txt_file_error):
        if txt_file_error:
            print(f"OSError: {txt_file_error}")
        elif txt_file is not None and liste_type in {"Avtale", "Kategori"}:
            liste.clear()
            for line in txt_file:
                line_strip: str = line.strip("\n")
                line_split: list[str] = line_strip.split(";")
                if liste_type == "Avtale":
                    tittel: str = str(line_split[0])
                    sted: str = str(line_split[1])
                    starttidspunkt: datetime = datetime.fromisoformat(
                        line_split[2])
                    varighet: int = int(line_split[3])
                    # TODO(wathne): kategorier
                    liste.append(
                        Avtale(tittel, sted, starttidspunkt, varighet))
                if liste_type == "Kategori":
                    id_: int = int(line_split[0])
                    navn: str = str(line_split[1])
                    prioritet: int = int(line_split[2])
                    liste.append(
                        Kategori(id_, navn, prioritet))

    # DEBUG: les_fra_tekstfil().
    if _debug_enabled:
        print(f"DEBUG: @les_fra_tekstfil(): id(liste): "
              f"{id(liste)}")

    return liste


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

    # TEST: skriv_til_tekstfil().
    #_test_skriv_til_tekstfil()

    # TEST: les_fra_tekstfil().
    #_test_les_fra_tekstfil()


