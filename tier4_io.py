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
def _opened_txt_files(
    file_paths: tuple[str, str],
    mode: str,
) -> Generator[
    tuple[IO[Any] | None, IO[Any] | None, OSError | None],
    None,
    None,
]:
    """A "with" statement context manager for opening two .txt files.

    For internal use.
    Handles OSError when opening two .txt files in a "with" statement.

    Args:
        file_paths: tuple[str, str]
        mode: str

    Yields:
        tuple[IO[Any] | None, IO[Any] | None, OSError | None]

    Raises:
    """

    txt_file_0: IO[Any] | None = None
    txt_file_1: IO[Any] | None = None
    txt_file_error: OSError | None = None

    try:
        txt_file_0 = open(file_paths[0], mode, encoding="utf-8", newline=None)
        txt_file_1 = open(file_paths[1], mode, encoding="utf-8", newline=None)
    except OSError as txt_file_error:
        yield (None, None, txt_file_error)
    else:
        try:
            yield (txt_file_0, txt_file_1, None)
        except OSError as txt_file_error:
            yield (None, None, txt_file_error)
        finally:
            txt_file_1.close()
            txt_file_0.close()


def skriv_til_tekstfil(
    avtaleliste: list[Avtale],
    avtaleliste_fil: str,
    kategoriliste: list[Kategori],
    kategoriliste_fil: str,
) -> tuple[list[Avtale], list[Kategori]]:
    """Skriver avtaleliste og kategoriliste til tekstfil.

    En liste er mutable. Vi bevarer id(liste).
    Det er ikke nødvendig å ta imot returverdien.
    id(liste) er identisk før og etter skriv_til_tekstfil().

    Args:
        avtaleliste: list[Avtale]
        avtaleliste_fil: str
        kategoriliste: list[Kategori]
        kategoriliste_fil: str

    Returns:
        tuple[list[Avtale], list[Kategori]]

    Raises:
    """

    txt_file_0: IO[Any] | None = None
    txt_file_1: IO[Any] | None = None
    txt_file_error: OSError | None = None
    kategori: Kategori
    avtale: Avtale

    with _opened_txt_files(
        file_paths=(avtaleliste_fil, kategoriliste_fil),
        mode="wt",
    ) as (txt_file_0, txt_file_1, txt_file_error):
        if txt_file_error is not None:
            print(f"OSError: {txt_file_error}")
        elif txt_file_0 is not None and txt_file_1 is not None:
            # kategoriliste
            txt_file_1.truncate(0)
            for kategori in (
                    x for x in kategoriliste if isinstance(x, Kategori)):
                txt_file_1.write(
                    f"{kategori.id_};"
                    f"{kategori.navn};"
                    f"{kategori.prioritet}")
                txt_file_1.write("\n")

            # avtaleliste
            txt_file_0.truncate(0)
            for avtale in (
                    x for x in avtaleliste if isinstance(x, Avtale)):
                txt_file_0.write(
                    f"{avtale.tittel};"
                    f"{avtale.sted};"
                    f"{avtale.starttidspunkt};"
                    f"{avtale.varighet};"
                    f"{','.join(str(k.id_) for k in avtale.kategorier)}")
                txt_file_0.write("\n")

    # DEBUG: skriv_til_tekstfil().
    if _debug_enabled:
        print(f"DEBUG: @skriv_til_tekstfil(): id(avtaleliste): "
              f"{id(avtaleliste)}")
        print(f"DEBUG: @skriv_til_tekstfil(): id(kategoriliste): "
              f"{id(kategoriliste)}")

    return (avtaleliste, kategoriliste)


def les_fra_tekstfil(
    avtaleliste: list[Avtale],
    avtaleliste_fil: str,
    kategoriliste: list[Kategori],
    kategoriliste_fil: str,
) -> tuple[list[Avtale], list[Kategori]]:
    """Leser avtaleliste og kategoriliste fra tekstfil.

    En liste er mutable. Vi bevarer id(liste).
    Det er ikke nødvendig å ta imot returverdien.
    id(liste) er identisk før og etter les_fra_tekstfil().

    Args:
        avtaleliste: list[Avtale]
        avtaleliste_fil: str
        kategoriliste: list[Kategori]
        kategoriliste_fil: str

    Returns:
        tuple[list[Avtale], list[Kategori]]

    Raises:
    """

    txt_file_0: IO[Any] | None = None
    txt_file_1: IO[Any] | None = None
    txt_file_error: OSError | None = None
    line: Any
    line_strip: str
    line_split: list[str]
    kategori: Kategori

    with _opened_txt_files(
        file_paths=(avtaleliste_fil, kategoriliste_fil),
        mode="rt",
    ) as (txt_file_0, txt_file_1, txt_file_error):
        if txt_file_error is not None:
            print(f"OSError: {txt_file_error}")
        elif txt_file_0 is not None and txt_file_1 is not None:
            # kategoriliste
            id_: int
            navn: str
            prioritet: int

            kategoriliste.clear()
            for line in txt_file_1:
                line_strip = line.strip("\n")
                line_split = line_strip.split(";")

                # TODO(wathne): try/except.
                id_ = int(line_split[0])
                navn = str(line_split[1])
                prioritet = int(line_split[2])

                kategoriliste.append(Kategori(
                    id_,
                    navn,
                    prioritet,
                ))
            try:
                del id_
            except NameError:
                pass
            try:
                del navn
            except NameError:
                pass
            try:
                del prioritet
            except NameError:
                pass

            # avtaleliste
            tittel: str
            sted: str
            starttidspunkt: datetime
            varighet: int
            kategorier: list[Kategori]
            k_id_string: str
            k_id_string_split: list[str]
            k_id_list: list[int]
            k_id: int

            avtaleliste.clear()
            for line in txt_file_0:
                line_strip = line.strip("\n")
                line_split = line_strip.split(";")

                # TODO(wathne): try/except.
                tittel = str(line_split[0])
                sted = str(line_split[1])
                starttidspunkt = datetime.fromisoformat(line_split[2])
                varighet = int(line_split[3])

                # TODO(wathne): try/except.
                # kategorier
                kategorier = []
                k_id_string = str(line_split[4])
                k_id_string_split = k_id_string.split(",")
                try:
                    k_id_list = [int(x) for x in k_id_string_split if x]
                except (TypeError, ValueError):
                    # TODO(wathne): Ta vare på delvis liste.
                    k_id_list = []
                for k_id in k_id_list:
                    for kategori in kategoriliste:
                        if k_id == kategori.id_:
                            kategorier.append(kategori)

                avtaleliste.append(Avtale(
                    tittel,
                    sted,
                    starttidspunkt,
                    varighet,
                    kategorier,
                ))
            try:
                del tittel
            except NameError:
                pass
            try:
                del sted
            except NameError:
                pass
            try:
                del starttidspunkt
            except NameError:
                pass
            try:
                del varighet
            except NameError:
                pass
            try:
                del kategorier
            except NameError:
                pass
            try:
                del k_id_string
            except NameError:
                pass
            try:
                del k_id_string_split
            except NameError:
                pass
            try:
                del k_id_list
            except NameError:
                pass
            try:
                del k_id
            except NameError:
                pass

    # DEBUG: les_fra_tekstfil().
    if _debug_enabled:
        print(f"DEBUG: @les_fra_tekstfil(): id(avtaleliste): "
              f"{id(avtaleliste)}")
        print(f"DEBUG: @les_fra_tekstfil(): id(kategoriliste): "
              f"{id(kategoriliste)}")

    return (avtaleliste, kategoriliste)


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


