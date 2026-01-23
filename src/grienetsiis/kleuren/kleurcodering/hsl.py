from __future__ import annotations
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .hex import HEX
    from .cmyk import CMYK
    from .rgb import RGB


class HSL:
    
    _RGB: ClassVar[RGB | None]  = None
    
    # DUNDER METHODS
    
    def __init__(
        self,
        tint: float = 0.0,
        verzadiging: float = 0.0,
        helderheid: float = 0.0,
        alfa: float = 1.0,
        ) -> HSL:
        
        self.tint = tint
        self.verzadiging = verzadiging
        self.helderheid = helderheid
        self.alfa = alfa
    
    def __repr__(self) -> str:
        return f"({self.tint}, {self.verzadiging}, {self.helderheid}, {self.alfa})" 
    
    # CLASS METHODS
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> HSL:
        return hex.naar_hsl()
    
    @classmethod
    def van_cmyk(
        cls,
        cmyk: CMYK,
        ) -> HSL:
        return cmyk.naar_hsl()
    
    @classmethod
    def van_rgb(
        cls,
        rgb: RGB,
        ) -> HSL:
        return rgb.naar_hsl()
    
    # INSTANCE METHODS
    
    def naar_hex(self) -> HEX:
        return self._RGB.van_hsl(self).naar_hex()
    
    def naar_cmyk(self) -> CMYK:
        return self._RGB.van_hsl(self).naar_cmyk()
    
    def naar_rgb(self) -> RGB:
        return self._RGB.van_hsl(self)
    
    # PROPERTIES
    
    @property
    def hex(self) -> HEX:
        return self.naar_hex()
    
    @property
    def cmyk(self) -> CMYK:
        return self.naar_cmyk()
    
    @property
    def rgb(self) -> RGB:
        return self.naar_rgb()