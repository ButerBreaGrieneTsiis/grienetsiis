import re
from dataclasses import dataclass
from typing import Tuple

class Kleur:
    
    def __init__(
            self,
            rood    : int   =   0,
            groen   : int   =   0,
            blauw   : int   =   0,
            alfa    : float =   1.0,
        ) -> "Kleur":
        
        self.rood   =   rood
        self.groen  =   groen
        self.blauw  =   blauw
        self.alfa   =   alfa
    
    @classmethod
    def van_hex(
        cls,
        hex: str,
        ) -> "Kleur":
        
        patroon_kleur   =   re.compile(r"^#(?P<rood>[0-9a-fA-F]{2})(?P<groen>[0-9a-fA-F]{2})(?P<blauw>[0-9a-fA-F]{2})(?P<alfa>[0-9a-fA-F]{2})?$")
        resultaat       =   patroon_kleur.match(hex).groupdict("ff")
        
        if not bool(resultaat):
            raise ValueError(f"Hexadecimale kleur \"{hex}\" ongeldig")
        
        rood    =   int(resultaat.get("rood"), 16)
        groen   =   int(resultaat.get("groen"), 16)
        blauw   =   int(resultaat.get("blauw"), 16)
        alfa    =   int(resultaat.get("alfa"), 16) / 255
        
        return cls(
            rood,
            groen,
            blauw,
            alfa,
            )
    
    @property
    def rood(self):
        return self._rood
    
    @rood.setter
    def rood(
        self,
        rood: int,
        ):
        
        if 0 <= rood <= 255:
            self._rood  =   int(rood)
        else:
            raise ValueError(f"Waarde moet tussen 0 en 255 zitten")
    
    @property
    def groen(self):
        return self._groen
    
    @groen.setter
    def groen(
        self,
        groen: int,
        ):
        
        if 0 <= groen <= 255:
            self._groen  =   int(groen)
        else:
            raise ValueError(f"Waarde moet tussen 0 en 255 zitten")
    
    @property
    def blauw(self):
        return self._blauw
    
    @blauw.setter
    def blauw(
        self,
        blauw: int,
        ):
        
        if 0 <= blauw <= 255:
            self._blauw  =   int(blauw)
        else:
            raise ValueError(f"Waarde moet tussen 0 en 255 zitten")
    
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
            raise ValueError(f"Waarde moet tussen 0 en 1 zitten")
    
    @property
    def rgb(self) -> Tuple[float, float, float]:
        return (self.rood/255, self.groen/255, self.blauw/255)
    
    @property
    def rgba(self) -> Tuple[float, float, float, float]:
        return (self.rood/255, self.groen/255, self.blauw/255, self.alfa)
    
    @property
    def hex(self) -> str:
        return f"#{self.rood:02x}{self.groen:02x}{self.blauw:02x}{int(self.alfa*255):02x}"
    
    @property
    def grijswaarden(self) -> float:
        return (0.2126*self.rood + 0.7152*self.groen + 0.0722*self.blauw) / 255

@dataclass
class RGBCMY:
    rood: Kleur
    groen: Kleur
    blauw: Kleur
    cyaan: Kleur
    magenta: Kleur
    geel: Kleur

wit_gebroken        =   Kleur.van_hex("#e9e8d3")

grijs_donkerder     =   Kleur.van_hex("#231f20")
grijs_donker        =   Kleur.van_hex("#564b4f")
grijs               =   Kleur.van_hex("#231f20")
grijs_licht         =   Kleur.van_hex("#bfbfbf")
grijs_lichter       =   Kleur.van_hex("#d9d9d9")

groen_donkerst      =   Kleur.van_hex("#18563f")
groen_donkerder     =   Kleur.van_hex("#217455")
groen_donker        =   Kleur.van_hex("#29926a")
groen               =   Kleur.van_hex("#2eab7b")
groen_licht         =   Kleur.van_hex("#44cc99")

standaard   =   RGBCMY(
    Kleur.van_hex("#ae2020"),
    Kleur.van_hex("#20ae20"),
    Kleur.van_hex("#2020ae"),
    Kleur.van_hex("#20aeae"),
    Kleur.van_hex("#ae20ae"),
    Kleur.van_hex("#aeae20"),
    )