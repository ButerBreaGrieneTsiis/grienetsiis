"""grienetsiis.kleuren.codering.hsl"""
from __future__ import annotations
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .hex import HEX
    from .hsv import HSV
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
        return f"HSL({self.tint*360:.1f}\u00b0, {self.verzadiging:.1%}, {self.helderheid:.1%}, {self.alfa:.1%})"
    
    def __eq__(self, other) -> bool:
        return self.tint == other.tint and self.verzadiging == other.verzadiging and self.helderheid == other.helderheid and self.alfa == other.alfa
    
    # CLASS METHODS
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> HSL:
        return hex.naar_hsl()
    
    @classmethod
    def van_hsv(
        cls,
        hsv: HSV,
        ) -> HSL:
        return hex.naar_hsv()
    
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
    
    def naar_hsv(self) -> HSV:
        return self._RGB.van_hsl(self).naar_hsv()
    
    def naar_cmyk(self) -> CMYK:
        return self._RGB.van_hsl(self).naar_cmyk()
    
    def naar_rgb(self) -> RGB:
        return self._RGB.van_hsl(self)
    
    # PROPERTIES
    
    @property
    def tint(self):
        return self._tint
    
    @tint.setter
    def tint(
        self,
        tint: int,
        ):
        
        if 0.0 <= tint <= 1.0:
            self._tint = tint
        else:
            raise ValueError(f"tint moet tussen 0.0 en 1.0 zitten, niet {tint}")
    
    @property
    def verzadiging(self):
        return self._verzadiging
    
    @verzadiging.setter
    def verzadiging(
        self,
        verzadiging: int,
        ):
        
        if 0.0 <= verzadiging <= 1.0:
            self._verzadiging = verzadiging
        else:
            raise ValueError(f"verzadiging moet tussen 0.0 en 1.0 zitten, niet {verzadiging}")
    
    @property
    def helderheid(self):
        return self._helderheid
    
    @helderheid.setter
    def helderheid(
        self,
        helderheid: int,
        ):
        
        if 0.0 <= helderheid <= 1.0:
            self._helderheid = helderheid
        else:
            raise ValueError(f"helderheid moet tussen 0.0 en 1.0 zitten, niet {helderheid}")
    
    @property
    def alfa(self):
        return self._alfa
    
    @alfa.setter
    def alfa(
        self,
        alfa: float,
        ):
        
        if 0.0 <= alfa <= 1.0:
            self._alfa = alfa
        else:
            raise ValueError(f"Waarde moet tussen 0.0 en 1.0 zitten, niet {alfa}")
    
    @property
    def hex(self) -> HEX:
        return self.naar_hex()
    
    @property
    def hsl(self) -> HSL:
        return self
    
    @property
    def hsv(self) -> HSV:
        return self.naar_hsv()
    
    @property
    def cmyk(self) -> CMYK:
        return self.naar_cmyk()
    
    @property
    def rgb(self) -> RGB:
        return self.naar_rgb()
    
    @property
    def inverse(self) -> HSL:
        return self.rgb.inverse.hsl
    
    @property
    def grijswaarde(self) -> float:
        return self.rgb.grijswaarde