"""
grienetsiis.kleuren.tinten
"""
from __future__ import annotations
from typing import List, Literal, Tuple, TYPE_CHECKING

from grienetsiis.kleuren.codering import HSL, HSV, CMYK, RGB
from grienetsiis.wiskunde.interpolatie import lineair, logaritmisch

if TYPE_CHECKING:
    from grienetsiis.kleuren.codering import HEX
    from grienetsiis.kleuren.kleur import Kleur


# https://graphicdesign.stackexchange.com/questions/75417/how-to-make-a-given-color-a-bit-darker-or-lighter/75419#75419
# https://stackoverflow.com/questions/5560248/programmatically-lighten-or-darken-a-hex-color-or-rgb-and-blend-colors
def schaalfactoren(
    waarde: float,
    aantal: int,
    schaalfactor_start: float | Literal["min", "max"],
    schaalfactor_eind: float | Literal["min", "max"],
    waarde_min: float,
    waarde_max: float,
    ) -> List[float]:
    
    if schaalfactor_start == "min":
        waarde_start = waarde_min
    elif schaalfactor_start == "max":
        waarde_start = waarde_max
    else:
        waarde_start = schaalfactor_start * waarde
    
    if schaalfactor_eind == "min":
        waarde_eind = waarde_min
    elif schaalfactor_eind == "max":
        waarde_eind = waarde_max
    else:
        waarde_eind = schaalfactor_eind * waarde
    
    schaalfactoren = []
    
    for kleur_nummer in range(aantal):
        schaalfactor = waarde_start + (waarde_eind - waarde_start)/(aantal - 1) * kleur_nummer
        
        schaalfactor = min(max(schaalfactor, waarde_min), waarde_max)
        
        schaalfactoren.append(schaalfactor)
    
    return schaalfactoren

def kleur_tint_hsl(
    grondkleur: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    schaal_tint: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_verzadiging: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_helderheid: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_alfa: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    ) -> List[HSL]:
    
    grondkleur_tint = grondkleur.hsl.tint
    grondkleur_verzadiging = grondkleur.hsl.verzadiging
    grondkleur_helderheid = grondkleur.hsl.helderheid
    grondkleur_alfa = grondkleur.hsl.alfa
    
    waardes_tint = schaalfactoren(
        waarde = grondkleur_tint,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_tint[0],
        schaalfactor_eind = schaal_tint[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_verzadiging = schaalfactoren(
        waarde = grondkleur_verzadiging,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_verzadiging[0],
        schaalfactor_eind = schaal_verzadiging[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_helderheid = schaalfactoren(
        waarde = grondkleur_helderheid,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_helderheid[0],
        schaalfactor_eind = schaal_helderheid[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_alfa = schaalfactoren(
        waarde = grondkleur_alfa,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_alfa[0],
        schaalfactor_eind = schaal_alfa[1],
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

def kleur_tint_hsv(
    grondkleur: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    schaal_tint: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_verzadiging: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_waarde: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_alfa: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    ) -> List[HSV]:
    
    grondkleur_tint = grondkleur.hsv.tint
    grondkleur_verzadiging = grondkleur.hsv.verzadiging
    grondkleur_waarde = grondkleur.hsv.waarde
    grondkleur_alfa = grondkleur.hsv.alfa
    
    waardes_tint = schaalfactoren(
        waarde = grondkleur_tint,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_tint[0],
        schaalfactor_eind = schaal_tint[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_verzadiging = schaalfactoren(
        waarde = grondkleur_verzadiging,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_verzadiging[0],
        schaalfactor_eind = schaal_verzadiging[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_waarde = schaalfactoren(
        waarde = grondkleur_waarde,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_waarde[0],
        schaalfactor_eind = schaal_waarde[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_alfa = schaalfactoren(
        waarde = grondkleur_alfa,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_alfa[0],
        schaalfactor_eind = schaal_alfa[1],
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

def kleur_tint_cmyk(
    grondkleur: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    schaal_cyaan: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_magenta: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_geel: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_zwart: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_alfa: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    ) -> List[CMYK]:
    
    grondkleur_cyaan = grondkleur.cmyk.cyaan
    grondkleur_magenta = grondkleur.cmyk.magenta
    grondkleur_geel = grondkleur.cmyk.geel
    grondkleur_zwart = grondkleur.cmyk.zwart
    grondkleur_alfa = grondkleur.cmyk.alfa
    
    waardes_cyaan = schaalfactoren(
        waarde = grondkleur_cyaan,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_cyaan[0],
        schaalfactor_eind = schaal_cyaan[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_magenta = schaalfactoren(
        waarde = grondkleur_magenta,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_magenta[0],
        schaalfactor_eind = schaal_magenta[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_geel = schaalfactoren(
        waarde = grondkleur_geel,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_geel[0],
        schaalfactor_eind = schaal_geel[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_zwart = schaalfactoren(
        waarde = grondkleur_zwart,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_zwart[0],
        schaalfactor_eind = schaal_zwart[1],
        waarde_min = 0.0,
        waarde_max = 1.0,
        )
    waardes_alfa = schaalfactoren(
        waarde = grondkleur_alfa,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_alfa[0],
        schaalfactor_eind = schaal_alfa[1],
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

def kleur_tint_rgb(
    grondkleur: Kleur | HEX | HSL | HSV | CMYK | RGB,
    aantal_kleuren: int,
    schaal_rood: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_groen: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_blauw: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    schaal_alfa: Tuple[float | Literal["min", "max"], float | Literal["min", "max"]] = (1.0, "max"),
    ) -> List[RGB]:
    
    grondkleur_rood = grondkleur.rgb.rood
    grondkleur_groen = grondkleur.rgb.groen
    grondkleur_blauw = grondkleur.rgb.blauw
    grondkleur_alfa = grondkleur.rgb.alfa
    
    waardes_rood = schaalfactoren(
        waarde = grondkleur_rood,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_rood[0],
        schaalfactor_eind = schaal_rood[1],
        waarde_min = 0,
        waarde_max = RGB.LIMIT_8BIT,
        )
    waardes_groen = schaalfactoren(
        waarde = grondkleur_groen,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_groen[0],
        schaalfactor_eind = schaal_groen[1],
        waarde_min = 0,
        waarde_max = RGB.LIMIT_8BIT,
        )
    waardes_blauw = schaalfactoren(
        waarde = grondkleur_blauw,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_blauw[0],
        schaalfactor_eind = schaal_blauw[1],
        waarde_min = 0,
        waarde_max = RGB.LIMIT_8BIT,
        )
    waardes_alfa = schaalfactoren(
        waarde = grondkleur_alfa,
        aantal = aantal_kleuren,
        schaalfactor_start = schaal_alfa[0],
        schaalfactor_eind = schaal_alfa[1],
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