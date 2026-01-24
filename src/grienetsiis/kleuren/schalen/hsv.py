from typing import List

from grienetsiis.kleuren.codering import HSV


def kleur_schaal_hsva(
    start: HSV,
    eind: HSV,
    aantal_kleuren: int,
    ) -> List[HSV]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = HSV(
            tint = start.tint  * (1-ratio) + eind.tint  * ratio,
            verzadiging = start.verzadiging * (1-ratio) + eind.verzadiging * ratio,
            waarde = start.waarde * (1-ratio) + eind.waarde * ratio,
            alfa = start.alfa  * (1-ratio) + eind.alfa  * ratio,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_hsv(
    start: HSV,
    eind: HSV,
    aantal_kleuren: int,
    ) -> List[HSV]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = HSV(
            tint = start.tint  * (1-ratio) + eind.tint  * ratio,
            verzadiging = start.verzadiging * (1-ratio) + eind.verzadiging * ratio,
            waarde = start.waarde * (1-ratio) + eind.waarde * ratio,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_waarde(
    start: HSV,
    eind: HSV,
    aantal_kleuren: int,
    ) -> List[HSV]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = HSV(
            tint = start.tint,
            verzadiging = start.verzadiging,
            waarde = start.waarde * (1-ratio) + eind.waarde * ratio,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren