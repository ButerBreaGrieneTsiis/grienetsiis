from __future__ import annotations
from enum import Enum

from grienetsiis.opdrachtprompt.invoer import invoeren, kiezen
from grienetsiis.register.types.geregistreerd_type import GeregistreerdType
from grienetsiis.types import BasisType


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