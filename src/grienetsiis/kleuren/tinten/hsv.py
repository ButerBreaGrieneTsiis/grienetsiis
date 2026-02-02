"""
grienetsiis.kleuren.tinten.hsv
"""
from typing import List

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.kleur import Kleur
from grienetsiis.wiskunde.interpolatie import Interpolatie


def kleur_tint_hsv(
    grondkleur: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    tint: Interpolatie = Interpolatie.lineair(1.0, "max"),
    verzadiging: Interpolatie = Interpolatie.lineair(1.0, "max"),
    waarde: Interpolatie = Interpolatie.lineair(1.0, "max"),
    alfa: Interpolatie = Interpolatie.lineair("min", "max"),
    ) -> List[HSV]:
    
    grondwaarde_tint = grondkleur.hsv.tint
    grondwaarde_verzadiging = grondkleur.hsv.verzadiging
    grondwaarde_waarde = grondkleur.hsv.waarde
    grondwaarde_alfa = grondkleur.hsv.alfa
    
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
    waardes_waarde = waarde.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_waarde,
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
        waarde_waarde,
        waarde_alfa,
        ) in zip(
            waardes_tint,
            waardes_verzadiging,
            waardes_waarde,
            waardes_alfa,
        ):
        
        kleur = HSV(
            tint = waarde_tint,
            verzadiging = waarde_verzadiging,
            waarde = waarde_waarde,
            alfa = waarde_alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren