from __future__ import annotations
import re
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .hsl import HSL
    from .cmyk import CMYK
    from .rgb import RGB


class HEX:
    
    _RGB: ClassVar[RGB | None]  = None
    
    # DUNDER METHODS
    
    def __init__(
        self,
        tekst: str,
        ) -> HEX:
        
        self._tekst = tekst
    
    def __repr__(self) -> str:
        return self.hex_code
    
    # CLASS METHODS
    
    @classmethod
    def van_hsl(
        cls,
        hsl: HSL,
        ) -> HEX:
        return hsl.naar_hex()
    
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
    
    def naar_cmyk(self) -> CMYK:
        return self._RGB.van_hex(self).naar_cmyk()
    
    def naar_rgb(self) -> RGB:
        return self._RGB.van_hex(self)
    
    # PROPERTIES
    
    @property
    def hex_code(self) -> str:
        patroon = re.compile("^#[0-9a-fA-F]{6}$") 
        if re.match(patroon, self._tekst):
            return self._tekst + "ff"
        return self._tekst
    
    @property
    def hex_rood(self) -> str:
        return self.hex_code[1:3]
    
    @property
    def hex_groen(self) -> str:
        return self.hex_code[3:5]
    
    @property
    def hex_blauw(self) -> str:
        return self.hex_code[5:7]
    
    @property
    def hex_alfa(self) -> str:
        return self.hex_code[7:]
    
    @property
    def hsl(self) -> HSL:
        return self.naar_hsl()
    
    @property
    def cmyk(self) -> CMYK:
        return self.naar_cmyk()
    
    @property
    def rgb(self) -> RGB:
        return self.naar_rgb()