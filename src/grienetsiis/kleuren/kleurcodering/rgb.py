from __future__ import annotations

from .hex import HEX
from .hsl import HSL
from .cmyk import CMYK


LIMIT_8BIT: int = 255
LIMIT_HEXDECIMAL: int = 16

class RGB:
    
    # DUNDER METHODS
    
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
        return f"({self.rood}, {self.groen}, {self.blauw}, {self.alfa})"
    
    # CLASS METHODS
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> RGB:
        
        rood = int(hex.hex_rood, LIMIT_HEXDECIMAL)
        groen = int(hex.hex_groen, LIMIT_HEXDECIMAL)
        blauw = int(hex.hex_blauw, LIMIT_HEXDECIMAL)
        alfa = int(hex.hex_alfa, LIMIT_HEXDECIMAL) / LIMIT_8BIT
        
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
                rood = LIMIT_8BIT*(rood + hsl.helderheid - chroma/2),
                groen = LIMIT_8BIT*(groen + hsl.helderheid - chroma/2),
                blauw = LIMIT_8BIT*(blauw + hsl.helderheid - chroma/2),
                )
    
    @classmethod
    def van_cmyk(
        cls,
        cmyk: CMYK,
        ) -> RGB:
        
        rood = LIMIT_8BIT * (1 - cmyk.cyaan) * (1 - cmyk.zwart)
        groen = LIMIT_8BIT * (1 - cmyk.magenta) * (1 - cmyk.zwart)
        blauw = LIMIT_8BIT * (1 - cmyk.geel) * (1 - cmyk.zwart)
        
        return cls(
            rood = rood,
            groen = groen,
            blauw = blauw,
            )
    
    # INSTANCE METHODS
    
    def naar_hex(self) -> HEX:
        return HEX(f"#{self.rood:02x}{self.groen:02x}{self.blauw:02x}{int(self.alfa*LIMIT_8BIT):02x}")
    
    def naar_hsl(self) -> HSL:
        
        # https://gist.github.com/ciembor/1494530
        rood = self.rood / LIMIT_8BIT
        groen = self.groen / LIMIT_8BIT
        blauw = self.blauw / LIMIT_8BIT
        
        waarde_min = min(rood, groen, blauw)
        waarde_max = max(rood, groen, blauw)
        
        helderheid = (waarde_max + waarde_min) / 2
        
        if waarde_min == waarde_max:
            tint = 0.0
            verzadiging = 0.0
        
        else:
            verzadiging = (waarde_max - waarde_min) / (2 - waarde_max - waarde_min)  if helderheid > 0.5 else (waarde_max - waarde_min) / (waarde_max + waarde_min)
            
            if waarde_max == rood:
                tint = (groen - blauw)/(waarde_max - waarde_min) + 6 if groen < blauw else (groen - blauw)/(waarde_max - waarde_min)
            elif waarde_max == groen:
                tint = (blauw - rood)/(waarde_max - waarde_min) + 2
            else:
                tint = (rood - groen)/(waarde_max - waarde_min) + 4
            
            tint /= 6
        
        return HSL(
            tint = tint,
            verzadiging = verzadiging,
            helderheid = helderheid,
            alfa = self.alfa,
            )
    
    def naar_cmyk(self) -> CMYK:
        
        zwart = 1 - max((self.rood/LIMIT_8BIT, self.groen/LIMIT_8BIT, self.blauw/LIMIT_8BIT))
        
        cyaan = (1 - self.rood/LIMIT_8BIT - zwart) / (1 - zwart)
        magenta = (1 - self.groen/LIMIT_8BIT - zwart) / (1 - zwart)
        geel = (1 - self.blauw/LIMIT_8BIT - zwart) / (1 - zwart)
        
        return CMYK(
            cyaan = cyaan,
            magenta = magenta,
            geel = geel,
            zwart = zwart,
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
        
        if 0 <= rood <= LIMIT_8BIT:
            self._rood = int(round(rood))
        else:
            raise ValueError(f"waarde moet tussen 0 en {LIMIT_8BIT} zitten, niet {rood}")
    
    @property
    def groen(self):
        return self._groen
    
    @groen.setter
    def groen(
        self,
        groen: int,
        ):
        
        if 0 <= groen <= LIMIT_8BIT:
            self._groen = int(round(groen))
        else:
            raise ValueError(f"Waarde moet tussen 0 en {LIMIT_8BIT} zitten, niet {groen}")
    
    @property
    def blauw(self):
        return self._blauw
    
    @blauw.setter
    def blauw(
        self,
        blauw: int,
        ):
        
        if 0 <= blauw <= LIMIT_8BIT:
            self._blauw = int(round(blauw))
        else:
            raise ValueError(f"Waarde moet tussen 0 en {LIMIT_8BIT} zitten, niet {blauw}")
    
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
    def cmyk(self) -> CMYK:
        return self.naar_cmyk()
    
    @property
    def grijswaarden(self) -> float:
        return (0.2126*self.rood + 0.7152*self.groen + 0.0722*self.blauw) / LIMIT_8BIT

HEX._RGB = RGB
HSL._RGB = RGB
CMYK._RGB = RGB