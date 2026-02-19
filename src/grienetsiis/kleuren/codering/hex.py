"""grienetsiis.kleuren.codering.hex"""
from __future__ import annotations
import re
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from grienetsiis.kleuren.codering import (
        HSL,
        HSV,
        CMYK,
        RGB,
        )


class HEX:
    
    LIMIT_HEXDECIMAL: ClassVar[int] = 16
    _RGB: ClassVar[RGB | None]  = None
    
    # DUNDER METHODS
    
    def __init__(
        self,
        code: str,
        ) -> HEX:
        
        self._code = code
    
    def __repr__(self) -> str:
        return f"HEX({self.code})"
    
    def __eq__(self, other) -> bool:
        return self.code == other.code
    
    # CLASS METHODS
    
    @classmethod
    def van_hsl(
        cls,
        hsl: HSL,
        ) -> HEX:
        return hsl.naar_hex()
    
    @classmethod
    def van_hsv(
        cls,
        hsv: HSV,
        ) -> HEX:
        return hsv.naar_hex()
    
    @classmethod
    def van_cmyk(
        cls,
        cmyk: CMYK,
        ) -> HEX:
        return cmyk.naar_hex()
    
    @classmethod
    def van_rgb(
        cls,
        rgb: RGB,
        ) -> HEX:
        return rgb.naar_hex()
    
    @classmethod
    def van_rgba(
        cls,
        rgba: RGB,
        ) -> HEX:
        return rgba.naar_hex()
    
    # INSTANCE METHODS
    
    def naar_hsl(self) -> HSL:
        return self._RGB.van_hex(self).naar_hsl()
    
    def naar_hsv(self) -> HSV:
        return self._RGB.van_hex(self).naar_hsv()
    
    def naar_cmyk(self) -> CMYK:
        return self._RGB.van_hex(self).naar_cmyk()
    
    def naar_rgb(self) -> RGB:
        return self._RGB.van_hex(self)
    
    # PROPERTIES
    
    @property
    def code(self) -> str:
        patroon = re.compile("^#[0-9a-fA-F]{6}$") 
        if re.match(patroon, self._code):
            return self._code + "ff"
        return self._code
    
    @property
    def hex_rood(self) -> str:
        return self.code[1:3]
    
    @property
    def hex_groen(self) -> str:
        return self.code[3:5]
    
    @property
    def hex_blauw(self) -> str:
        return self.code[5:7]
    
    @property
    def hex_alfa(self) -> str:
        return self.code[7:]
    
    @property
    def hex(self) -> HEX:
        return self
    
    @property
    def hsl(self) -> HSL:
        return self.naar_hsl()
    
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
    def inverse(self) -> HEX:
        return self.rgb.inverse.hex
    
    @property
    def grijswaarde(self) -> float:
        return self.rgb.grijswaarde