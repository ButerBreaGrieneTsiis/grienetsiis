from typing import Callable, List

from grienetsiis.kleuren.codering.rgb import RGB


def kleur_schaal_rgba(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_rood = interpolatie_func(start.rood/RGB.LIMIT_8BIT, eind.rood/RGB.LIMIT_8BIT, aantal_kleuren)
    waardes_groen = interpolatie_func(start.groen/RGB.LIMIT_8BIT, eind.groen/RGB.LIMIT_8BIT, aantal_kleuren)
    waardes_blauw = interpolatie_func(start.blauw/RGB.LIMIT_8BIT, eind.blauw/RGB.LIMIT_8BIT, aantal_kleuren)
    waardes_alfa = interpolatie_func(start.alfa, eind.alfa, aantal_kleuren)
    
    for (
        rood,
        groen,
        blauw,
        alfa,
        ) in zip(
        waardes_rood,
        waardes_groen,
        waardes_blauw,
        waardes_alfa,
        ):
        
        kleur = RGB(
            rood = rood * RGB.LIMIT_8BIT,
            groen = groen * RGB.LIMIT_8BIT,
            blauw = blauw * RGB.LIMIT_8BIT,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_rgb(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_rood = interpolatie_func(start.rood/RGB.LIMIT_8BIT, eind.rood/RGB.LIMIT_8BIT, aantal_kleuren)
    waardes_groen = interpolatie_func(start.groen/RGB.LIMIT_8BIT, eind.groen/RGB.LIMIT_8BIT, aantal_kleuren)
    waardes_blauw = interpolatie_func(start.blauw/RGB.LIMIT_8BIT, eind.blauw/RGB.LIMIT_8BIT, aantal_kleuren)
    
    if constante == "start":
        alfa = start.alfa
    elif constante == "eind":
        alfa = eind.alfa
    elif constante == "gemiddeld":
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        rood,
        groen,
        blauw,
        ) in zip(
        waardes_rood,
        waardes_groen,
        waardes_blauw,
        ):
        
        kleur = RGB(
            rood = rood * RGB.LIMIT_8BIT,
            groen = groen * RGB.LIMIT_8BIT,
            blauw = blauw * RGB.LIMIT_8BIT,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_rood(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_rood = interpolatie_func(start.rood/RGB.LIMIT_8BIT, eind.rood/RGB.LIMIT_8BIT, aantal_kleuren)
    
    if constante == "start":
        groen = start.groen
        blauw = start.blauw
        alfa = start.alfa
    elif constante == "eind":
        groen = eind.groen
        blauw = eind.blauw
        alfa = eind.alfa
    elif constante == "gemiddeld":
        groen = 0.5 * start.groen + 0.5 * eind.groen
        blauw = 0.5 * start.blauw + 0.5 * eind.blauw
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for rood in waardes_rood:
        
        kleur = RGB(
            rood = rood * RGB.LIMIT_8BIT,
            groen = groen,
            blauw = blauw,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_groen(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_groen = interpolatie_func(start.groen/RGB.LIMIT_8BIT, eind.groen/RGB.LIMIT_8BIT, aantal_kleuren)
    
    if constante == "start":
        rood = start.rood
        blauw = start.blauw
        alfa = start.alfa
    elif constante == "eind":
        rood = eind.rood
        blauw = eind.blauw
        alfa = eind.alfa
    elif constante == "gemiddeld":
        rood = 0.5 * start.rood + 0.5 * eind.rood
        blauw = 0.5 * start.blauw + 0.5 * eind.blauw
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for groen in waardes_groen:
        
        kleur = RGB(
            rood = rood,
            groen = groen * RGB.LIMIT_8BIT,
            blauw = blauw,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_blauw(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_blauw = interpolatie_func(start.blauw/RGB.LIMIT_8BIT, eind.blauw/RGB.LIMIT_8BIT, aantal_kleuren)
    
    if constante == "start":
        rood = start.rood
        groen = start.groen
        alfa = start.alfa
    elif constante == "eind":
        rood = eind.rood
        groen = eind.groen
        alfa = eind.alfa
    elif constante == "gemiddeld":
        rood = 0.5 * start.rood + 0.5 * eind.rood
        groen = 0.5 * start.groen + 0.5 * eind.groen
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for blauw in waardes_blauw:
        
        kleur = RGB(
            rood = rood,
            groen = groen,
            blauw = blauw * RGB.LIMIT_8BIT,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_roodgroen(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_rood = interpolatie_func(start.rood/RGB.LIMIT_8BIT, eind.rood/RGB.LIMIT_8BIT, aantal_kleuren)
    waardes_groen = interpolatie_func(start.groen/RGB.LIMIT_8BIT, eind.groen/RGB.LIMIT_8BIT, aantal_kleuren)
    
    if constante == "start":
        blauw = start.blauw
        alfa = start.alfa
    elif constante == "eind":
        blauw = eind.blauw
        alfa = eind.alfa
    elif constante == "gemiddeld":
        blauw = 0.5 * start.blauw + 0.5 * eind.blauw
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        rood,
        groen,
        ) in zip(
        waardes_rood,
        waardes_groen,
        ):
        
        kleur = RGB(
            rood = rood * RGB.LIMIT_8BIT,
            groen = groen * RGB.LIMIT_8BIT,
            blauw = blauw,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_roodblauw(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_rood = interpolatie_func(start.rood/RGB.LIMIT_8BIT, eind.rood/RGB.LIMIT_8BIT, aantal_kleuren)
    waardes_blauw = interpolatie_func(start.blauw/RGB.LIMIT_8BIT, eind.blauw/RGB.LIMIT_8BIT, aantal_kleuren)
    
    if constante == "start":
        groen = start.groen
        alfa = start.alfa
    elif constante == "eind":
        groen = eind.groen
        alfa = eind.alfa
    elif constante == "gemiddeld":
        groen = 0.5 * start.groen + 0.5 * eind.groen
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        rood,
        blauw,
        ) in zip(
        waardes_rood,
        waardes_blauw,
        ):
        
        kleur = RGB(
            rood = rood * RGB.LIMIT_8BIT,
            groen = groen,
            blauw = blauw * RGB.LIMIT_8BIT,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_groenblauw(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_groen = interpolatie_func(start.groen/RGB.LIMIT_8BIT, eind.groen/RGB.LIMIT_8BIT, aantal_kleuren)
    waardes_blauw = interpolatie_func(start.blauw/RGB.LIMIT_8BIT, eind.blauw/RGB.LIMIT_8BIT, aantal_kleuren)
    
    if constante == "start":
        rood = start.rood
        alfa = start.alfa
    elif constante == "eind":
        rood = eind.rood
        alfa = eind.alfa
    elif constante == "gemiddeld":
        rood = 0.5 * start.rood + 0.5 * eind.rood
        alfa = 0.5 * start.alfa + 0.5 * eind.alfa
    
    for (
        groen,
        blauw,
        ) in zip(
        waardes_groen,
        waardes_blauw,
        ):
        
        kleur = RGB(
            rood = rood,
            groen = groen * RGB.LIMIT_8BIT,
            blauw = blauw * RGB.LIMIT_8BIT,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleur_schaal_alfa(
    start: RGB,
    eind: RGB,
    aantal_kleuren: int,
    interpolatie_func: Callable,
    constante: str,
    ) -> List[RGB]:
    
    kleuren = []
    
    waardes_alfa = interpolatie_func(start.alfa, eind.alfa, aantal_kleuren)
    
    if constante == "start":
        rood = start.rood
        groen = start.groen
        blauw = start.blauw
    elif constante == "eind":
        rood = eind.rood
        groen = eind.groen
        blauw = eind.blauw
    elif constante == "gemiddeld":
        rood = 0.5 * start.rood + 0.5 * eind.rood
        groen = 0.5 * start.groen + 0.5 * eind.groen
        blauw = 0.5 * start.blauw + 0.5 * eind.blauw
    
    for alfa in waardes_alfa:
        
        kleur = RGB(
            rood = rood,
            groen = groen,
            blauw = blauw,
            alfa = alfa,
            )
        
        kleuren.append(kleur)
    
    return kleuren