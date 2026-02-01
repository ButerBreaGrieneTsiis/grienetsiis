"""grienetsiis.wiskunde.interpolatie.logaritmisch"""
from math import exp, log
from typing import List


def logaritmisch(
    start: float,
    eind: float,
    aantal: int,
    ondergrens: float = 0.01,
    ) -> List[float]:
    
    waardes = []
    
    log_start = log(ondergrens) - start if start < ondergrens else log(start)
    log_eind = log(ondergrens) - eind if eind < ondergrens else log(eind)
    
    afstand = log_eind - log_start
    
    for index_kleur in range(aantal):
        exponent = log_start + afstand * (index_kleur)/(aantal - 1)
        waarde = exp(exponent)
        waardes.append(waarde)
    
    return waardes