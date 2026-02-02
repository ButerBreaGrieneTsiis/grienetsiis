"""
grienetsiis.kleuren.schalen.hsv
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.kleur import Kleur
from grienetsiis.wiskunde.interpolatie import interpoleer


def kleur_schaal_hsv(
    start: Kleur | HEX | HSL | HSV | CMYK | RGB,
    eind: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    tint: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    verzadiging: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    waarde: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    alfa: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    ) -> List[HSV]:
    
    kleuren = []
    
    start = start.hsv
    eind = eind.hsv
    
    waardes_tint = interpoleer(
        start = start.tint,
        eind = eind.tint,
        methode = tint,
        aantal = aantal_kleuren,
        )
    waardes_verzadiging = interpoleer(
        start = start.verzadiging,
        eind = eind.verzadiging,
        methode = verzadiging,
        aantal = aantal_kleuren,
        )
    waardes_waarde = interpoleer(
        start = start.waarde,
        eind = eind.waarde,
        methode = waarde,
        aantal = aantal_kleuren,
        )
    waardes_alfa = interpoleer(
        start = start.alfa,
        eind = eind.alfa,
        methode = alfa,
        aantal = aantal_kleuren,
        )
    
    for (
        tint,
        verzadiging,
        waarde,
        alfa,
        ) in zip(
        waardes_tint,
        waardes_verzadiging,
        waardes_waarde,
        waardes_alfa,
        ):
        
        kleur = HSV(
            tint = tint,
            verzadiging = verzadiging,
            waarde = waarde,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren