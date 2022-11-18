"""Avtalebok med menysystem.

Menysystemet drives av sammenhengende klasseinstanser istedenfor å
bruke en loop.
"""

from typing import Any

from tier1_liste import vis_liste
from tier1_meny import MenyListe
from tier1_meny import MenyValg
from tier2_kategori import endre_kategori_fra_kategoriliste
from tier2_kategori import Kategori
from tier2_kategori import ny_kategori_til_kategoriliste
from tier2_kategori import slett_kategori_fra_kategoriliste
from tier3_avtale import Avtale
from tier3_avtale import endre_avtale_fra_avtaleliste
from tier3_avtale import legg_til_kategori_til_avtale
from tier3_avtale import ny_avtale_til_avtaleliste
from tier3_avtale import slett_avtale_fra_avtaleliste
from tier4_io import les_fra_tekstfil
from tier4_io import skriv_til_tekstfil


_debug_enabled: bool = False


def _start_meny(
    clear_terminal: bool = False,
) -> None:
    """Starter et menysystem.

    Args:
        clear_terminal: bool = False
            (Clear the terminal screen.)

    Returns:

    Raises:
    """

    avtaleliste: list[Avtale] = []
    avtaleliste_fil: str = "./avtaleliste.txt"
    avtaleliste_overskrift: str | None = "Avtaleliste:"
    kategoriliste: list[Kategori] = []
    kategoriliste_fil: str = "./kategoriliste.txt"
    kategoriliste_overskrift: str | None = "Kategoriliste:"

    test_fil: str = "./test_avtaleliste.txt"
    backup_test_fil: str = "./backup_test_avtaleliste.txt"

    # Initialize MenyListe avtale, kategori, main, settings, debug
    meny_avtale: MenyListe = MenyListe(clear_terminal)
    meny_kategori: MenyListe = MenyListe(clear_terminal)
    meny_main: MenyListe = MenyListe(clear_terminal)
    meny_settings: MenyListe = MenyListe(clear_terminal)
    meny_debug: MenyListe = MenyListe(clear_terminal)

    # MenyValg function- and arguments-placeholders.
    add_kategori_to_avtale_text: str = "Legg til kategori til avtale."
    add_kategori_to_avtale_func: object | None = legg_til_kategori_til_avtale
    add_kategori_to_avtale_args: tuple[Any, ...] = (
        avtaleliste,
        kategoriliste,
    )
    show_all_avtale_text: str = "Vis alle avtaler."
    show_all_avtale_func: object | None = vis_liste
    show_all_avtale_args: tuple[Any, ...] = (
        avtaleliste,
        avtaleliste_overskrift,
    )
    read_avtale_file_text: str = "Les avtaler og kategorier fra fil."
    read_avtale_file_func: object | None = les_fra_tekstfil
    read_avtale_file_args: tuple[Any, ...] = (
        avtaleliste,
        avtaleliste_fil,
        kategoriliste,
        kategoriliste_fil,
    )
    write_avtale_file_text: str = "Skriv avtaler og kategorier til fil."
    write_avtale_file_func: object | None = skriv_til_tekstfil
    write_avtale_file_args: tuple[Any, ...] = (
        avtaleliste,
        avtaleliste_fil,
        kategoriliste,
        kategoriliste_fil,
    )
    create_avtale_text: str = "Lag en ny avtale."
    create_avtale_func: object | None = ny_avtale_til_avtaleliste
    create_avtale_args: tuple[Any, ...] = (
        avtaleliste,
    )
    edit_avtale_text: str = "Endre en avtale."
    edit_avtale_func: object | None = endre_avtale_fra_avtaleliste
    edit_avtale_args: tuple[Any, ...] = (
        avtaleliste,
    )
    delete_avtale_text: str = "Slett en avtale."
    delete_avtale_func: object | None = slett_avtale_fra_avtaleliste
    delete_avtale_args: tuple[Any, ...] = (
        avtaleliste,
    )

    # MenyValg function- and arguments-placeholders.
    show_all_kategori_text: str = "Vis alle kategorier."
    show_all_kategori_func: object | None = vis_liste
    show_all_kategori_args: tuple[Any, ...] = (
        kategoriliste,
        kategoriliste_overskrift,
    )
    read_kategori_file_text: str = "Les avtaler og kategorier fra fil."
    read_kategori_file_func: object | None = les_fra_tekstfil
    read_kategori_file_args: tuple[Any, ...] = (
        avtaleliste,
        avtaleliste_fil,
        kategoriliste,
        kategoriliste_fil,
    )
    write_kategori_file_text: str = "Skriv avtaler og kategorier til fil."
    write_kategori_file_func: object | None = skriv_til_tekstfil
    write_kategori_file_args: tuple[Any, ...] = (
        avtaleliste,
        avtaleliste_fil,
        kategoriliste,
        kategoriliste_fil,
    )
    create_kategori_text: str = "Lag en ny kategori."
    create_kategori_func: object | None = ny_kategori_til_kategoriliste
    create_kategori_args: tuple[Any, ...] = (
        kategoriliste,
    )
    edit_kategori_text: str = "Endre en kategori."
    edit_kategori_func: object | None = endre_kategori_fra_kategoriliste
    edit_kategori_args: tuple[Any, ...] = (
        kategoriliste,
    )
    delete_kategori_text: str = "Slett en kategori."
    delete_kategori_func: object | None = slett_kategori_fra_kategoriliste
    delete_kategori_args: tuple[Any, ...] = (
        kategoriliste,
    )

    # Populate MenyListe avtale with MenyValg.
    meny_avtale.append(MenyValg(
        "Hovedmeny.",
        meny_main.show,
        (),
    ))
    meny_avtale.append(MenyValg(
        show_all_avtale_text,
        show_all_avtale_func,
        show_all_avtale_args,
    ))
    meny_avtale.append(MenyValg(
        read_avtale_file_text,
        read_avtale_file_func,
        read_avtale_file_args,
    ))
    meny_avtale.append(MenyValg(
        write_avtale_file_text,
        write_avtale_file_func,
        write_avtale_file_args,
    ))
    meny_avtale.append(MenyValg(
        create_avtale_text,
        create_avtale_func,
        create_avtale_args,
    ))
    meny_avtale.append(MenyValg(
        edit_avtale_text,
        edit_avtale_func,
        edit_avtale_args,
    ))
    meny_avtale.append(MenyValg(
        delete_avtale_text,
        delete_avtale_func,
        delete_avtale_args,
    ))
    meny_avtale.append(MenyValg(
        add_kategori_to_avtale_text,
        add_kategori_to_avtale_func,
        add_kategori_to_avtale_args,
    ))
    meny_avtale.append(MenyValg(
        "Kategorimeny.",
        meny_kategori.show,
        (),
    ))
    # DEBUG: En meny for testing og feilsøking.
    if _debug_enabled:
        meny_avtale.append(MenyValg(
            "DEBUG meny.",
            meny_debug.show,
            (),
        ))

    # Populate MenyListe kategori with MenyValg.
    meny_kategori.append(MenyValg(
        "Hovedmeny.",
        meny_main.show,
        (),
    ))
    meny_kategori.append(MenyValg(
        show_all_kategori_text,
        show_all_kategori_func,
        show_all_kategori_args,
    ))
    meny_kategori.append(MenyValg(
        read_kategori_file_text,
        read_kategori_file_func,
        read_kategori_file_args,
    ))
    meny_kategori.append(MenyValg(
        write_kategori_file_text,
        write_kategori_file_func,
        write_kategori_file_args,
    ))
    meny_kategori.append(MenyValg(
        create_kategori_text,
        create_kategori_func,
        create_kategori_args,
    ))
    meny_kategori.append(MenyValg(
        edit_kategori_text,
        edit_kategori_func,
        edit_kategori_args,
    ))
    meny_kategori.append(MenyValg(
        delete_kategori_text,
        delete_kategori_func,
        delete_kategori_args,
    ))
    meny_kategori.append(MenyValg(
        add_kategori_to_avtale_text,
        add_kategori_to_avtale_func,
        add_kategori_to_avtale_args,
    ))
    meny_kategori.append(MenyValg(
        "Avtalemeny.",
        meny_avtale.show,
        (),
    ))
    # DEBUG: En meny for testing og feilsøking.
    if _debug_enabled:
        meny_kategori.append(MenyValg(
            "DEBUG meny.",
            meny_debug.show,
            (),
        ))

    # Populate MenyListe main with MenyValg.
    meny_main.append(MenyValg(
        "Hovedmeny.",
        meny_main.show,
        (),
    ))
    meny_main.append(MenyValg(
        "Avtalemeny.",
        meny_avtale.show,
        (),
    ))
    meny_main.append(MenyValg(
        "Kategorimeny.",
        meny_kategori.show,
        (),
    ))
    meny_main.append(MenyValg(
        "Innstillinger.",
        meny_settings.show,
        (),
    ))
    # DEBUG: En meny for testing og feilsøking.
    if _debug_enabled:
        meny_main.append(MenyValg(
            "DEBUG meny.",
            meny_debug.show,
            (),
        ))
    meny_main.append(MenyValg(
        "Avslutt.",
        None,
        (),
    ))

    # Populate MenyListe settings with MenyValg.
    meny_settings.append(MenyValg(
        "Hovedmeny.",
        meny_main.show,
        (),
    ))

    # Populate MenyListe debug with MenyValg.
    meny_debug.append(MenyValg(
        "Hovedmeny.",
        meny_main.show,
        (),
    ))
    meny_debug.append(MenyValg(
        f"les_fra_tekstfil() {test_fil}, {kategoriliste_fil}",
        les_fra_tekstfil,
        (avtaleliste, test_fil, kategoriliste, kategoriliste_fil),
    ))
    meny_debug.append(MenyValg(
        f"skriv_til_tekstfil() {test_fil}, {kategoriliste_fil}",
        skriv_til_tekstfil,
        (avtaleliste, test_fil, kategoriliste, kategoriliste_fil),
    ))
    meny_debug.append(MenyValg(
        f"les_fra_tekstfil() {backup_test_fil}, {kategoriliste_fil}",
        les_fra_tekstfil,
        (avtaleliste, backup_test_fil, kategoriliste, kategoriliste_fil),
    ))

    # Start the show :)
    meny_main.show()


def main() -> None:
    """Main.

    Args:

    Returns:

    Raises:
    """

    _start_meny(clear_terminal=False)


if __name__ == "__main__":
    main()


