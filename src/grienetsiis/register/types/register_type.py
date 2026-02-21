from __future__ import annotations
from typing import TYPE_CHECKING

from grienetsiis.types import Singleton

if TYPE_CHECKING:
    from grienetsiis.register import Subregister


class RegisterType(Singleton):
    
    def __getitem__(cls, sleutel) -> Subregister:
        return cls()[sleutel]
    
    def __setitem__(cls, sleutel, waarde) -> None:
        cls()[sleutel] = waarde
        
    def __contains__(cls, sleutel) -> bool:
        return sleutel in cls()