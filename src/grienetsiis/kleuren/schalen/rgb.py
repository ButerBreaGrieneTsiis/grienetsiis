"""
grienetsiis.kleuren.schalen.rgb
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from ._invoer_naar_waardes import _invoer_naar_waardes


def kleur_schaal_rgb(
    start: HEX | HSL | HSV | CMYK | RGB,
    eind: HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    rood: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    groen: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    blauw: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    alfa: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    ) -> List[RGB]:
    
    kleuren = []
    
    start = start.rgb
    eind = eind.rgb
    
    waardes_rood = _invoer_naar_waardes(
        start = start.rood/RGB.LIMIT_8BIT,
        eind = eind.rood/RGB.LIMIT_8BIT,
        kleur_invoer = rood,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_groen = _invoer_naar_waardes(
        start = start.groen/RGB.LIMIT_8BIT,
        eind = eind.groen/RGB.LIMIT_8BIT,
        kleur_invoer = groen,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_blauw = _invoer_naar_waardes(
        start = start.blauw/RGB.LIMIT_8BIT,
        eind = eind.blauw/RGB.LIMIT_8BIT,
        kleur_invoer = blauw,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_alfa = _invoer_naar_waardes(
        start = start.alfa,
        eind = eind.alfa,
        kleur_invoer = alfa,
        aantal_kleuren = aantal_kleuren,
        )
    
    for (
        rood,
        groen,
        blauw,
        alfa,
        ) in zip(
        waardes_rood,
        waardes_groen,
        waardes_blauw,
        waardes_alfa,
        ):
        
        kleur = RGB(
            rood = rood * RGB.LIMIT_8BIT,
            groen = groen * RGB.LIMIT_8BIT,
            blauw = blauw * RGB.LIMIT_8BIT,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren