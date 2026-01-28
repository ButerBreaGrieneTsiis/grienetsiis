"""
grienetsiis.kleuren.schalen
"""
from __future__ import annotations
from typing import List, Literal, TYPE_CHECKING

from .rgb import (
    kleur_schaal_rgba,
    kleur_schaal_rgb,
    kleur_schaal_rood,
    kleur_schaal_groen,
    kleur_schaal_blauw,
    kleur_schaal_roodgroen,
    kleur_schaal_roodblauw,
    kleur_schaal_groenblauw,
    kleur_schaal_alfa,
    )
from .cmyk import (
    kleur_schaal_cmyka,
    kleur_schaal_cmyk,
    kleur_schaal_cmy,
    kleur_schaal_cyaan,
    kleur_schaal_magenta,
    kleur_schaal_geel,
    kleur_schaal_cyaanmagenta,
    kleur_schaal_cyaangeel,
    kleur_schaal_magentageel,
    kleur_schaal_zwart,
    )
from .hsl import (
    kleur_schaal_hsla,
    kleur_schaal_hsl,
    kleur_schaal_tint,
    kleur_schaal_verzadiging,
    kleur_schaal_helderheid,
    )
from .hsv import (
    kleur_schaal_hsva,
    kleur_schaal_hsv,
    kleur_schaal_waarde,
    )
from grienetsiis.wiskunde.interpolatie import (
    lineair,
    lineair_door_grenzen,
    logaritmisch,
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
    "roodgroen": (kleur_schaal_roodgroen, "rgb"),
    "roodblauw": (kleur_schaal_roodblauw, "rgb"),
    "groenblauw": (kleur_schaal_groenblauw, "rgb"),
    "alfa": (kleur_schaal_alfa, "rgb"),
    "cmyka": (kleur_schaal_cmyka, "cmyk"),
    "cmyk": (kleur_schaal_cmyk, "cmyk"),
    "cmy": (kleur_schaal_cmy, "cmyk"),
    "cyaan": (kleur_schaal_cyaan, "cmyk"),
    "magenta": (kleur_schaal_magenta, "cmyk"),
    "geel": (kleur_schaal_geel, "cmyk"),
    "cyaanmagenta": (kleur_schaal_cyaanmagenta, "cmyk"),
    "cyaangeel": (kleur_schaal_cyaangeel, "cmyk"),
    "magentageel": (kleur_schaal_magentageel, "cmyk"),
    "zwart": (kleur_schaal_zwart, "cmyk"),
    "hsla": (kleur_schaal_hsla, "hsl"),
    "hsl": (kleur_schaal_hsl, "hsl"),
    "tint": (kleur_schaal_tint, "hsl"),
    "verzadiging": (kleur_schaal_verzadiging, "hsl"),
    "helderheid": (kleur_schaal_helderheid, "hsl"),
    "hsva": (kleur_schaal_hsva, "hsv"),
    "hsv": (kleur_schaal_hsv, "hsv"),
    "waarde": (kleur_schaal_waarde, "hsv"),
    }
INTERPOLATIE_FUNCTIES = {
    "lineair": lineair,
    "lineair_omgekeerd": lineair_door_grenzen,
    "logaritmisch": logaritmisch,
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
        "roodgroen",
        "roodblauw",
        "groenblauw",
        "cmyka",
        "cmyk",
        "cmy",
        "cyaan",
        "magenta",
        "geel",
        "cyaanmagenta",
        "cyaangeel",
        "magentageel",
        "zwart",
        "hsla",
        "hsl",
        "verzadiging",
        "tint",
        "helderheid",
        "hsva",
        "hsv",
        "waarde",
        ] = "rgba",
    interpolatie: Literal[
        "lineair",
        "lineair_omgekeerd",
        ] = "lineair",
    constante: Literal[
        "start",
        "eind",
        "gemiddeld",
        ] = "start",
    ) -> List[HEX | HSL | HSV | CMYK | RGB]:
    
    if schaal not in SCHAAL_FUNCTIES:
        raise ValueError(f"onbekende schaal \"{schaal}\"")
    
    return SCHAAL_FUNCTIES[schaal][0](
        start = getattr(start, SCHAAL_FUNCTIES[schaal][1]),
        eind = getattr(eind, SCHAAL_FUNCTIES[schaal][1]),
        aantal_kleuren = aantal_kleuren,
        interpolatie_func = INTERPOLATIE_FUNCTIES[interpolatie],
        constante = constante,
        )