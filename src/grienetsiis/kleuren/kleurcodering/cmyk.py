from __future__ import annotations
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .hex import HEX
    from .hsl import HSL
    from .rgb import RGB


class CMYK:
    
    _RGB: ClassVar[RGB | None]  = None
    
    # DUNDER METHODS
    
    def __init__(
        self,
        cyaan: float = 0.0,
        magenta: float = 0.0,
        geel: float = 0.0,
        zwart: float = 0.0,
        ) -> HSL:
        
        self.cyaan = cyaan
        self.magenta = magenta
        self.geel = geel
        self.zwart = zwart
    
    def __repr__(self) -> str:
        return f"({self.cyaan}, {self.magenta}, {self.geel}, {self.zwart})" 
    
    # CLASS METHODS
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> CMYK:
        return hex.naar_cmyk()
    
    @classmethod
    def van_hsl(
        cls,
        hsl: HSL,
        ) -> CMYK:
        return hsl.naar_cmyk()
    
    @classmethod
    def van_rgb(
        cls,
        rgb: RGB,
        ) -> CMYK:
        return rgb.naar_cmyk()
    
    # INSTANCE METHODS
    
    def naar_hex(self) -> HEX:
        return self._RGB.van_cmyk(self).naar_hex()
    
    def naar_hsl(self) -> HSL:
        return self._RGB.van_cmyk(self).naar_hsl()
    
    def naar_rgb(self) -> RGB:
        return self._RGB.van_cmyk(self)
    
    # PROPERTIES
    
    @property
    def hex(self) -> HEX:
        return self.naar_hex()
    
    @property
    def hsl(self) -> HSL:
        return self.naar_hsl()
    
    @property
    def rgb(self) -> RGB:
        return self.naar_rgb()