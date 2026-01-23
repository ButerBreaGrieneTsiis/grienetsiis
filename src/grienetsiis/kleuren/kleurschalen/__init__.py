from __future__ import annotations
from typing import List, Literal, TYPE_CHECKING

from .rgb import (
    kleur_schaal_rgba,
    kleur_schaal_rgb,
    kleur_schaal_rood,
    kleur_schaal_groen,
    kleur_schaal_blauw,
    )

if TYPE_CHECKING:
    from grienetsiis.kleuren.kleurcodering import HEX, HSL, HSV, CMYK, RGB
    from grienetsiis.kleuren.kleur import Kleur


SCHAAL_FUNCTIES = {
    "rgba": (kleur_schaal_rgba, "rgb"),
    "rgb": (kleur_schaal_rgb, "rgb"),
    "rood": (kleur_schaal_rood, "rgb"),
    "groen": (kleur_schaal_groen, "rgb"),
    "blauw": (kleur_schaal_blauw, "rgb"),
    }

def kleur_schaal(
    start: Kleur | HEX | HSL | HSV | CMYK | RGB,
    eind: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    schaal: Literal[
        "rgba",
        "rgb",
        "rood",
        "groen",
        "alfa",
        "blauw",
        "cyaan",
        "magneta",
        "geel",
        "zwart",
        "verzadiging",
        "tint",
        "helderheid",
        "waarde",
        ]
    ) -> List[RGB]:
    
    if schaal not in SCHAAL_FUNCTIES:
        raise ValueError("onbekende schaal \"{schaal}\"")
    
    return SCHAAL_FUNCTIES[schaal][0](
        start = getattr(start, SCHAAL_FUNCTIES[schaal][1]),
        eind = getattr(eind, SCHAAL_FUNCTIES[schaal][1]),
        aantal_kleuren = aantal_kleuren,
        )