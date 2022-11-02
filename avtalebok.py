"""Avtalebok.
"""

#from asdf import Avtale, ny_avtale
from meny import MenyValg, MenyListe


# TODO(Issue l): Diverse.
def _start_meny(clear_terminal: bool = False) -> None:
    """Starter et menysystem.

    Args:
        clear_terminal: bool = False
            (Clear the terminal screen.)

    Returns:

    Raises:
    """

    meny_a = MenyListe(clear_terminal)
    meny_b = MenyListe(clear_terminal)

    meny_a.append(MenyValg("Valg A1.", print, "Kjører A1."))
    meny_a.append(MenyValg("Valg A2.", print, "Kjører A2."))
    meny_a.append(MenyValg("Valg A3.", print, "Kjører A3."))
    meny_a.append(MenyValg("Valg A4.", print, "Kjører A4."))
    meny_a.append(MenyValg("Meny B.", meny_b.show))
    meny_a.append(MenyValg("Avslutt."))

    meny_b.append(MenyValg("Valg B1.", print, "Kjører B1."))
    meny_b.append(MenyValg("Valg B2.", print, "Kjører B2."))
    meny_b.append(MenyValg("Valg B3.", print, "Kjører B3."))
    meny_b.append(MenyValg("Valg B4.", print, "Kjører B4."))
    meny_b.append(MenyValg("Meny A.", meny_a.show))
    meny_b.append(MenyValg("Avslutt."))

    meny_a.show()


def main() -> None:
    """Main.

    Args:

    Returns:

    Raises:
    """

    # Advarsel: clear_terminal = True
    _start_meny(clear_terminal = True)


if __name__ == "__main__":
    main()


