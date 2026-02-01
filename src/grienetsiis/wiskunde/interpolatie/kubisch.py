"""grienetsiis.wiskunde.interpolatie.kubisch"""
from typing import List


def _kubisch(
    a: float,
    b: float,
    c: float,
    d: float,
    x: float,
    ) -> float:
    return a*x**3 + b*x**2 + c*x + d

def kubisch(
    start: float,
    eind: float,
    aantal: int,
    helling_start: float = 0.0,
    helling_eind: float = 0.0,
    ) -> List[float]:
    
    waardes = []
    
    d = start
    c = helling_start
    a = helling_eind - 2*eind + c + 2*d
    b = eind - a - c - d
    
    for index_kleur in range(aantal):
        
        x = index_kleur/(aantal - 1)
        
        waarde = _kubisch(a, b, c, d, x)
        waardes.append(waarde)
    
    return waardes