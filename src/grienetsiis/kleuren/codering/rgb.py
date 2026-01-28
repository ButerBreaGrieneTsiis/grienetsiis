"""grienetsiis.kleuren.codering.rgb"""
from __future__ import annotations
from typing import ClassVar

from .hex import HEX
from .hsl import HSL
from .hsv import HSV
from .cmyk import CMYK


class RGB:
    
    # DUNDER METHODS
    
    LIMIT_8BIT: ClassVar[int] = 255
    
    def __init__(
        self,
        rood: int = 0,
        groen: int = 0,
        blauw: int = 0,
        alfa: float = 1.0,
        ) -> RGB:
        
        self.rood = rood
        self.groen = groen
        self.blauw = blauw
        self.alfa = alfa
    
    def __repr__(self) -> str:
        return f"RGB({self.rood}, {self.groen}, {self.blauw}, {self.alfa})"
    
    # CLASS METHODS
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> RGB:
        
        rood = int(hex.hex_rood, HEX.LIMIT_HEXDECIMAL)
        groen = int(hex.hex_groen, HEX.LIMIT_HEXDECIMAL)
        blauw = int(hex.hex_blauw, HEX.LIMIT_HEXDECIMAL)
        alfa = int(hex.hex_alfa, HEX.LIMIT_HEXDECIMAL) / cls.LIMIT_8BIT
        
        return cls(
            rood = rood,
            groen = groen,
            blauw = blauw,
            alfa = alfa,
            )
    
    @classmethod
    def van_hsl(
        cls,
        hsl: HSL,
        ) -> RGB:
        
        # https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB
        if hsl.verzadiging == 0:
            return cls()
        else:
            
            chroma = (1 - abs(2*hsl.helderheid - 1)) * hsl.verzadiging
            waarde = chroma * (1 - abs(6*hsl.tint%2 - 1))
            
            if 0 <= hsl.tint < 1/6:
                rood, groen, blauw = chroma, waarde, 0
            elif 1/6 <= hsl.tint < 2/6:
                rood, groen, blauw = waarde, chroma, 0
            elif 2/6 <= hsl.tint < 3/6:
                rood, groen, blauw = 0, chroma, waarde
            elif 3/6 <= hsl.tint < 4/6:
                rood, groen, blauw = 0, waarde, chroma
            elif 4/6 <= hsl.tint < 5/6:
                rood, groen, blauw = waarde, 0, chroma
            elif 5/6 <= hsl.tint <= 6/6:
                rood, groen, blauw = chroma, 0, waarde
            
            return cls(
                rood = cls.LIMIT_8BIT*(rood + hsl.helderheid - chroma/2),
                groen = cls.LIMIT_8BIT*(groen + hsl.helderheid - chroma/2),
                blauw = cls.LIMIT_8BIT*(blauw + hsl.helderheid - chroma/2),
                alfa = hsl.alfa,
                )
    
    @classmethod
    def van_hsv(
        cls,
        hsv: HSV,
        ) -> RGB:
        
        if hsv.verzadiging == 0:
            return cls()
        else:
            
            chroma = hsv.waarde * hsv.verzadiging
            waarde = chroma * (1 - abs(6*hsv.tint%2 - 1))
            
            if 0 <= hsv.tint < 1/6:
                rood, groen, blauw = chroma, waarde, 0
            elif 1/6 <= hsv.tint < 2/6:
                rood, groen, blauw = waarde, chroma, 0
            elif 2/6 <= hsv.tint < 3/6:
                rood, groen, blauw = 0, chroma, waarde
            elif 3/6 <= hsv.tint < 4/6:
                rood, groen, blauw = 0, waarde, chroma
            elif 4/6 <= hsv.tint < 5/6:
                rood, groen, blauw = waarde, 0, chroma
            elif 5/6 <= hsv.tint <= 6/6:
                rood, groen, blauw = chroma, 0, waarde
            
            return cls(
                rood = cls.LIMIT_8BIT*(rood + hsv.waarde - chroma),
                groen = cls.LIMIT_8BIT*(groen + hsv.waarde - chroma),
                blauw = cls.LIMIT_8BIT*(blauw + hsv.waarde - chroma),
                alfa = hsv.alfa,
                )
    
    @classmethod
    def van_cmyk(
        cls,
        cmyk: CMYK,
        ) -> RGB:
        
        rood = cls.LIMIT_8BIT * (1 - cmyk.cyaan) * (1 - cmyk.zwart)
        groen = cls.LIMIT_8BIT * (1 - cmyk.magenta) * (1 - cmyk.zwart)
        blauw = cls.LIMIT_8BIT * (1 - cmyk.geel) * (1 - cmyk.zwart)
        
        return cls(
            rood = rood,
            groen = groen,
            blauw = blauw,
            alfa = cmyk.alfa,
            )
    
    # INSTANCE METHODS
    
    def naar_hex(self) -> HEX:
        return HEX(f"#{self.rood:02x}{self.groen:02x}{self.blauw:02x}{int(self.alfa*self.LIMIT_8BIT):02x}")
    
    def naar_hsl(self) -> HSL:
        
        # https://gist.github.com/ciembor/1494530
        rood_decimaal = self.rood / self.LIMIT_8BIT
        groen_decimaal = self.groen / self.LIMIT_8BIT
        blauw_decimaal = self.blauw / self.LIMIT_8BIT
        
        waarde_min = min(rood_decimaal, groen_decimaal, blauw_decimaal)
        waarde_max = max(rood_decimaal, groen_decimaal, blauw_decimaal)
        
        helderheid = (waarde_max + waarde_min) / 2
        
        if waarde_min == waarde_max:
            tint = 0.0
            verzadiging = 0.0
        
        else:
            verzadiging = (waarde_max - waarde_min) / (2 - waarde_max - waarde_min)  if helderheid > 0.5 else (waarde_max - waarde_min) / (waarde_max + waarde_min)
            
            if waarde_max == rood_decimaal:
                tint = (groen_decimaal - blauw_decimaal)/(waarde_max - waarde_min) + 6 if groen_decimaal < blauw_decimaal else (groen_decimaal - blauw_decimaal)/(waarde_max - waarde_min)
            elif waarde_max == groen_decimaal:
                tint = (blauw_decimaal - rood_decimaal)/(waarde_max - waarde_min) + 2
            else:
                tint = (rood_decimaal - groen_decimaal)/(waarde_max - waarde_min) + 4
            
            tint /= 6
        
        return HSL(
            tint = tint,
            verzadiging = verzadiging,
            helderheid = helderheid,
            alfa = self.alfa,
            )
    
    def naar_hsv(self) -> HSV:
        
        rood_decimaal = self.rood / self.LIMIT_8BIT
        groen_decimaal = self.groen / self.LIMIT_8BIT
        blauw_decimaal = self.blauw / self.LIMIT_8BIT
        
        waarde_min = min(rood_decimaal, groen_decimaal, blauw_decimaal)
        waarde_max = max(rood_decimaal, groen_decimaal, blauw_decimaal)
        
        if waarde_max == 0.0:
            verzadiging = 0.0
        else:
            verzadiging = (waarde_max - waarde_min)/waarde_max
        
        if waarde_min == waarde_max:
            tint = 0.0
        else:
            
            if waarde_max == rood_decimaal:
                tint = (groen_decimaal - blauw_decimaal)/(waarde_max - waarde_min) + 6 if groen_decimaal < blauw_decimaal else (groen_decimaal - blauw_decimaal)/(waarde_max - waarde_min)
            elif waarde_max == groen_decimaal:
                tint = (blauw_decimaal - rood_decimaal)/(waarde_max - waarde_min) + 2
            else:
                tint = (rood_decimaal - groen_decimaal)/(waarde_max - waarde_min) + 4
            
            tint /= 6
        
        waarde = waarde_max
        
        return HSV(
            tint = tint,
            verzadiging = verzadiging,
            waarde = waarde,
            alfa = self.alfa,
            )
    
    def naar_cmyk(self) -> CMYK:
        
        zwart = 1 - max((self.rood/self.LIMIT_8BIT, self.groen/self.LIMIT_8BIT, self.blauw/self.LIMIT_8BIT))
        
        cyaan = (1 - self.rood/self.LIMIT_8BIT - zwart) / (1 - zwart)
        magenta = (1 - self.groen/self.LIMIT_8BIT - zwart) / (1 - zwart)
        geel = (1 - self.blauw/self.LIMIT_8BIT - zwart) / (1 - zwart)
        
        return CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
            alfa = self.alfa,
            )
    
    # PROPERTIES
    
    @property
    def rood(self):
        return self._rood
    
    @rood.setter
    def rood(
        self,
        rood: int,
        ):
        
        if 0 <= rood <= self.LIMIT_8BIT:
            self._rood = int(round(rood))
        else:
            raise ValueError(f"waarde moet tussen 0 en {self.LIMIT_8BIT} zitten, niet {rood}")
    
    @property
    def groen(self):
        return self._groen
    
    @groen.setter
    def groen(
        self,
        groen: int,
        ):
        
        if 0 <= groen <= self.LIMIT_8BIT:
            self._groen = int(round(groen))
        else:
            raise ValueError(f"Waarde moet tussen 0 en {self.LIMIT_8BIT} zitten, niet {groen}")
    
    @property
    def blauw(self):
        return self._blauw
    
    @blauw.setter
    def blauw(
        self,
        blauw: int,
        ):
        
        if 0 <= blauw <= self.LIMIT_8BIT:
            self._blauw = int(round(blauw))
        else:
            raise ValueError(f"Waarde moet tussen 0 en {self.LIMIT_8BIT} zitten, niet {blauw}")
    
    @property
    def alfa(self):
        return self._alfa
    
    @alfa.setter
    def alfa(
        self,
        alfa: float,
        ):
        
        if 0 <= alfa <= 1:
            self._alfa = alfa
        else:
            raise ValueError(f"Waarde moet tussen 0.0 en 1.0 zitten, niet {alfa}")
    
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
        return self.naar_cmyk()
    
    @property
    def rgb(self) -> RGB:
        return self
    
    @property
    def inverse(self) -> RGB:
        return RGB(
            rood = RGB.LIMIT_8BIT - self.rood,
            groen = RGB.LIMIT_8BIT - self.groen,
            blauw = RGB.LIMIT_8BIT - self.blauw,
            alfa = self.alfa,
            )
    
    @property
    def grijswaarde(self) -> float:
        return (0.2126*self.rood + 0.7152*self.groen + 0.0722*self.blauw) / self.LIMIT_8BIT

HEX._RGB = RGB
HSL._RGB = RGB
HSV._RGB = RGB
CMYK._RGB = RGB