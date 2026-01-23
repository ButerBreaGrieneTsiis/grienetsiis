from typing import List

from grienetsiis.kleuren.kleurcodering import RGB


def kleur_schaal_rgba(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    ) -> List[RGB]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = RGB(
            rood = start.rood  * (1-ratio) + eind.rood  * ratio,
            groen = start.groen * (1-ratio) + eind.groen * ratio,
            blauw = start.blauw * (1-ratio) + eind.blauw * ratio,
            alfa = start.alfa  * (1-ratio) + eind.alfa  * ratio,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_rgb(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    ) -> List[RGB]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = RGB(
            rood = start.rood  * (1-ratio) + eind.rood  * ratio,
            groen = start.groen * (1-ratio) + eind.groen * ratio,
            blauw = start.blauw * (1-ratio) + eind.blauw * ratio,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_rood(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    ) -> List[RGB]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = RGB(
            rood = start.rood  * (1-ratio) + eind.rood  * ratio,
            groen = start.groen,
            blauw = start.blauw,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_groen(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    ) -> List[RGB]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = RGB(
            rood = start.rood,
            groen = start.groen * (1-ratio) + eind.groen * ratio,
            blauw = start.blauw,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_blauw(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    ) -> List[RGB]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = RGB(
            rood = start.rood,
            groen = start.groen,
            blauw = start.blauw * (1-ratio) + eind.blauw * ratio,
            )
        
        kleuren.append(kleur)
    
    return kleuren