from __future__ import annotations
from typing import List, Literal, TYPE_CHECKING

from .rgb import (
    kleur_schaal_rgba,
    kleur_schaal_rgb,
    kleur_schaal_rood,
    kleur_schaal_groen,
    kleur_schaal_blauw,
    )
from .cmyk import (
    kleur_schaal_cmyka,
    kleur_schaal_cmyk,
    kleur_schaal_cmy,
    kleur_schaal_cyaan,
    kleur_schaal_magenta,
    kleur_schaal_geel,
    kleur_schaal_zwart,
    )

if TYPE_CHECKING:
    from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
    from grienetsiis.kleuren.kleur import Kleur


SCHAAL_FUNCTIES = {
    "rgba": (kleur_schaal_rgba, "rgb"),
    "rgb": (kleur_schaal_rgb, "rgb"),
    "rood": (kleur_schaal_rood, "rgb"),
    "groen": (kleur_schaal_groen, "rgb"),
    "blauw": (kleur_schaal_blauw, "rgb"),
    "cmyka": (kleur_schaal_cmyka, "cmyk"),
    "cmyk": (kleur_schaal_cmyk, "cmyk"),
    "cmy": (kleur_schaal_cmy, "cmyk"),
    "cyaan": (kleur_schaal_cyaan, "cmyk"),
    "magenta": (kleur_schaal_magenta, "cmyk"),
    "geel": (kleur_schaal_geel, "cmyk"),
    "zwart": (kleur_schaal_zwart, "cmyk"),
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
        "cmyka",
        "cmyk",
        "cmy",
        "cyaan",
        "magenta",
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