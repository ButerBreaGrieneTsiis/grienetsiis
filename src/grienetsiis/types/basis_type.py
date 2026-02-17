from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class BasisType:
    
    # CLASS METHODS
    
    @classmethod
    def van_json(
        cls,
        **dict,
        ) -> BasisType:
        
        return cls(**dict)
    
    # INSTANCE METHODS
    
    def naar_json(self) -> Dict[str, Any]:
        
        dict_naar_json = {}
        
        for veld_sleutel, veld_waarde in self.__dict__.items():
            
            # alle velden uitsluiten die standaardwaardes hebben; nutteloos om op te slaan
            if not veld_waarde:
                continue
            
            if veld_sleutel == "_id":
                continue
            else:
                dict_naar_json[veld_sleutel] = veld_waarde
        
        return dict_naar_json