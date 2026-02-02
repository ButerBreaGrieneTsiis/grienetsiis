"""
grienetsiis.kleuren.schalen.rgb
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.wiskunde.interpolatie import interpoleer


def kleur_schaal_rgb(
    start: HEX | HSL | HSV | CMYK | RGB,
    eind: HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    rood: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    groen: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    blauw: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    alfa: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    ) -> List[RGB]:
    
    kleuren = []
    
    start = start.rgb
    eind = eind.rgb
    
    waardes_rood = interpoleer(
        start = start.rood/RGB.LIMIT_8BIT,
        eind = eind.rood/RGB.LIMIT_8BIT,
        methode = rood,
        aantal = aantal_kleuren,
        )
    waardes_groen = interpoleer(
        start = start.groen/RGB.LIMIT_8BIT,
        eind = eind.groen/RGB.LIMIT_8BIT,
        methode = groen,
        aantal = aantal_kleuren,
        )
    waardes_blauw = interpoleer(
        start = start.blauw/RGB.LIMIT_8BIT,
        eind = eind.blauw/RGB.LIMIT_8BIT,
        methode = blauw,
        aantal = aantal_kleuren,
        )
    waardes_alfa = interpoleer(
        start = start.alfa,
        eind = eind.alfa,
        methode = alfa,
        aantal = aantal_kleuren,
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