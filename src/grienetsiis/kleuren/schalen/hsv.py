"""
grienetsiis.kleuren.schalen.hsv
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from ._invoer_naar_waardes import _invoer_naar_waardes


def kleur_schaal_hsv(
    start: HEX | HSL | HSV | CMYK | RGB,
    eind: HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    tint: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    verzadiging: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    waarde: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    alfa: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    ) -> List[HSV]:
    
    kleuren = []
    
    start = start.hsv
    eind = eind.hsv
    
    waardes_tint = _invoer_naar_waardes(
        start = start.tint,
        eind = eind.tint,
        kleur_invoer = tint,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_verzadiging = _invoer_naar_waardes(
        start = start.verzadiging,
        eind = eind.verzadiging,
        kleur_invoer = verzadiging,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_waarde = _invoer_naar_waardes(
        start = start.waarde,
        eind = eind.waarde,
        kleur_invoer = waarde,
        aantal_kleuren = aantal_kleuren,
        )
    waardes_alfa = _invoer_naar_waardes(
        start = start.alfa,
        eind = eind.alfa,
        kleur_invoer = alfa,
        aantal_kleuren = aantal_kleuren,
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