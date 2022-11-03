"""Avtalebok.
"""

from asdf import ny_avtale, vis_avtaleliste
from meny import MenyValg, MenyListe


def _start_meny(clear_terminal: bool = False) -> None:
    """Starter et menysystem.

    Args:
        clear_terminal: bool = False
            (Clear the terminal screen.)

    Returns:

    Raises:
    """

    # Initialize MenyListe.
    meny_a = MenyListe(clear_terminal)
    meny_b = MenyListe(clear_terminal)

    # TODO(Issue l): Import and add functions.
    # MenyValg function- and arguments-placeholders.
    show_all_avtale_text = "Vis alle avtaler."
    show_all_avtale_func = vis_avtaleliste
    show_all_avtale_args = ([],)  # TODO(Issue l): Avtaleliste som arg.
    read_file_text = "Les avtaler fra fil."
    read_file_func = print
    read_file_args = ("Placeholder: Leser avtaler fra fil.",)
    write_file_text = "Skriv avtaler til fil."
    write_file_func = print
    write_file_args = ("Placeholder: Skriver avtaler til fil.",)
    create_avtale_text = "Lag en ny avtale."
    create_avtale_func = ny_avtale
    create_avtale_args = ()
    edit_avtale_text = "Rediger en avtale."
    edit_avtale_func = print
    edit_avtale_args = ("Placeholder: Redigerer en avtale.",)
    delete_file_text = "Slett en avtale."
    delete_file_func = print
    delete_file_args = ("Placeholder: Sletter en avtale.",)

    # Populate MenyListe with MenyValg.
    meny_a.append(MenyValg(
        show_all_avtale_text, show_all_avtale_func, show_all_avtale_args))
    meny_a.append(MenyValg(
        read_file_text, read_file_func, read_file_args))
    meny_a.append(MenyValg(
        write_file_text, write_file_func, write_file_args))
    meny_a.append(MenyValg(
        create_avtale_text, create_avtale_func, create_avtale_args))
    meny_a.append(MenyValg(
        edit_avtale_text, edit_avtale_func, edit_avtale_args))
    meny_a.append(MenyValg(
        delete_file_text, delete_file_func, delete_file_args))
    meny_a.append(MenyValg(
        "Meny B.", meny_b.show, ()))
    meny_a.append(MenyValg(
        "Avslutt.", None, ()))

    meny_b.append(MenyValg(
        "Valg B1.", print, ("Placeholder: Kjører B1.",)))
    meny_b.append(MenyValg(
        "Valg B2.", print, ("Placeholder: Kjører B2.",)))
    meny_b.append(MenyValg(
        "Valg B3.", print, ("Placeholder: Kjører B3.",)))
    meny_b.append(MenyValg(
        "Valg B4.", print, ("Placeholder: Kjører B4.",)))
    meny_b.append(MenyValg(
        "Meny A.", meny_a.show, ()))
    meny_b.append(MenyValg(
        "Avslutt.", None, ()))

    meny_a.show()


def main() -> None:
    """Main.

    Args:

    Returns:

    Raises:
    """

    _start_meny(clear_terminal = False)


if __name__ == "__main__":
    main()


