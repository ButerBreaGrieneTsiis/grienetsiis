from __future__ import annotations
from typing import TYPE_CHECKING

from grienetsiis.register import Register

if TYPE_CHECKING:
    from grienetsiis.register.geregistreerd_object import GeregistreerdObject


class GeregistreerdType(type):
    
    REGISTREER_OBJECT: bool = True
    
    def __call__(self, *args, **kwargs) -> GeregistreerdObject:
        
        instantie = super().__call__(*args, **kwargs)
        Register.registreer_instantie(instantie)
        
        return instantie