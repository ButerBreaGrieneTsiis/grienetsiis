"""
grienetsiis.kleuren.schalen.hsl
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from ._invoer_naar_waardes import _invoer_naar_waardes


def kleur_schaal_hsl(
    start: HEX | HSL | HSV | CMYK | RGB,
    eind: HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    tint: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    verzadiging: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    helderheid: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    alfa: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    ) -> List[HSL]:
    
    kleuren = []
    
    start = start.hsl
    eind = eind.hsl
    
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
    waardes_helderheid = _invoer_naar_waardes(
        start = start.helderheid,
        eind = eind.helderheid,
        kleur_invoer = helderheid,
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
        helderheid,
        alfa,
        ) in zip(
        waardes_tint,
        waardes_verzadiging,
        waardes_helderheid,
        waardes_alfa,
        ):
        
        kleur = HSL(
            tint = tint,
            verzadiging = verzadiging,
            helderheid = helderheid,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren