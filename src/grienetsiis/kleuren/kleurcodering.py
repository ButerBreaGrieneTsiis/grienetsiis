from __future__ import annotations


LIMIT_8BIT: int = 255
LIMIT_HEXADECIMAL: int = 16

class HEX:
    
    # DUNDER METHODS
    
    def __init__(
        self,
        tekst: str,
        ) -> HEX:
        
        self._tekst = tekst
    
    def __repr__(self) -> str:
        return self.hexa
    
    # CLASS METHODS
    
    @classmethod
    def van_rgba(
        cls,
        rgba: RGBA,
        ) -> HEX:
        return rgba.naar_hex()
    
    @classmethod
    def van_rgb(
        cls,
        rgb: RGB,
        ) -> HEX:
        return rgb.naar_hex()
    
    @classmethod
    def van_hex(
        cls,
        hsl: HSL,
        ) -> HEX:
        return hsl.naar_hex()
    
    # INSTANCE METHODS
    
    def naar_rgba(self) -> RGBA:
        return RGBA.van_hex(self)
    
    def naar_rgb(self) -> RGB:
        return RGBA.van_hex(self).naar_rgb()
    
    def naar_hsl(self) -> HSL:
        return RGBA.van_hex(self).naar_hsl()
    
    # PROPERTIES
    
    @property
    def hex(self) -> str:
        if len(self._tekst) == 7:
            return self._tekst
        return self._tekst[:-2]
    
    @property
    def hexa(self) -> str:
        if len(self._tekst) == 7:
            return self._tekst + "ff"
        return self._tekst
    
    @property
    def hex_rood(self) -> str:
        return self.hexa[1:3]
    
    @property
    def hex_groen(self) -> str:
        return self.hexa[3:5]
    
    @property
    def hex_blauw(self) -> str:
        return self.hexa[5:7]
    
    @property
    def hex_alfa(self) -> str:
        return self.hexa[7:]
    
    @property
    def RGBA(self) -> RGBA:
        return self.naar_rgba()
    
    @property
    def RGB(self) -> RGB:
        return self.naar_rgb()
    
    @property
    def HEX(self) -> HEX:
        return self
    
    @property
    def HSL(self) -> HSL:
        return self.naar_hsl()

class HSL:
    
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
    def van_rgba(
        cls,
        rgba: RGBA,
        ) -> HSL:
        return rgba.naar_hsl()
    
    @classmethod
    def van_rgb(
        cls,
        rgb: RGB,
        ) -> HSL:
        return rgb.naar_hsl()
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> HSL:
        return hex.naar_hsl()
    
    # INSTANCE METHODS
    
    def naar_rgba(self) -> RGBA:
        return RGBA.van_hsl(self)
    
    def naar_rgb(self) -> RGB:
        return RGBA.van_hsl(self).naar_rgb()
    
    def naar_hex(self) -> HEX:
        return RGBA.van_hsl(self).naar_hex()
    
    # PROPERTIES
    
    @property
    def RGBA(self) -> RGBA:
        return self.naar_rgba()
    
    @property
    def RGB(self) -> RGB:
        return self.naar_rgb()
    
    @property
    def HEX(self) -> HEX:
        return self.naar_hex()
    
    @property
    def HSL(self) -> HSL:
        return self

class RGB:
    
    # DUNDER METHODS
    
    def __init__(
        self,
        rood: int = 0,
        groen: int = 0,
        blauw: int = 0,
        ) -> RGB:
        
        self.rood = rood
        self.groen = groen
        self.blauw = blauw
    
    def __repr__(self) -> str:
        return f"({self.rood}, {self.groen}, {self.blauw})"
    
    # CLASS METHODS
    
    @classmethod
    def van_rgba(
        cls,
        rgba: RGBA,
        ) -> RGB:
        return rgba.naar_rgb()
        
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> RGB:
        return hex.naar_rgb()
    
    @classmethod
    def van_hsl(
        cls,
        hsl: HSL,
        ) -> RGB:
        return hsl.naar_rgb()
    
    # INSTANCE METHODS
    
    def naar_rgba(self) -> RGB:
        return RGBA.van_rgb(self)
    
    def naar_hex(self) -> HEX:
        return RGBA.van_rgb(self).naar_hex()
    
    def naar_hsl(self) -> HSL:
        return RGBA.van_rgb(self).naar_hsl()
    
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
            self._rood  =   int(round(rood))
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
            self._groen  =   int(round(groen))
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
            self._blauw  =   int(round(blauw))
        else:
            raise ValueError(f"Waarde moet tussen 0 en {LIMIT_8BIT} zitten, niet {blauw}")
    
    @property
    def RGBA(self) -> RGBA:
        return self.naar_rgba()
    
    @property
    def RGB(self) -> RGB:
        return self
    
    @property
    def HEX(self) -> HEX:
        return self.naar_hex()
    
    @property
    def HSL(self) -> HSL:
        return self.naar_hsl()

class RGBA(RGB):
    
    # DUNDER METHODS
    
    def __init__(
        self,
        rood: int = 0,
        groen: int = 0,
        blauw: int = 0,
        alfa: float = 1.0,
        ) -> RGBA:
        
        super().__init__(
            rood = rood,
            groen = groen,
            blauw = blauw,
            )
        
        self.alfa = alfa
    
    def __repr__(self) -> str:
        return f"({self.rood}, {self.groen}, {self.blauw}, {self.alfa})"
    
    # CLASS METHODS
    
    @classmethod
    def van_rgb(
        cls,
        rgb: RGB,
        ) -> RGBA:
        
        return cls(
            rood = rgb.rood,
            groen = rgb.groen,
            blauw = rgb.blauw,
            )
    
    @classmethod
    def van_hex(
        cls,
        hex: HEX,
        ) -> RGBA:
        
        rood = int(hex.hex_rood, LIMIT_HEXADECIMAL)
        groen = int(hex.hex_groen, LIMIT_HEXADECIMAL)
        blauw = int(hex.hex_blauw, LIMIT_HEXADECIMAL)
        alfa = int(hex.hex_alfa, LIMIT_HEXADECIMAL) / LIMIT_8BIT
        
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
        ) -> RGBA:
        
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
    
    # INSTANCE METHODS
    
    def naar_rgb(self) -> RGB:
        return RGB(
            rood = self.rood,
            groen = self.groen,
            blauw = self.blauw,
            )
    
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
    
    # PROPERTIES
    
    @property
    def alfa(self):
        return self._alfa
    
    @alfa.setter
    def alfa(
        self,
        alfa: float,
        ):
        
        if 0 <= alfa <= 1:
            self._alfa  =   alfa
        else:
            raise ValueError(f"Waarde moet tussen 0.0 en 1.0 zitten, niet {alfa}")
    
    @property
    def RGBA(self) -> RGBA:
        return self
    
    @property
    def RGB(self) -> RGB:
        return self.naar_rgb()
    
    @property
    def HEX(self) -> HEX:
        return self.naar_hex()
    
    @property
    def HSL(self) -> HSL:
        return self.naar_hsl()
    
    @property
    def grijswaarden(self) -> float:
        return (0.2126*self.rood + 0.7152*self.groen + 0.0722*self.blauw) / LIMIT_8BIT

if __name__ == "__main__":
    
    hex = HEX("#2eab7b")
    
    rgb = RGB.van_hex(hex)
    rgba = RGBA.van_hex(hex)
    hsl = HSL.van_hex(hex)
    
    print(hex.HEX)
    print(rgb.HEX)
    print(rgba.HEX)
    print(hsl.HEX)
    
    print(hex.RGB)
    print(rgb.RGB)
    print(rgba.RGB)
    print(hsl.RGB)
    
    print(hex.RGBA)
    print(rgb.RGBA)
    print(rgba.RGBA)
    print(hsl.RGBA)
    
    print(hex.HSL)
    print(rgb.HSL)
    print(rgba.HSL)
    print(hsl.HSL)
