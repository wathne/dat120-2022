"""Klasser og funksjoner for et menysystem.
"""

from os import name, system
from typing import Any


_debug_enabled = True


def _clear() -> None:
    """Clear the terminal screen.

    Args:

    Returns:

    Raises:
    """

    if name == "nt":
        system("clr")  # Windows
    else:
        system("clear")  # Linux, Mac


class MenyValg():
    """Representerer et menyvalg.

    Attributes:
        text: str
        function: object = None
        arguments: tuple[Any, ...] = ()
        parent: MenyListe = None
        storage: Any = None
    """

    def __init__(
            self,
            text: str,
            function: object = None,
            args: tuple[Any, ...] = ()):
        self.text = text
        self.function = function
        self.arguments = args
        # self.parent will be set to meny_x by meny_x.append().
        self.parent = None
        self.storage = None

    # TODO(Issue l): def __str__(self) -> str:

    def run(self) -> None:
        """Kjører funksjonen til et menyvalg.

        Args:

        Returns:

        Raises:
            SystemExit("\U0001F92F Avslutter.")
        """

        if self.function is None:
            pass  # Placeholder.
            # TODO(Issue l): Kjør en avsluttende funksjon.
            raise SystemExit("\U0001F92F Avslutter.")
        else:
            # DEBUG: MenyValg.run().
            if _debug_enabled:
                print(f"DEBUG: function: {self.function}")
                print(f"DEBUG: arguments: {self.arguments}")
                print(f"DEBUG: parent: {self.parent}")
            # TODO(Issue l): Lag en try/except rundt denne.
            # self.arguments is a tuple of arguments.
            # *self.arguments (with leading asterix) unpacks the arguments.
            # self.storage grabs the return of self.function(*self.arguments).
            self.storage = self.function(*self.arguments)
            # DEBUG: MenyValg.run().
            if _debug_enabled:
                print(f"DEBUG: storage: {self.storage}")
            if self.parent is None:
                pass  # Placeholder.
                # TODO(Issue l): Kjør en avsluttende funksjon.
                raise SystemExit("\U0001F92F Avslutter.")
            else:
                self.parent.show()


class MenyListe():
    """Representerer en menyliste.

    For å lage en ny menyliste så må vi først initialisere en tom MenyList
    og deretter bruker vi append() funksjonen for å legge til et MenyValg.

    En MenyList er et mutable objekt. Den egenskapen er viktig for
    at et MenyValg i test_meny_a skal kunne kjøre funksjonen
    test_meny_b.show() og at et MenyValg i test_meny_b skal kunne
    kjøre funksjonen test_meny_a.show().
    (Sirkulær referanse mellom to menylister, a og b.)
    (Obs! Traceback kan bli lang.)

    Attributes:
        entries: list[MenyValg]
        clear_terminal: bool = False
    """

    def __init__(
            self,
            clear_terminal: bool = False):
        self.entries = []
        self.clear_terminal = clear_terminal

    # TODO(Issue l): def __str__(self) -> str:

    def append(self, entry: MenyValg) -> None:
        """Legger et menyvalg til i menylisten.

        Args:

        Returns:

        Raises:
        """

        entry.parent = self
        self.entries.append(entry)

    def _input(self) -> None:
        """Ber brukeren om å velge et menyvalg fra menylisten.

        Args:

        Returns:

        Raises:
        """

        # TODO(Issue l): Lag en try/except i en while loop rundt denne.
        user_input = int(
            input(f" > Skriv et tall "
                  f"[0-{len(self.entries) - 1}]: "))
        print(f"    > Du valgte: "
              f"[{user_input}]"
              f"{self.entries[user_input].text}")
        self.entries[user_input].run()

    def show(self) -> None:
        """Viser menylisten med menyvalg til brukeren.

        Args:

        Returns:

        Raises:
        """

        if self.clear_terminal:
            _clear()
        print("----------------------------------------")
        for i, entry in enumerate(self.entries):
            print(f"[{i}]{entry.text}")
        print("----------------------------------------")
        self._input()


# TEST: _test_meny().
def _test_meny(clear_terminal: bool = False) -> None:
    """Tester et menysystem.

    Args:
        clear_terminal: bool = False
            (Clear the terminal screen.)

    Returns:

    Raises:
    """

    test_meny_a = MenyListe(clear_terminal)
    test_meny_b = MenyListe(clear_terminal)
    # DEBUG: _test_meny().
    if _debug_enabled:
        print(f"DEBUG: id(test_meny_a): {id(test_meny_a)}")
        print(f"DEBUG: id(test_meny_b): {id(test_meny_b)}")

    test_meny_a.append(MenyValg(
        "Valg A1.",
        print,
        ("Kjører A1.",)))
    test_meny_a.append(MenyValg(
        "Valg A2.",
        print,
        ("Kjører A2.",)))
    test_meny_a.append(MenyValg(
        "Valg A3.",
        print,
        ("Kjører A3.",)))
    test_meny_a.append(MenyValg(
        "Valg A4.",
        print,
        ("Kjører A4.",)))
    test_meny_a.append(MenyValg(
        "Meny B.",
        test_meny_b.show,
        ()))
    test_meny_a.append(MenyValg(
        "Avslutt.",
        None,
        ()))
    # DEBUG: _test_meny().
    if _debug_enabled:
        print(f"DEBUG: id(test_meny_a): {id(test_meny_a)}")
        print(f"DEBUG: id(test_meny_b): {id(test_meny_b)}")

    test_meny_b.append(MenyValg(
        "Valg B1.",
        print,
        ("Kjører B1.",)))
    test_meny_b.append(MenyValg(
        "Valg B2.",
        print,
        ("Kjører B2.",)))
    test_meny_b.append(MenyValg(
        "Valg B3.",
        print,
        ("Kjører B3.",)))
    test_meny_b.append(MenyValg(
        "Valg B4.",
        print,
        ("Kjører B4.",)))
    test_meny_b.append(MenyValg(
        "Meny A.",
        test_meny_a.show,
        ()))
    test_meny_b.append(MenyValg(
        "Avslutt.",
        None,
        ()))
    # DEBUG: _test_meny().
    if _debug_enabled:
        print(f"DEBUG: id(test_meny_a): {id(test_meny_a)}")
        print(f"DEBUG: id(test_meny_b): {id(test_meny_b)}")

    test_meny_a.show()


if __name__ == "__main__":
    pass

    # TEST: _test_meny().
    _debug_enabled = True
    _test_meny(clear_terminal=False)


