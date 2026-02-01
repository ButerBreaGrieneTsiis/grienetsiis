"""
grienetsiis.kleuren.schalen._invoer_naar_waardes
"""
from __future__ import annotations
from typing import List, Literal

from grienetsiis.wiskunde import interpolatie


def _invoer_naar_waardes(
    start: float,
    eind: float,
    kleur_invoer: Literal["start", "gemiddeld", "eind", "lineair", "kwadratisch-start", "kwadratisch-eind", "kubisch", "logaritmisch", "smoothstep", "smootherstep"] | float,
    aantal_kleuren: int,
    ) -> List[float]:
    
    if kleur_invoer == "start":
        return [start for _ in range(aantal_kleuren)]
    elif kleur_invoer == "gemiddeld":
        return [0.5*start + 0.5*eind for _ in range(aantal_kleuren)]
    elif kleur_invoer == "eind":
        return [eind for _ in range(aantal_kleuren)]
    elif kleur_invoer == "lineair":
        return interpolatie.lineair(start, eind, aantal_kleuren)
    elif kleur_invoer == "kwadratisch-start":
        return interpolatie.kwadratisch(start, eind, aantal_kleuren, helling = "start")
    elif kleur_invoer == "kwadratisch-eind":
        return interpolatie.kwadratisch(start, eind, aantal_kleuren, helling = "eind")
    elif kleur_invoer == "kubisch":
        return interpolatie.kubisch(start, eind, aantal_kleuren)
    elif kleur_invoer == "logaritmisch":
        return interpolatie.logaritmisch(start, eind, aantal_kleuren)
    elif kleur_invoer == "smoothstep":
        return interpolatie.smoothstep(start, eind, aantal_kleuren)
    elif kleur_invoer == "smootherstep":
        return interpolatie.smootherstep(start, eind, aantal_kleuren)
    elif isinstance(kleur_invoer, float):
        return [kleur_invoer for _ in range(aantal_kleuren)]