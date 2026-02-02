"""
grienetsiis.kleuren.schalen
"""
from .hsl import kleur_schaal_hsl
from .hsv import kleur_schaal_hsv
from .cmyk import kleur_schaal_cmyk
from .rgb import kleur_schaal_rgb


__all__ = [
    "kleur_schaal_hsl",
    "kleur_schaal_hsv",
    "kleur_schaal_cmyk",
    "kleur_schaal_rgb",
    ]