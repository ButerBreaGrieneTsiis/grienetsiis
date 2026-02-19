"""grienetsiis.wiskunde.interpolatie.smoothstep"""
from typing import List

from grienetsiis.wiskunde.interpolatie import kubisch


def smoothstep(
    start: float,
    eind: float,
    aantal: int,
    ) -> List[float]:
    
    return kubisch(start, eind, aantal)