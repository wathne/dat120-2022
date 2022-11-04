"""Avtalebok.

chmod a+rwx ./avtalebok.txt
chmod a+rwx ./test_avtalebok.txt
chmod a+rwx ./backup_test_avtalebok.txt
"""

from asdf import endre_avtale_fra_avtaleliste
from asdf import les_fra_tekstfil
from asdf import ny_avtale_til_avtaleliste
from asdf import skriv_til_tekstfil
from asdf import slett_avtale_fra_avtaleliste
from asdf import vis_avtaleliste
from meny import MenyListe
from meny import MenyValg


_debug_enabled = True


def _start_meny(clear_terminal: bool = False) -> None:
    """Starter et menysystem.

    Args:
        clear_terminal: bool = False
            (Clear the terminal screen.)

    Returns:

    Raises:
    """

    # Initialize list[Avtale] and filepath.
    avtaleliste = []
    overskrift = None
    tekstfil = "./avtalebok.txt"
    test_tekstfil = "./test_avtalebok.txt"
    backup_test_tekstfil = "./backup_test_avtalebok.txt"

    # Initialize MenyListe A, B and DEBUG
    meny_a = MenyListe(clear_terminal)
    meny_b = MenyListe(clear_terminal)
    meny_debug = MenyListe(clear_terminal)

    # TODO(Issue l): Import and add functions.
    # MenyValg function- and arguments-placeholders.
    show_all_avtale_text = "Vis alle avtaler."
    show_all_avtale_func = vis_avtaleliste
    show_all_avtale_args = (avtaleliste, overskrift,)
    read_file_text = "Les avtaler fra fil."
    read_file_func = les_fra_tekstfil
    read_file_args = (avtaleliste, tekstfil,)
    write_file_text = "Skriv avtaler til fil."
    write_file_func = skriv_til_tekstfil
    write_file_args = (avtaleliste, tekstfil,)
    create_avtale_text = "Lag en ny avtale."
    create_avtale_func = ny_avtale_til_avtaleliste
    create_avtale_args = (avtaleliste,)
    edit_avtale_text = "Rediger en avtale."
    edit_avtale_func = endre_avtale_fra_avtaleliste
    edit_avtale_args = (avtaleliste,)
    delete_avtale_text = "Slett en avtale."
    delete_avtale_func = slett_avtale_fra_avtaleliste
    delete_avtale_args = (avtaleliste,)

    # Populate MenyListe A with MenyValg.
    meny_a.append(MenyValg(
        show_all_avtale_text,
        show_all_avtale_func,
        show_all_avtale_args))
    meny_a.append(MenyValg(
        read_file_text,
        read_file_func,
        read_file_args))
    meny_a.append(MenyValg(
        write_file_text,
        write_file_func,
        write_file_args))
    meny_a.append(MenyValg(
        create_avtale_text,
        create_avtale_func,
        create_avtale_args))
    meny_a.append(MenyValg(
        edit_avtale_text,
        edit_avtale_func,
        edit_avtale_args))
    meny_a.append(MenyValg(
        delete_avtale_text,
        delete_avtale_func,
        delete_avtale_args))
    # DEBUG: En meny for diverse testing og feilsøking.
    if _debug_enabled:
        meny_a.append(MenyValg(
            "DEBUG meny.",
            meny_debug.show,
            ()))
    meny_a.append(MenyValg(
        "B meny.",
        meny_b.show,
        ()))
    meny_a.append(MenyValg(
        "Avslutt.",
        None,
        ()))

    # Populate MenyListe B with MenyValg.
    meny_b.append(MenyValg(
        "Valg B1.",
        print,
        ("Placeholder: Kjører B1.",)))
    meny_b.append(MenyValg(
        "Valg B2.",
        print,
        ("Placeholder: Kjører B2.",)))
    meny_b.append(MenyValg(
        "Valg B3.",
        print,
        ("Placeholder: Kjører B3.",)))
    meny_b.append(MenyValg(
        "Valg B4.",
        print,
        ("Placeholder: Kjører B4.",)))
    meny_b.append(MenyValg(
        "A meny.",
        meny_a.show,
        ()))
    meny_b.append(MenyValg(
        "Avslutt.",
        None,
        ()))

    # Populate MenyListe DEBUG with MenyValg.
    meny_debug.append(MenyValg(
        f"les_fra_tekstfil {test_tekstfil}",
        les_fra_tekstfil,
        (avtaleliste, test_tekstfil,)))
    meny_debug.append(MenyValg(
        f"skriv_til_tekstfil {test_tekstfil}",
        skriv_til_tekstfil,
        (avtaleliste, test_tekstfil,)))
    meny_debug.append(MenyValg(
        f"les_fra_tekstfil {backup_test_tekstfil}",
        les_fra_tekstfil,
        (avtaleliste, backup_test_tekstfil,)))
    meny_debug.append(MenyValg(
        "A meny.",
        meny_a.show,
        ()))
    meny_debug.append(MenyValg(
        "B meny.",
        meny_b.show,
        ()))
    meny_debug.append(MenyValg(
        "Avslutt.",
        None,
        ()))

    # Start the show :)
    meny_a.show()


def main() -> None:
    """Main.

    Args:

    Returns:

    Raises:
    """

    _start_meny(clear_terminal=False)


if __name__ == "__main__":
    main()


