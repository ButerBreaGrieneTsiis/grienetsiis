from typing import List

from grienetsiis.kleuren.kleurcodering import CMYK


def kleur_schaal_cmyka(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    ) -> List[CMYK]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = CMYK(
            cyaan = start.cyaan  * (1-ratio) + eind.cyaan  * ratio,
            magenta = start.magenta * (1-ratio) + eind.magenta * ratio,
            geel = start.geel * (1-ratio) + eind.geel * ratio,
            zwart = start.zwart  * (1-ratio) + eind.zwart  * ratio,
            alfa = start.alfa  * (1-ratio) + eind.alfa  * ratio,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_cmyk(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    ) -> List[CMYK]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = CMYK(
            cyaan = start.cyaan  * (1-ratio) + eind.cyaan  * ratio,
            magenta = start.magenta * (1-ratio) + eind.magenta * ratio,
            geel = start.geel * (1-ratio) + eind.geel * ratio,
            zwart = start.zwart  * (1-ratio) + eind.zwart  * ratio,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_cmy(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    ) -> List[CMYK]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = CMYK(
            cyaan = start.cyaan  * (1-ratio) + eind.cyaan  * ratio,
            magenta = start.magenta * (1-ratio) + eind.magenta * ratio,
            geel = start.geel * (1-ratio) + eind.geel * ratio,
            zwart = start.zwart,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_cyaan(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    ) -> List[CMYK]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = CMYK(
            cyaan = start.cyaan  * (1-ratio) + eind.cyaan  * ratio,
            magenta = start.magenta,
            geel = start.geel,
            zwart = start.zwart,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_magenta(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    ) -> List[CMYK]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = CMYK(
            cyaan = start.cyaan,
            magenta = start.magenta * (1-ratio) + eind.magenta * ratio,
            geel = start.geel,
            zwart = start.zwart,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_geel(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    ) -> List[CMYK]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = CMYK(
            cyaan = start.cyaan,
            magenta = start.magenta,
            geel = start.geel * (1-ratio) + eind.geel * ratio,
            zwart = start.zwart,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_zwart(
    start: CMYK,
    eind: CMYK,
    aantal_kleuren: int,
    ) -> List[CMYK]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = CMYK(
            cyaan = start.cyaan,
            magenta = start.magenta,
            geel = start.geel,
            zwart = start.zwart  * (1-ratio) + eind.zwart  * ratio,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren