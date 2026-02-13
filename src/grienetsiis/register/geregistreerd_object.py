from __future__ import annotations
from enum import Enum
from typing import Any, Dict

from grienetsiis.opdrachtprompt.invoer import invoeren, kiezen

from .register import Register


class GeregistreerdType(type):
    
    REGISTREER_OBJECT: bool = True
    
    def __call__(self, *args, **kwargs):
        
        instantie = super().__call__(*args, **kwargs)
        Register().registreer_instantie(instantie)
        
        return instantie

class GeregistreerdObject(metaclass = GeregistreerdType):
    
    # CLASS METHODS
    
    @classmethod
    def van_json(
        cls,
        **dict,
        ) -> GeregistreerdObject:
        
        return cls(**dict)
    
    @classmethod
    def nieuw(cls) -> GeregistreerdObject:
        
        velden = {sleutel: veld for sleutel, veld in cls.__annotations__.items() if sleutel not in cls.__dict__}
        
        dict = {}
        
        for sleutel, veld in velden.items():
            
            if isinstance(veld, type) and issubclass(veld, Enum):
                waarde = kiezen(
                    opties = {enum: enum.value for enum in veld},
                    tekst_beschrijving = sleutel,
                    )
            elif veld in ("int", "float", "str"):
                waarde = invoeren(
                    tekst_beschrijving = sleutel,
                    invoer_type = veld,
                    )
            else:
                continue
            
            dict[sleutel] = waarde
        
        return cls(**dict)
    
    # INSTANCE METHODS
    
    def naar_json(self) -> Dict[str, Any]:
        
        dict_naar_json = {}
        
        for veld_sleutel, veld_waarde in self.__dict__.items():
            
            # alle velden uitsluiten die standaardwaardes hebben; nutteloos om op te slaan
            if not veld_waarde:
                continue
            
            if veld_sleutel == self._ID_VELD:
                continue
            else:
                dict_naar_json[veld_sleutel] = veld_waarde
        
        return dict_naar_json