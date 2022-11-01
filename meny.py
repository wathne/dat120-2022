"""Klasser og funksjoner for et menysystem.
"""

from os import name, system
from typing import Any, Optional


# TODO(Issue l): Fullfør docstring, clear() bør være disabled by default.
def _clear() -> None:
    """Clear the terminal screen.

    F.eks.:

    Args:

    Returns:

    Raises:
    """

    if name == "nt":
        system("clr")  # Windows
    else:
        system("clear")  # Linux, Mac


# TODO(Issue l): Fullfør docstring, try/except og diverse.
class MenyValg():
    """Representerer et menyvalg.

    F.eks.:

    Attributes:
        text: str
        function: object
        arguments: Optional[Any]
    """

    def __init__(
            self,
            text: str,
            function: object = None,
            /,
            *args: Optional[Any]):
            # /, PEP 570: pylint: disable=keyword-arg-before-vararg
            #     (https://peps.python.org/pep-0570/)
            # Er Optional[Any] riktig typing?
        self.text = text
        self.function = function
        self.arguments = args  # args er en tuple med arguments.

    # TODO(Issue l): def __str__(self) -> str:

    # TODO(Issue l): Fullfør docstring, try/except og diverse.
    def run(self) -> None:
        """Kjører funksjonen til et menyvalg.

        F.eks.:

        Args:

        Returns:

        Raises:
        """

        if self.function is None:
            # TODO(Issue l): Kjør en avsluttende funksjon.
            pass
        else:
            # TODO(Issue l): Lag en try/except rundt denne.
            # DEBUG(MenyValg.run()):
            print("****************************************")
            print(f"DEBUG: function: {self.function}")
            print(f"DEBUG: arguments: {self.arguments}")
            print("****************************************")
            # self.arguments er en tuple med arguments.
            # *self.arguments (med ledende asterix) pakker ut arguments.
            self.function(*self.arguments)

# TODO(Issue l): Fullfør docstring, try/except og diverse.
class MenyListe():
    """Representerer en menyliste.

    F.eks.:

    Attributes:
        entries: list[MenyValg]
    """

    def __init__(
            self,
            entries: list[MenyValg]):
        self.entries = entries

    # TODO(Issue l): def __str__(self) -> str:

    # TODO(Issue l): Fullfør docstring, try/except og diverse.
    def _input(self) -> None:
        """Ber brukeren om å velge et menyvalg fra menylisten.

        F.eks.:

        Args:

        Returns:

        Raises:
        """

        # TODO(Issue l): Lag en try/except i en while loop.
        user_input = int(
            input(f" > Skriv et tall [0-{len(self.entries) - 1}]: "))
        print(f"    > Du valgte "
              f"{self.entries[user_input].text}[{user_input}]")
        self.entries[user_input].run()

    # TODO(Issue l): Fullfør docstring og diverse.
    def show(self) -> None:
        """Viser menylisten med menyvalg til brukeren.

        F.eks.:

        Args:

        Returns:

        Raises:
        """

        _clear()
        print("----------------------------------------")
        for i, entry in enumerate(self.entries):
            print(f"{entry.text}[{i}]")
        print("----------------------------------------")
        self._input()


# TODO(Issue l): Fullfør docstring, try/except og diverse.
def start_meny() -> None:
    """Starter et menysystem.

    F.eks.:

    Args:

    Returns:

    Raises:
    """

    pass


# TEST: _test_meny().
def _test_meny() -> None:
    """Tester et menysystem.

    F.eks.:

    Args:

    Returns:

    Raises:
    """

    # TODO(Issue l): test_meny_b is referenced before assignment.
    test_meny_a = MenyListe([
        MenyValg("Valg A1.", print, "Kjører A1."),
        MenyValg("Valg A2.", print, "Kjører A2."),
        MenyValg("Valg A3.", print, "Kjører A3."),
        MenyValg("Meny B."),
        MenyValg("Avslutt.")])

    test_meny_b = MenyListe([
        MenyValg("Valg B1.", print, "Kjører B1."),
        MenyValg("Valg B2.", print, "Kjører B2."),
        MenyValg("Valg B3.", print, "Kjører B3."),
        MenyValg("Meny A.", test_meny_a.show),
        MenyValg("Avslutt.")])

    test_meny_b.show()


if __name__ == "__main__":
    pass
    # TEST: _test_meny().
    print(_test_meny())


