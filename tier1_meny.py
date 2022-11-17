"""Klasser og metoder for menysystem.

Menysystemet drives av sammenhengende klasseinstanser istedenfor å
bruke en loop.
"""

from __future__ import annotations

from os import name
from os import system
from typing import Any


_debug_enabled: bool = False


def _clear() -> None:
    """Clear the terminal screen.

    For internal use.

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
        function: object | None
        arguments: tuple[Any, ...]
        parent: MenyListe | None
        storage: Any | None
    """

    def __init__(
        self,
        text: str,
        function: object | None = None,
        args: tuple[Any, ...] = (),
    ) -> None:
        self.text: str = text
        self.function: object | None = function
        self.arguments: tuple[Any, ...] = args
        # self.parent will be set to meny_x by meny_x.append().
        self.parent: MenyListe | None = None
        # self.storage grabs the return of self.function(*self.arguments).
        self.storage: Any | None = None

    # TODO(Issue l): def __str__(self) -> str:

    def run(self) -> None:
        """Kjører funksjonen til et menyvalg.

        Args:

        Returns:

        Raises:
            SystemExit("\U0001F92F Avslutter.")
        """

        # DEBUG: MenyValg.run().
        if _debug_enabled:
            print(f"DEBUG: function: {self.function}")
            print(f"DEBUG: arguments: {self.arguments}")
            print(f"DEBUG: parent: {self.parent}")
            print(f"DEBUG: storage: {self.storage}")
            print(f"DEBUG: id(storage): {id(self.storage)}")

        if self.function is None:
            pass  # Placeholder.
            # TODO(Issue l): Kjør en avsluttende funksjon.
            raise SystemExit("\U0001F92F Avslutter.")
        else:
            if callable(self.function):
                # TODO(Issue l): Lag en try/except rundt denne.
                # self.arguments is a tuple of arguments.
                # *self.arguments (with leading asterix) unpacks the arguments.
                # self.storage grabs the return of
                # self.function(*self.arguments).
                self.storage = self.function(*self.arguments)

            # DEBUG: MenyValg.run().
            if _debug_enabled:
                print(f"DEBUG: storage: {self.storage}")
                print(f"DEBUG: id(storage): {id(self.storage)}")

            if self.parent is None:
                pass  # Placeholder.
                # TODO(Issue l): Kjør en avsluttende funksjon.
                raise SystemExit("\U0001F92F Avslutter.")
            else:
                self.parent.storage = self.storage

                # DEBUG: MenyValg.run().
                if _debug_enabled:
                    print(f"DEBUG: parent.storage: "
                          f"{self.parent.storage}")
                    print(f"DEBUG: id(parent.storage): "
                          f"{id(self.parent.storage)}")

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
        clear_terminal: bool
        storage: Any | None
    """

    def __init__(
        self,
        clear_terminal: bool = False,
    ) -> None:
        self.entries: list[MenyValg] = []
        self.clear_terminal: bool = clear_terminal
        # self.storage will be set by valg_x.run().
        # self.storage grabs the return of valg_x.function(*valg_x.arguments).
        self.storage: Any | None = None

    # TODO(Issue l): def __str__(self) -> str:

    def append(
        self,
        entry: MenyValg,
    ) -> None:
        """Legger et menyvalg til i menylisten.

        Args:
            entry: MenyValg

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
        user_input: int = int(
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

        # DEBUG: MenyListe.show().
        if _debug_enabled:
            print(f"DEBUG: @MenyListe.show(): id(storage): {id(self.storage)}")

        if self.clear_terminal:
            _clear()
        print("----------------------------------------")
        for i, entry in enumerate(self.entries):
            print(f"[{i}]{entry.text}")
        print("----------------------------------------")
        self._input()


def _test_meny(
    clear_terminal: bool = False,
) -> None:
    """Tester et menysystem.

    Args:
        clear_terminal: bool = False
            (Clear the terminal screen.)

    Returns:

    Raises:
    """

    test_meny_a: MenyListe = MenyListe(clear_terminal)
    test_meny_b: MenyListe = MenyListe(clear_terminal)

    # DEBUG: _test_meny().
    if _debug_enabled:
        print(f"DEBUG: id(test_meny_a): {id(test_meny_a)}")
        print(f"DEBUG: id(test_meny_b): {id(test_meny_b)}")

    test_meny_a.append(MenyValg(
        "Valg A1.",
        print,
        ("Kjører A1.",),
    ))
    test_meny_a.append(MenyValg(
        "Valg A2.",
        print,
        ("Kjører A2.",),
    ))
    test_meny_a.append(MenyValg(
        "Valg A3.",
        print,
        ("Kjører A3.",),
    ))
    test_meny_a.append(MenyValg(
        "Valg A4.",
        print,
        ("Kjører A4.",),
    ))
    test_meny_a.append(MenyValg(
        "B meny.",
        test_meny_b.show,
        (),
    ))
    test_meny_a.append(MenyValg(
        "Avslutt.",
        None,
        (),
    ))

    # DEBUG: _test_meny().
    if _debug_enabled:
        print(f"DEBUG: id(test_meny_a): {id(test_meny_a)}")
        print(f"DEBUG: id(test_meny_b): {id(test_meny_b)}")

    test_meny_b.append(MenyValg(
        "Valg B1.",
        print,
        ("Kjører B1.",),
    ))
    test_meny_b.append(MenyValg(
        "Valg B2.",
        print,
        ("Kjører B2.",),
    ))
    test_meny_b.append(MenyValg(
        "Valg B3.",
        print,
        ("Kjører B3.",),
    ))
    test_meny_b.append(MenyValg(
        "Valg B4.",
        print,
        ("Kjører B4.",),
    ))
    test_meny_b.append(MenyValg(
        "A meny.",
        test_meny_a.show,
        (),
    ))
    test_meny_b.append(MenyValg(
        "Avslutt.",
        None,
        (),
    ))

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


