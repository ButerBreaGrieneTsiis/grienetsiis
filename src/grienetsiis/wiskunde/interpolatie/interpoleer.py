"""grienetsiis.wiskunde.kubisch"""
from typing import List, Literal

from .lineair import lineair
from .logaritmisch import logaritmisch
from .smoothstep import smoothstep
from .smootherstep import smootherstep


def interpoleer(
    start: float,
    eind: float,
    methode: Literal["start", "gemiddeld", "eind", "lineair", "logaritmisch", "smoothstep", "smootherstep"] | float,
    aantal: int,
    ) -> List[float]:
    
    if methode == "start":
        return [start for _ in range(aantal)]
    elif methode == "gemiddeld":
        return [0.5*start + 0.5*eind for _ in range(aantal)]
    elif methode == "eind":
        return [eind for _ in range(aantal)]
    elif methode == "lineair":
        return lineair(start, eind, aantal)
    elif methode == "logaritmisch":
        return logaritmisch(start, eind, aantal)
    elif methode == "smoothstep":
        return smoothstep(start, eind, aantal)
    elif methode == "smootherstep":
        return smootherstep(start, eind, aantal)
    elif isinstance(methode, float):
        return [methode for _ in range(aantal)]
    
    raise ValueError(f"onbekende methode \"{methode}\"")