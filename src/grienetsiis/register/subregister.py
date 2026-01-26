from __future__ import annotations
from typing import List, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from .geregistreerd_object import GeregistreerdObject


class Subregister(dict):
    
    # DUNDER METHODS
    
    def __init__(
        self,
        geregistreerd_type: Type
        ):
        
        self._type = geregistreerd_type
    
    # INSTANCE METHODS
    
    # PROPERTIES
    
    @property
    def lijst(self) -> List[GeregistreerdObject]:
        return list(self.values())