"""grienetsiis.kleuren.codering.hsv"""
from __future__ import annotations
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .hex import HEX
    from .hsl import HSL
    from .cmyk import CMYK
    from .rgb import RGB


class HSV:
    
    _RGB: ClassVar[RGB | None]  = None
    
    # DUNDER METHODS
    
    def __init__(
        self,
        tint: float = 0.0,
        verzadiging: float = 0.0,
        waarde: float = 0.0,
        alfa: float = 1.0,
        ) -> HSL:
        
        self.tint = tint
        self.verzadiging = verzadiging
        self.waarde = waarde
        self.alfa = alfa
    
    def __repr__(self) -> str:
        return f"HSV({self.tint*360:.1f}\u00b0, {self.verzadiging:.1%}, {self.waarde:.1%}, {self.alfa:.1%})"
    
    # CLASS METHODS
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> HSV:
        return hex.naar_hsv()
    
    @classmethod
    def van_hsl(
        cls,
        hsl: HSL,
        ) -> HSV:
        return hsl.naar_hsv()
    
    @classmethod
    def van_cmyk(
        cls,
        cmyk: CMYK,
        ) -> HSV:
        return cmyk.naar_hsv()
    
    @classmethod
    def van_rgb(
        cls,
        rgb: RGB,
        ) -> HSV:
        return rgb.naar_hsv()
    
    # INSTANCE METHODS
    
    def naar_hex(self) -> HEX:
        return self._RGB.van_hsv(self).naar_hex()
    
    def naar_hsl(self) -> HSL:
        return self._RGB.van_hsv(self).naar_hsl()
    
    def naar_cmyk(self) -> CMYK:
        return self._RGB.van_hsv(self).naar_cmyk()
    
    def naar_rgb(self) -> RGB:
        return self._RGB.van_hsv(self)
    
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
    def waarde(self):
        return self._waarde
    
    @waarde.setter
    def waarde(
        self,
        waarde: int,
        ):
        
        if 0.0 <= waarde <= 1.0:
            self._waarde = waarde
        else:
            raise ValueError(f"waarde moet tussen 0.0 en 1.0 zitten, niet {waarde}")
    
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
            raise ValueError(f"alfa moet tussen 0.0 en 1.0 zitten, niet {alfa}")
    
    @property
    def hex(self) -> HEX:
        return self.naar_hex()
    
    @property
    def hsl(self) -> HSL:
        return self.naar_hsl()
    
    @property
    def hsv(self) -> HSV:
        return self
    
    @property
    def cmyk(self) -> CMYK:
        return self.naar_cmyk()
    
    @property
    def rgb(self) -> RGB:
        return self.naar_rgb()
    
    @property
    def inverse(self) -> HSV:
        return self.rgb.inverse.hsv
    
    @property
    def grijswaarde(self) -> float:
        return self.rgb.grijswaarde