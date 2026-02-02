"""
grienetsiis.kleuren.palet
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.tinten import kleur_tint_hsv
from grienetsiis.wiskunde.interpolatie import Interpolatie


def palet_regenboog(
    aantal_kleuren: int,
    codering: Literal["hex", "hsl", "hsv", "cmyk", "rgb"] = "hex",
    helderheid: float = 1.0,
    ) -> List[HEX | HSL | HSV | CMYK | RGB]:
    
    grondkleur = HSV(
        tint = 0.0,
        verzadiging = 1.0,
        waarde = helderheid,
        )
    
    kleuren =  kleur_tint_hsv(
        grondkleur = grondkleur,
        aantal_kleuren = aantal_kleuren,
        tint = Interpolatie.lineair("min", "max"),
        verzadiging = Interpolatie.constant(1.0),
        waarde = Interpolatie.constant(1.0),
        )
    
    if codering == "hex":
        return [kleur.hex for kleur in kleuren]
    if codering == "hsl":
        return [kleur.hsl for kleur in kleuren]
    if codering == "hsv":
        return [kleur.hsv for kleur in kleuren]
    if codering == "cmyk":
        return [kleur.cmyk for kleur in kleuren]
    if codering == "rgb":
        return [kleur.rgb for kleur in kleuren]