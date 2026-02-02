"""
grienetsiis.kleuren.cyaanen.cmyk
"""
from typing import List

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.kleur import Kleur
from grienetsiis.wiskunde.interpolatie import Interpolatie


def kleur_tint_cmyk(
    grondkleur: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    cyaan: Interpolatie = Interpolatie.lineair(1.0, "max"),
    magenta: Interpolatie = Interpolatie.lineair(1.0, "max"),
    geel: Interpolatie = Interpolatie.lineair(1.0, "max"),
    zwart: Interpolatie = Interpolatie.lineair(1.0, "max"),
    alfa: Interpolatie = Interpolatie.lineair("min", "max"),
    ) -> List[CMYK]:
    
    grondwaarde_cyaan = grondkleur.cmyk.cyaan
    grondwaarde_magenta = grondkleur.cmyk.magenta
    grondwaarde_geel = grondkleur.cmyk.geel
    grondwaarde_zwart = grondkleur.cmyk.zwart
    grondwaarde_alfa = grondkleur.cmyk.alfa
    
    waardes_cyaan = cyaan.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_cyaan,
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_magenta = magenta.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_magenta,
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_geel = geel.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_geel,
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_zwart = zwart.toepassen(
        aantal = aantal_kleuren,
        waarde = grondwaarde_zwart,
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
        waarde_cyaan,
        waarde_magenta,
        waarde_geel,
        waarde_zwart,
        waarde_alfa,
        ) in zip(
            waardes_cyaan,
            waardes_magenta,
            waardes_geel,
            waardes_zwart,
            waardes_alfa,
        ):
        
        kleur = CMYK(
            cyaan = waarde_cyaan,
            magenta = waarde_magenta,
            geel = waarde_geel,
            zwart = waarde_zwart,
            alfa = waarde_alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren