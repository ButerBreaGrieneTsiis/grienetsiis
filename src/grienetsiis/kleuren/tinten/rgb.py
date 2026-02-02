"""
grienetsiis.kleuren.rooden.rgb
"""
from typing import List

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.kleur import Kleur
from grienetsiis.wiskunde.interpolatie import Interpolatie


def kleur_tint_rgb(
    grondkleur: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    rood: Interpolatie = Interpolatie.lineair(1.0, "max"),
    groen: Interpolatie = Interpolatie.lineair(1.0, "max"),
    blauw: Interpolatie = Interpolatie.lineair(1.0, "max"),
    alfa: Interpolatie = Interpolatie.lineair("min", "max"),
    ) -> List[RGB]:
    
    grondwaarde_rood = grondkleur.rgb.rood
    grondwaarde_groen = grondkleur.rgb.groen
    grondwaarde_blauw = grondkleur.rgb.blauw
    grondwaarde_alfa = grondkleur.rgb.alfa
    
    waardes_rood = rood.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_rood,
        waarde_min = 0,
        waarde_max = RGB.LIMIT_8BIT,
        )
    waardes_groen = groen.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_groen,
        waarde_min = 0,
        waarde_max = RGB.LIMIT_8BIT,
        )
    waardes_blauw = blauw.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_blauw,
        waarde_min = 0,
        waarde_max = RGB.LIMIT_8BIT,
        )
    waardes_alfa = alfa.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_alfa,
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    
    kleuren = []
    
    for (
        waarde_rood,
        waarde_groen,
        waarde_blauw,
        waarde_alfa,
        ) in zip(
            waardes_rood,
            waardes_groen,
            waardes_blauw,
            waardes_alfa,
        ):
        
        kleur = RGB(
            rood = waarde_rood,
            groen = waarde_groen,
            blauw = waarde_blauw,
            alfa = waarde_alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren