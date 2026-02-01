"""grienetsiis.wiskunde.interpolatie.smoothstep"""
from typing import List

from grienetsiis.wiskunde import functies


def smootherstep(
    start: float,
    eind: float,
    aantal: int,
    ) -> List[float]:
    
    waardes = []
    
    a = 6.0 * (eind - start)
    b = -15.0 * (eind - start)
    c = 10.0 * (eind - start)
    d = 0.0
    f = start
    e = 0.0
    
    for index_kleur in range(aantal):
        
        x = index_kleur/(aantal - 1)
        
        waarde = functies.polynoom(x, a, b, c, d, e, f)
        waardes.append(waarde)
    
    return waardes