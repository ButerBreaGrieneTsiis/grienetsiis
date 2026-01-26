from __future__ import annotations
from typing import Any, Dict

from .register import Register


class GeregistreerdType(type):
    
    REGISTREER_OBJECT: bool = True
    
    def __call__(self, *args, **kwargs):
        
        instantie = super().__call__(*args, **kwargs)
        Register().registreer_instantie(instantie)
        
        return instantie

class GeregistreerdObject(metaclass = GeregistreerdType):
    
    @classmethod
    def van_json(
        cls,
        **dict,
        ) -> GeregistreerdObject:
        
        return cls(**dict)
    
    def naar_json(self) -> Dict[str, Any]:
        
        dict_naar_json = {}
        
        for veld_sleutel, veld_waarde in self.__dict__.items():
            
            # alle velden uitsluiten die standaardwaardes hebben; nutteloos om op te slaan
            if not veld_waarde:
                continue
            elif veld_sleutel == "uuid":
                continue
            else:
                dict_naar_json[veld_sleutel] = veld_waarde
        
        return dict_naar_json