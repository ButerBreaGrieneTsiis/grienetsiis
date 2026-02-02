"""grienetsiis.wiskunde.interpoleer"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Callable, List, Literal

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

class InterpolatieMethode(Enum):
    
    CONSTANT = "constant"
    LINEAR = "lineair"
    LOGARITMISCH = "logaritmisch"
    SMOOTHSTEP = "smoothstep"
    SMOOTHERSTEP = "smootherstep"

@dataclass
class Interpolatie:
    
    methode: InterpolatieMethode
    schaalfactor: Literal["min", "max"] | float | None = None
    schaalfactor_start: Literal["min", "max"] | float | None = None
    schaalfactor_eind: Literal["min", "max"] | float | None = None
    
    # CLASS METHODS
    
    @classmethod
    def constant(
        cls,
        schaalfactor: float,
        ) -> Interpolatie:
        
        return cls(
            methode = InterpolatieMethode.CONSTANT,
            schaalfactor = schaalfactor,
            )
    
    @classmethod
    def lineair(
        cls,
        schaalfactor_start: Literal["min", "max"] | float,
        schaalfactor_eind: Literal["min", "max"] | float,
        ) -> Interpolatie:
        
        return cls(
            methode = InterpolatieMethode.LINEAR,
            schaalfactor_start = schaalfactor_start,
            schaalfactor_eind = schaalfactor_eind,
            )
    
    # INSTANCE METHODS
    
    def toepassen(
        self,
        aantal: int,
        waarde: float,
        waarde_min: float = 0.0,
        waarde_max: float = 1.0,
        ) -> List[float]:
        
        if self.methode == InterpolatieMethode.CONSTANT:
            
            if self.schaalfactor == "min":
                waarde_constant = waarde_min
            elif self.schaalfactor == "max":
                waarde_constant = waarde_max
            else:
                waarde_constant = min(max(self.schaalfactor * waarde, waarde_min), waarde_max)
                
                if self.schaalfactor * waarde < waarde_min or self.schaalfactor * waarde > waarde_max:
                    print(f"resulterende waarde {self.schaalfactor * waarde} buiten domein {waarde_min}-{waarde_max}, schaalfactor verlaagd van {self.schaalfactor} naar {waarde_constant/waarde:.3f}")
            
            return list(waarde_constant for _ in range(aantal))
        
        if self.schaalfactor_start == "min":
            waarde_start = waarde_min
        elif self.schaalfactor_start == "max":
            waarde_start = waarde_max
        else:
            waarde_start = min(max(self.schaalfactor_start * waarde, waarde_min), waarde_max)
            
            if self.schaalfactor_start * waarde < waarde_min or self.schaalfactor_start * waarde > waarde_max:
                print(f"resulterende waarde {self.schaalfactor_start * waarde} buiten domein {waarde_min}-{waarde_max}, schaalfactor verlaagd van {self.schaalfactor_start} naar {waarde_start/waarde:.3f}")
        
        if self.schaalfactor_eind == "min":
            waarde_eind = waarde_min
        elif self.schaalfactor_eind == "max":
            waarde_eind = waarde_max
        else:
            waarde_eind = min(max(self.schaalfactor_eind * waarde, waarde_min), waarde_max)
            
            if self.schaalfactor_eind * waarde < waarde_min or self.schaalfactor_start * waarde > waarde_max:
                print(f"resulterende waarde {self.schaalfactor_eind * waarde} buiten domein {waarde_min}-{waarde_max}, schaalfactor verlaagd van {self.schaalfactor_eind} naar {waarde_eind/waarde:.3f}")
        
        return self.functie(
            start = waarde_start,
            eind = waarde_eind,
            aantal = aantal,
            )
    
    # PROPERTIES
    
    @property
    def functie(self) -> Callable:
        
        if self.methode == InterpolatieMethode.CONSTANT:
            return lambda x: x
        if self.methode == InterpolatieMethode.LINEAR:
            return lineair
        if self.methode == InterpolatieMethode.LOGARITMISCH:
            return logaritmisch
        if self.methode == InterpolatieMethode.SMOOTHSTEP:
            return smoothstep
        if self.methode == InterpolatieMethode.SMOOTHERSTEP:
            return smootherstep