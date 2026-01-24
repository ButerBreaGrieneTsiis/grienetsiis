from typing import List

from grienetsiis.kleuren.codering import HSL


def kleur_schaal_hsla(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    ) -> List[HSL]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = HSL(
            tint = start.tint  * (1-ratio) + eind.tint  * ratio,
            verzadiging = start.verzadiging * (1-ratio) + eind.verzadiging * ratio,
            helderheid = start.helderheid * (1-ratio) + eind.helderheid * ratio,
            alfa = start.alfa  * (1-ratio) + eind.alfa  * ratio,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_hsl(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    ) -> List[HSL]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = HSL(
            tint = start.tint  * (1-ratio) + eind.tint  * ratio,
            verzadiging = start.verzadiging * (1-ratio) + eind.verzadiging * ratio,
            helderheid = start.helderheid * (1-ratio) + eind.helderheid * ratio,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_tint(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    ) -> List[HSL]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = HSL(
            tint = start.tint  * (1-ratio) + eind.tint  * ratio,
            verzadiging = start.verzadiging,
            helderheid = start.helderheid,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_verzadiging(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    ) -> List[HSL]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = HSL(
            tint = start.tint,
            verzadiging = start.verzadiging * (1-ratio) + eind.verzadiging * ratio,
            helderheid = start.helderheid,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_helderheid(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    ) -> List[HSL]:
    
    kleuren = []
    
    for index_kleur in range(aantal_kleuren):
        
        ratio = index_kleur / (aantal_kleuren - 1)
        kleur = HSL(
            tint = start.tint,
            verzadiging = start.verzadiging,
            helderheid = start.helderheid * (1-ratio) + eind.helderheid * ratio,
            alfa = start.alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren