"""
grienetsiis.kleuren
"""
from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.schalen import kleur_schaal
from grienetsiis.kleuren.tinten import kleur_tint_hsl, kleur_tint_hsv, kleur_tint_cmyk, kleur_tint_rgb
from grienetsiis.kleuren.kleur import Kleur


__all__ = [
    "HEX",
    "HSL",
    "HSV",
    "CMYK",
    "RGB",
    "Kleur",
    "kleur_schaal",
    "kleur_tint_hsl",
    "kleur_tint_hsv",
    "kleur_tint_cmyk",
    "kleur_tint_rgb",
    ]