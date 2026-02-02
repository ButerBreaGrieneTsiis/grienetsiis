"""
grienetsiis.wiskunde.interpolatie
"""
from .interpoleer import interpoleer, Interpolatie
from .kubisch import kubisch
from .kwadratisch import kwadratisch
from .lineair import lineair
from .logaritmisch import logaritmisch
from .smootherstep import smootherstep
from .smoothstep import smoothstep


__all__ = [
    "interpoleer",
    "Interpolatie",
    "kubisch",
    "kwadratisch",
    "lineair",
    "logaritmisch",
    "smootherstep",
    "smoothstep",
    ]