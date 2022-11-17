"""Funksjon for å vise avtalelister og kategorilister."""

from typing import Any


_debug_enabled: bool = False


def vis_liste(
    liste: list[Any],
    overskrift: str | None = None,
) -> list[Any]:
    """Skriver ut en liste til skjermen.

    En liste er mutable. Vi bevarer id(liste).
    Det er ikke nødvendig å ta imot returverdien.
    id(liste) er identisk før og etter vis_liste().

    Args:
        liste: list[Any]
        overskrift: str | None = None

    Returns:
        liste: list[Any]

    Raises:
    """

    if overskrift is not None:
        print(overskrift)
    for i, item in enumerate(liste):
        print(f"[{i}]{item}")

    # DEBUG: vis_liste().
    if _debug_enabled:
        print(f"DEBUG: @vis_liste(): id(liste): "
              f"{id(liste)}")

    return liste


def _test_vis_liste() -> None:
    """Tester vis_liste().

    Args:

    Returns:

    Raises:
    """

    pass


if __name__ == "__main__":
    pass

    # TEST: vis_liste().
    #_test_vis_liste()


