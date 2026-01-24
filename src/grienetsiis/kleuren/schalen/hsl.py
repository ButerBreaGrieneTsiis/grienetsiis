from typing import Callable, List

from grienetsiis.kleuren.codering import HSL


def kleur_schaal_hsla(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[HSL]:
    
    kleuren = []
    
    waardes_tint = interpolatie_func(start.tint, eind.tint, aantal_kleuren)
    waardes_verzadiging = interpolatie_func(start.verzadiging, eind.verzadiging, aantal_kleuren)
    waardes_helderheid = interpolatie_func(start.helderheid, eind.helderheid, aantal_kleuren)
    waardes_alfa = interpolatie_func(start.alfa, eind.alfa, aantal_kleuren)
    
    for (
        tint,
        verzadiging,
        helderheid,
        alfa,
        ) in zip(
        waardes_tint,
        waardes_verzadiging,
        waardes_helderheid,
        waardes_alfa,
        ):
        
        kleur = HSL(
            tint = tint,
            verzadiging = verzadiging,
            helderheid = helderheid,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_hsl(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[HSL]:
    
    kleuren = []
    
    waardes_tint = interpolatie_func(start.tint, eind.tint, aantal_kleuren)
    waardes_verzadiging = interpolatie_func(start.verzadiging, eind.verzadiging, aantal_kleuren)
    waardes_helderheid = interpolatie_func(start.helderheid, eind.helderheid, aantal_kleuren)
    
    if constante == "start":
        alfa = start.alfa
    elif constante == "eind":
        alfa = eind.alfa
    elif constante == "gemiddeld":
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        tint,
        verzadiging,
        helderheid,
        ) in zip(
        waardes_tint,
        waardes_verzadiging,
        waardes_helderheid,
        ):
        
        kleur = HSL(
            tint = tint,
            verzadiging = verzadiging,
            helderheid = helderheid,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_tint(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[HSL]:
    
    kleuren = []
    
    waardes_tint = interpolatie_func(start.tint, eind.tint, aantal_kleuren)
    alfa = start.alfa
    
    if constante == "start":
        verzadiging = start.verzadiging
        helderheid = start.helderheid
        alfa = start.alfa
    elif constante == "eind":
        verzadiging = eind.verzadiging
        helderheid = eind.helderheid
        alfa = eind.alfa
    elif constante == "gemiddeld":
        verzadiging = 0.5 * start.verzadiging + 0.5 * eind.verzadiging
        helderheid = 0.5 * start.helderheid + 0.5 * eind.helderheid
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for tint in waardes_tint:
        
        kleur = HSL(
            tint = tint,
            verzadiging = verzadiging,
            helderheid = helderheid,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_verzadiging(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[HSL]:
    
    kleuren = []
    
    waardes_verzadiging = interpolatie_func(start.verzadiging, eind.verzadiging, aantal_kleuren)
    
    if constante == "start":
        tint = start.tint
        helderheid = start.helderheid
        alfa = start.alfa
    elif constante == "eind":
        tint = eind.tint
        helderheid = eind.helderheid
        alfa = eind.alfa
    elif constante == "gemiddeld":
        tint = 0.5 * start.tint + 0.5 * eind.tint
        helderheid = 0.5 * start.helderheid + 0.5 * eind.helderheid
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for verzadiging in waardes_verzadiging:
        
        kleur = HSL(
            tint = tint,
            verzadiging = verzadiging,
            helderheid = helderheid,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_helderheid(
    start: HSL,
    eind: HSL,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[HSL]:
    
    kleuren = []
    
    waardes_helderheid = interpolatie_func(start.helderheid, eind.helderheid, aantal_kleuren)
    
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
    
    for helderheid in waardes_helderheid:
        
        kleur = HSL(
            tint = tint,
            verzadiging = verzadiging,
            helderheid = helderheid,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren