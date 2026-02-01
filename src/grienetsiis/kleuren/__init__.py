"""
grienetsiis.kleuren

grienetsiis.kleuren.codering
    achterliggende wiskundige classes voor de kleuren

grienetsiis.kleuren.schalen
    genereren van kleuren tussen twee kleuren
    op basis van interpolatiefuncties

grienetsiis.kleuren.tinten
    generen van kleuren op basis van één kleur
    op basis van schaalfactoren

grienetsiis.kleuren.palet
    vooraf ingestelde kleurentinten

"""
from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.palet import palet_regenboog
from grienetsiis.kleuren.schalen import kleur_schaal_hsl, kleur_schaal_hsv, kleur_schaal_cmyk, kleur_schaal_rgb
from grienetsiis.kleuren.tinten import kleur_tint_hsl, kleur_tint_hsv, kleur_tint_cmyk, kleur_tint_rgb
from grienetsiis.kleuren.kleur import Kleur


__all__ = [
    "HEX",
    "HSL",
    "HSV",
    "CMYK",
    "RGB",
    "palet_regenboog",
    "Kleur",
    "kleur_schaal_hsl",
    "kleur_schaal_hsv",
    "kleur_schaal_cmyk",
    "kleur_schaal_rgb",
    "kleur_tint_hsl",
    "kleur_tint_hsv",
    "kleur_tint_cmyk",
    "kleur_tint_rgb",
    ]