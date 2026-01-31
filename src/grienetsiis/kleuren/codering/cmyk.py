"""grienetsiis.kleuren.codering.cmyk"""
from __future__ import annotations
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .hex import HEX
    from .hsl import HSL
    from .hsv import HSV
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
        alfa: float = 0.0,
        ) -> HSL:
        
        self.cyaan = cyaan
        self.magenta = magenta
        self.geel = geel
        self.zwart = zwart
        self.alfa = alfa
    
    def __repr__(self) -> str:
        return f"CMYK({self.cyaan:.1%}, {self.magenta:.1%}, {self.geel:.1%}, {self.zwart:.1%}, {self.alfa:.1%})" 
    
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
    def van_hsv(
        cls,
        hsv: HSV,
        ) -> CMYK:
        return hsv.naar_cmyk()
    
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
    
    def naar_hsv(self) -> HSV:
        return self._RGB.van_cmyk(self).naar_hsv()
    
    def naar_rgb(self) -> RGB:
        return self._RGB.van_cmyk(self)
    
    # PROPERTIES
    
    @property
    def cyaan(self):
        return self._cyaan
    
    @cyaan.setter
    def cyaan(
        self,
        cyaan: int,
        ):
        
        if 0.0 <= cyaan <= 1.0:
            self._cyaan = cyaan
        else:
            raise ValueError(f"cyaan moet tussen 0.0 en 1.0 zitten, niet {cyaan}")
    
    @property
    def magenta(self):
        return self._magenta
    
    @magenta.setter
    def magenta(
        self,
        magenta: int,
        ):
        
        if 0.0 <= magenta <= 1.0:
            self._magenta = magenta
        else:
            raise ValueError(f"magenta moet tussen 0.0 en 1.0 zitten, niet {magenta}")
    
    @property
    def geel(self):
        return self._geel
    
    @geel.setter
    def geel(
        self,
        geel: int,
        ):
        
        if 0.0 <= geel <= 1.0:
            self._geel = geel
        else:
            raise ValueError(f"geel moet tussen 0.0 en 1.0 zitten, niet {geel}")
    
    @property
    def zwart(self):
        return self._zwart
    
    @zwart.setter
    def zwart(
        self,
        zwart: int,
        ):
        
        if 0.0 <= zwart <= 1.0:
            self._zwart = zwart
        else:
            raise ValueError(f"zwart moet tussen 0.0 en 1.0 zitten, niet {zwart}")
    
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
        return self.naar_hsv()
    
    @property
    def cmyk(self) -> CMYK:
        return self
    
    @property
    def rgb(self) -> RGB:
        return self.naar_rgb()
    
    @property
    def inverse(self) -> CMYK:
        return self.rgb.inverse.cmyk
    
    @property
    def grijswaarde(self) -> float:
        return self.rgb.grijswaarde