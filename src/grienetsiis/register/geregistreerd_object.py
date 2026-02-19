from __future__ import annotations
from enum import Enum
from typing import Any, Dict

from grienetsiis.register import Register
from grienetsiis.opdrachtprompt.invoer import invoeren, kiezen
from grienetsiis.types import BasisType

from .register import Register


class GeregistreerdType(type):
    
    REGISTREER_OBJECT: bool = True
    
    def __call__(self, *args, **kwargs):
        
        instantie = super().__call__(*args, **kwargs)
        Register().registreer_instantie(instantie)
        
        return instantie

class GeregistreerdObject(BasisType, metaclass = GeregistreerdType):
    
    # CLASS METHODS
    
    @classmethod
    def nieuw(cls) -> BasisType:
        
        velden = {sleutel: veld for sleutel, veld in cls.__annotations__.items() if sleutel not in cls.__dict__}
        
        dict_nieuw = {}
        
        for sleutel, veld in velden.items():
            
            if isinstance(veld, type) and issubclass(veld, Enum):
                waarde = kiezen(
                    opties = {enum: enum.value for enum in veld},
                    tekst_beschrijving = sleutel,
                    )
            elif veld in ("int", "float", "str", "bool"):
                waarde = invoeren(
                    tekst_beschrijving = sleutel,
                    invoer_type = veld,
                    )
            else:
                continue
            
            dict_nieuw[sleutel] = waarde
        
        return cls(**dict_nieuw)

