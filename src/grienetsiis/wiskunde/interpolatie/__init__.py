"""
grienetsiis.wiskunde.interpolatie
"""
from .lineair import lineair
from .kwadratisch import kwadratisch
from .kubisch import kubisch
from .smoothstep import smoothstep
from .smootherstep import smootherstep
from .logaritmisch import logaritmisch


__all__ = [
    "lineair",
    "kwadratisch",
    "kubisch",
    "smoothstep",
    "smootherstep",
    "logaritmisch",
    ]