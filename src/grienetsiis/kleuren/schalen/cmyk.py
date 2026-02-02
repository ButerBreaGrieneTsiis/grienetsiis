"""
grienetsiis.kleuren.schalen.cmyk
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.kleur import Kleur
from grienetsiis.wiskunde.interpolatie import interpoleer


def kleur_schaal_cmyk(
    start: Kleur | HEX | HSL | HSV | CMYK | RGB,
    eind: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    cyaan: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    magenta: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    geel: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    zwart: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    alfa: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    ) -> List[CMYK]:
    
    kleuren = []
    
    start = start.cmyk
    eind = eind.cmyk
    
    waardes_cyaan = interpoleer(
        start = start.cyaan,
        eind = eind.cyaan,
        methode = cyaan,
        aantal = aantal_kleuren,
        )
    waardes_magenta = interpoleer(
        start = start.magenta,
        eind = eind.magenta,
        methode = magenta,
        aantal = aantal_kleuren,
        )
    waardes_geel = interpoleer(
        start = start.geel,
        eind = eind.geel,
        methode = geel,
        aantal = aantal_kleuren,
        )
    waardes_zwart = interpoleer(
        start = start.zwart,
        eind = eind.zwart,
        methode = zwart,
        aantal = aantal_kleuren,
        )
    waardes_alfa = interpoleer(
        start = start.alfa,
        eind = eind.alfa,
        methode = alfa,
        aantal = aantal_kleuren,
        )
    
    for (
        cyaan,
        magenta,
        geel,
        zwart,
        alfa,
        ) in zip(
        waardes_cyaan,
        waardes_magenta,
        waardes_geel,
        waardes_zwart,
        waardes_alfa,
        ):
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren