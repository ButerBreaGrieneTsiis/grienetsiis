"""grienetsiis.wiskunde.interpolatie.kwadratisch"""
from typing import List, Literal

from grienetsiis.wiskunde import functies


def kwadratisch(
    start: float,
    eind: float,
    aantal: int,
    helling: Literal["start", "eind"] = "eind"
    ) -> List[float]:
    
    waardes = []
    
    if helling == "start":
        x_helling = 0.0
    elif helling == "eind":
        x_helling = 1.0
    
    c = start
    a = (c-eind)/(2*x_helling - 1)
    b = eind-c-a
    
    for index_kleur in range(aantal):
        
        x = index_kleur/(aantal - 1)
        
        waarde = functies.polynoom(x, a, b, c)
        waardes.append(waarde)
    
    return waardes