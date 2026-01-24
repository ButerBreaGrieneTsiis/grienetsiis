from typing import Callable, List

from grienetsiis.kleuren.codering import HSV


def kleur_schaal_hsva(
    start: HSV,
    eind: HSV,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[HSV]:
    
    kleuren = []
    
    waardes_tint = interpolatie_func(start.tint, eind.tint, aantal_kleuren)
    waardes_verzadiging = interpolatie_func(start.verzadiging, eind.verzadiging, aantal_kleuren)
    waardes_waarde = interpolatie_func(start.waarde, eind.waarde, aantal_kleuren)
    waardes_alfa = interpolatie_func(start.alfa, eind.alfa, aantal_kleuren)
    
    for (
        tint,
        verzadiging,
        waarde,
        alfa,
        ) in zip(
        waardes_tint,
        waardes_verzadiging,
        waardes_waarde,
        waardes_alfa,
        ):
        
        kleur = HSV(
            tint = tint,
            verzadiging = verzadiging,
            waarde = waarde,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_hsv(
    start: HSV,
    eind: HSV,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[HSV]:
    
    kleuren = []
    
    waardes_tint = interpolatie_func(start.tint, eind.tint, aantal_kleuren)
    waardes_verzadiging = interpolatie_func(start.verzadiging, eind.verzadiging, aantal_kleuren)
    waardes_waarde = interpolatie_func(start.waarde, eind.waarde, aantal_kleuren)
    
    if constante == "start":
        alfa = start.alfa
    elif constante == "eind":
        alfa = eind.alfa
    elif constante == "gemiddeld":
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        tint,
        verzadiging,
        waarde,
        ) in zip(
        waardes_tint,
        waardes_verzadiging,
        waardes_waarde,
        ):
        
        kleur = HSV(
            tint = tint,
            verzadiging = verzadiging,
            waarde = waarde,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_waarde(
    start: HSV,
    eind: HSV,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[HSV]:
    
    kleuren = []
    
    waardes_waarde = interpolatie_func(start.waarde, eind.waarde, aantal_kleuren)
    
    if constante == "start":
        tint = start.tint
        verzadiging = start.verzadiging
        alfa = start.alfa
    elif constante == "eind":
        tint = eind.tint
        verzadiging = eind.verzadiging
        alfa = eind.alfa
    elif constante == "gemiddeld":
        tint = 0.5 * start.tint + 0.5 * eind.tint
        verzadiging = 0.5 * start.verzadiging + 0.5 * eind.verzadiging
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for waarde in waardes_waarde:
        
        kleur = HSV(
            tint = tint,
            verzadiging = verzadiging,
            waarde = waarde,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren