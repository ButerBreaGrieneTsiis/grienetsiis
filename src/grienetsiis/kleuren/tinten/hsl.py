"""
grienetsiis.kleuren.tinten.hsl
"""
from typing import List

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.kleur import Kleur
from grienetsiis.wiskunde.interpolatie import Interpolatie


def kleur_tint_hsl(
    grondkleur: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    tint: Interpolatie = Interpolatie.lineair(1.0, "max"),
    verzadiging: Interpolatie = Interpolatie.lineair(1.0, "max"),
    helderheid: Interpolatie = Interpolatie.lineair(1.0, "max"),
    alfa: Interpolatie = Interpolatie.lineair("min", "max"),
    ) -> List[HSL]:
    
    grondwaarde_tint = grondkleur.hsl.tint
    grondwaarde_verzadiging = grondkleur.hsl.verzadiging
    grondwaarde_helderheid = grondkleur.hsl.helderheid
    grondwaarde_alfa = grondkleur.hsl.alfa
    
    waardes_tint = tint.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_tint,
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_verzadiging = verzadiging.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_verzadiging,
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_helderheid = helderheid.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_helderheid,
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_alfa = alfa.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_alfa,
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    
    kleuren = []
    
    for (
        waarde_tint,
        waarde_verzadiging,
        waarde_helderheid,
        waarde_alfa,
        ) in zip(
            waardes_tint,
            waardes_verzadiging,
            waardes_helderheid,
            waardes_alfa,
        ):
        
        kleur = HSL(
            tint = waarde_tint,
            verzadiging = waarde_verzadiging,
            helderheid = waarde_helderheid,
            alfa = waarde_alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren