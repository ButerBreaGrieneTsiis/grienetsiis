"""
grienetsiis.kleuren.schalen.hsl
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.kleur import Kleur
from grienetsiis.wiskunde.interpolatie import interpoleer


def kleur_schaal_hsl(
    start: Kleur | HEX | HSL | HSV | CMYK | RGB,
    eind: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    tint: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    verzadiging: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    helderheid: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    alfa: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float = "gemiddeld",
    ) -> List[HSL]:
    
    kleuren = []
    
    start = start.hsl
    eind = eind.hsl
    
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
    waardes_helderheid = interpoleer(
        start = start.helderheid,
        eind = eind.helderheid,
        methode = helderheid,
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