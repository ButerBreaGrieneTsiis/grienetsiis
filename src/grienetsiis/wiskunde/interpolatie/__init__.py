"""
grienetsiis.wiskunde.interpolatie
"""
from .kubisch import kubisch
from .kwadratisch import kwadratisch
from .lineair import lineair
from .logaritmisch import logaritmisch
from .smootherstep import smootherstep
from .smoothstep import smoothstep
from .interpoleer import interpoleer, Interpolatie


__all__ = [
    "kubisch",
    "kwadratisch",
    "lineair",
    "logaritmisch",
    "smootherstep",
    "smoothstep",
    "interpoleer",
    "Interpolatie",
    ]