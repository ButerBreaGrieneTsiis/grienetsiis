"""
grienetsiis.kleuren.schalen.cmyk
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from ._invoer_naar_waardes import _invoer_naar_waardes


def kleur_schaal_cmyk(
    start: HEX | HSL | HSV | CMYK | RGB,
    eind: HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    cyaan: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    magenta: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    geel: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    zwart: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    alfa: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    ) -> List[CMYK]:
    
    kleuren = []
    
    start = start.cmyk
    eind = eind.cmyk
    
    waardes_cyaan = _invoer_naar_waardes(
        start = start.cyaan,
        eind = eind.cyaan,
        kleur_invoer = cyaan,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_magenta = _invoer_naar_waardes(
        start = start.magenta,
        eind = eind.magenta,
        kleur_invoer = magenta,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_geel = _invoer_naar_waardes(
        start = start.geel,
        eind = eind.geel,
        kleur_invoer = geel,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_zwart = _invoer_naar_waardes(
        start = start.zwart,
        eind = eind.zwart,
        kleur_invoer = zwart,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_alfa = _invoer_naar_waardes(
        start = start.alfa,
        eind = eind.alfa,
        kleur_invoer = alfa,
        aantal_kleuren = aantal_kleuren,
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