from __future__ import annotations
from enum import Enum
from typing import Any, ClassVar, Dict

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
    def nieuw(
        cls,
        velden: Dict[str, type],
        ) -> GeregistreerdObject:
        
        dict = {}
        
        for veld, _type in velden.items():
            
            if isinstance(_type, type) and issubclass(_type, Enum):
                waarde = kiezen(
                    opties = {enum.value: enum for enum in _type},
                    tekst_beschrijving = veld,
                    )
            elif _type in ("int", "float", "str"):
                waarde = invoeren(
                    tekst_beschrijving = veld,
                    invoer_type = _type,
                    )
            else:
                continue
            
            dict[veld] = waarde
        
        return cls(**dict)
    
    # INSTANCE METHODS
    
    def naar_json(self) -> Dict[str, Any]:
        
        dict_naar_json = {}
        
        for veld_sleutel, veld_waarde in self.__dict__.items():
            
            # alle velden uitsluiten die standaardwaardes hebben; nutteloos om op te slaan
            if not veld_waarde:
                continue
            
            if veld_sleutel == self._id_veld:
                continue
            else:
                dict_naar_json[veld_sleutel] = veld_waarde
        
        return dict_naar_json