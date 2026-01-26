from typing import Callable, List

from grienetsiis.kleuren.codering import CMYK


def kleur_schaal_cmyka(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_cyaan = interpolatie_func(start.cyaan, eind.cyaan, aantal_kleuren)
    waardes_magenta = interpolatie_func(start.magenta, eind.magenta, aantal_kleuren)
    waardes_geel = interpolatie_func(start.geel, eind.geel, aantal_kleuren)
    waardes_zwart = interpolatie_func(start.zwart, eind.zwart, aantal_kleuren)
    waardes_alfa = interpolatie_func(start.alfa, eind.alfa, aantal_kleuren)
    
    for (
        cyaan,
        magenta,
        geel,
        zwart,
        alfa,
        ) in zip(
        waardes_cyaan,
        waardes_magenta,
        waardes_geel,
        waardes_zwart,
        waardes_alfa,
        ):
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_cmyk(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_cyaan = interpolatie_func(start.cyaan, eind.cyaan, aantal_kleuren)
    waardes_magenta = interpolatie_func(start.magenta, eind.magenta, aantal_kleuren)
    waardes_geel = interpolatie_func(start.geel, eind.geel, aantal_kleuren)
    waardes_zwart = interpolatie_func(start.zwart, eind.zwart, aantal_kleuren)
    
    if constante == "start":
        alfa = start.alfa
    elif constante == "eind":
        alfa = eind.alfa
    elif constante == "gemiddeld":
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        cyaan,
        magenta,
        geel,
        zwart,
        ) in zip(
        waardes_cyaan,
        waardes_magenta,
        waardes_geel,
        waardes_zwart,
        ):
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_cmy(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_cyaan = interpolatie_func(start.cyaan, eind.cyaan, aantal_kleuren)
    waardes_magenta = interpolatie_func(start.magenta, eind.magenta, aantal_kleuren)
    waardes_geel = interpolatie_func(start.geel, eind.geel, aantal_kleuren)
    
    if constante == "start":
        zwart = start.zwart
        alfa = start.alfa
    elif constante == "eind":
        zwart = eind.zwart
        alfa = eind.alfa
    elif constante == "gemiddeld":
        zwart = 0.5 * start.zwart + 0.5 * eind.zwart
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        cyaan,
        magenta,
        geel,
        ) in zip(
        waardes_cyaan,
        waardes_magenta,
        waardes_geel,
        ):
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_cyaan(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_cyaan = interpolatie_func(start.cyaan, eind.cyaan, aantal_kleuren)
    
    if constante == "start":
        magenta = start.magenta
        geel = start.geel
        zwart = start.zwart
        alfa = start.alfa
    elif constante == "eind":
        magenta = eind.magenta
        geel = eind.geel
        zwart = eind.zwart
        alfa = eind.alfa
    elif constante == "gemiddeld":
        magenta = 0.5 * start.magenta + 0.5 * eind.magenta
        geel = 0.5 * start.geel + 0.5 * eind.geel
        zwart = 0.5 * start.zwart + 0.5 * eind.zwart
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for cyaan in waardes_cyaan:
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_magenta(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_magenta = interpolatie_func(start.magenta, eind.magenta, aantal_kleuren)
    
    if constante == "start":
        cyaan = start.cyaan
        geel = start.geel
        zwart = start.zwart
        alfa = start.alfa
    elif constante == "eind":
        cyaan = eind.cyaan
        geel = eind.geel
        zwart = eind.zwart
        alfa = eind.alfa
    elif constante == "gemiddeld":
        cyaan = 0.5 * start.cyaan + 0.5 * eind.cyaan
        geel = 0.5 * start.geel + 0.5 * eind.geel
        zwart = 0.5 * start.zwart + 0.5 * eind.zwart
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for magenta in waardes_magenta:
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_geel(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_geel = interpolatie_func(start.geel, eind.geel, aantal_kleuren)
    
    if constante == "start":
        cyaan = start.cyaan
        magenta = start.magenta
        zwart = start.zwart
        alfa = start.alfa
    elif constante == "eind":
        cyaan = eind.cyaan
        magenta = eind.magenta
        zwart = eind.zwart
        alfa = eind.alfa
    elif constante == "gemiddeld":
        cyaan = 0.5 * start.cyaan + 0.5 * eind.cyaan
        magenta = 0.5 * start.magenta + 0.5 * eind.magenta
        zwart = 0.5 * start.zwart + 0.5 * eind.zwart
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for geel in waardes_geel:
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_cyaanmagenta(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_cyaan = interpolatie_func(start.cyaan, eind.cyaan, aantal_kleuren)
    waardes_magenta = interpolatie_func(start.magenta, eind.magenta, aantal_kleuren)
    
    if constante == "start":
        geel = start.geel
        zwart = start.zwart
        alfa = start.alfa
    elif constante == "eind":
        geel = eind.geel
        zwart = eind.zwart
        alfa = eind.alfa
    elif constante == "gemiddeld":
        geel = 0.5 * start.geel + 0.5 * eind.geel
        zwart = 0.5 * start.zwart + 0.5 * eind.zwart
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        cyaan,
        magenta,
        ) in zip(
        waardes_cyaan,
        waardes_magenta,
        ):
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_cyaangeel(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_cyaan = interpolatie_func(start.cyaan, eind.cyaan, aantal_kleuren)
    waardes_geel = interpolatie_func(start.geel, eind.geel, aantal_kleuren)
    
    if constante == "start":
        magenta = start.magenta
        zwart = start.zwart
        alfa = start.alfa
    elif constante == "eind":
        magenta = eind.magenta
        zwart = eind.zwart
        alfa = eind.alfa
    elif constante == "gemiddeld":
        magenta = 0.5 * start.magenta + 0.5 * eind.magenta
        zwart = 0.5 * start.zwart + 0.5 * eind.zwart
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        cyaan,
        geel,
        ) in zip(
        waardes_cyaan,
        waardes_geel,
        ):
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_magentageel(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_magenta = interpolatie_func(start.magenta, eind.magenta, aantal_kleuren)
    waardes_geel = interpolatie_func(start.geel, eind.geel, aantal_kleuren)
    
    if constante == "start":
        cyaan = start.cyaan
        zwart = start.zwart
        alfa = start.alfa
    elif constante == "eind":
        cyaan = eind.cyaan
        zwart = eind.zwart
        alfa = eind.alfa
    elif constante == "gemiddeld":
        cyaan = 0.5 * start.cyaan + 0.5 * eind.cyaan
        zwart = 0.5 * start.zwart + 0.5 * eind.zwart
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        magenta,
        geel,
        ) in zip(
        waardes_magenta,
        waardes_geel,
        ):
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_zwart(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[CMYK]:
    
    kleuren = []
    
    waardes_zwart = interpolatie_func(start.zwart, eind.zwart, aantal_kleuren)
    
    if constante == "start":
        cyaan = start.cyaan
        magenta = start.magenta
        geel = start.geel
        alfa = start.alfa
    elif constante == "eind":
        cyaan = eind.cyaan
        magenta = eind.magenta
        geel = eind.geel
        alfa = eind.alfa
    elif constante == "gemiddeld":
        cyaan = 0.5 * start.cyaan + 0.5 * eind.cyaan
        magenta = 0.5 * start.magenta + 0.5 * eind.magenta
        geel = 0.5 * start.geel + 0.5 * eind.geel
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for zwart in waardes_zwart:
        
        kleur = CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren