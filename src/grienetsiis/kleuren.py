from dataclasses import dataclass
import random
import re
from typing import Tuple, List, Any

from numpy import linspace


class Kleur:
    
    def __init__(
        self,
        rood    : int   =   0,
        groen   : int   =   0,
        blauw   : int   =   0,
        alfa    : float =   1.0,
        naam    : str   =   None,
        ) -> "Kleur":
        
        self.rood   =   rood
        self.groen  =   groen
        self.blauw  =   blauw
        self.alfa   =   alfa
        self.naam   =   naam
    
    def __repr__(self):
        
        if self.naam is not None:
            return f"Kleur {self.naam}"
        else:
            return f"Kleur {self.hex}"
    
    @classmethod
    def willekeurig(
        cls,
        seed: Any = None,
        ) -> "Kleur":
        
        random.seed(seed)
        
        rood = random.randint(0, 255)
        groen = random.randint(0, 255)
        blauw = random.randint(0, 255)
        
        return cls(
            rood = rood,
            groen = groen,
            blauw = blauw,
            )
    
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
    
    @classmethod
    def van_cmyk(cls):
        ...
    
    @classmethod
    def van_hsl(
        cls,
        tint            :   float,
        verzadiging     :   float,
        helderheid      :   float,
        ) -> "Kleur":
        
        # https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB
        if verzadiging == 0:
            return cls()
        else:
            
            chroma = (1 - abs(2*helderheid - 1)) * verzadiging
            waarde = chroma * (1 - abs(6*tint%2 - 1))
            
            if 0 <= tint < 1/6:
                rood, groen, blauw = chroma, waarde, 0
            elif 1/6 <= tint < 2/6:
                rood, groen, blauw = waarde, chroma, 0
            elif 2/6 <= tint < 3/6:
                rood, groen, blauw = 0, chroma, waarde
            elif 3/6 <= tint < 4/6:
                rood, groen, blauw = 0, waarde, chroma
            elif 4/6 <= tint < 5/6:
                rood, groen, blauw = waarde, 0, chroma
            elif 5/6 <= tint <= 6/6:
                rood, groen, blauw = chroma, 0, waarde
            
            return cls(
                rood    =   255*(rood + helderheid - chroma/2),
                groen   =   255*(groen + helderheid - chroma/2),
                blauw   =   255*(blauw + helderheid - chroma/2),
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
            self._rood  =   int(round(rood))
        else:
            raise ValueError(f"waarde moet tussen 0 en 255 zitten")
    
    @property
    def groen(self):
        return self._groen
    
    @groen.setter
    def groen(
        self,
        groen: int,
        ):
        
        if 0 <= groen <= 255:
            self._groen  =   int(round(groen))
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
            self._blauw  =   int(round(blauw))
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
    
    def cmyk(self) -> Tuple[float, float, float, float]:
        ...
    
    @property
    def hex(self) -> str:
        return f"#{self.rood:02x}{self.groen:02x}{self.blauw:02x}"
    
    @property
    def hexa(self) -> str:
        return f"#{self.rood:02x}{self.groen:02x}{self.blauw:02x}{int(self.alfa*255):02x}"
    
    @property
    def hsl(self) -> Tuple[float, float, float]: 
        
        # https://gist.github.com/ciembor/1494530
        rood, groen, blauw = self.rgb
        
        waarde_min = min(rood, groen, blauw)
        waarde_max = max(rood, groen, blauw)
        
        helderheid = (waarde_max + waarde_min) / 2
        
        if waarde_min == waarde_max:
            tint        =   0.0
            verzadiging =   0.0
        else:
            
            verzadiging = (waarde_max - waarde_min) / (2 - waarde_max - waarde_min)  if helderheid > 0.5 else (waarde_max - waarde_min) / (waarde_max + waarde_min)
            
            if waarde_max == rood:
                tint = (groen - blauw)/(waarde_max - waarde_min) + 6 if groen < blauw else (groen - blauw)/(waarde_max - waarde_min)
            elif waarde_max == groen:
                tint = (blauw - rood)/(waarde_max - waarde_min) + 2
            else:
                tint = (rood - groen)/(waarde_max - waarde_min) + 4
            
            tint /= 6
        
        return (tint, verzadiging, helderheid)
    
    @property
    def grijswaarden(self) -> float:
        return (0.2126*self.rood + 0.7152*self.groen + 0.0722*self.blauw) / 255

def kleurschaal(
    kleur_begin: Kleur,
    kleur_eind: Kleur,
    aantal_kleuren: int,
    ) -> List[Kleur]:
    
    kleuren = []
    
    for kleur_nummer in range(aantal_kleuren):
        
        ratio = kleur_nummer / (aantal_kleuren - 1)
        kleur = Kleur(
            rood    =   kleur_begin.rood  * (1-ratio) + kleur_eind.rood  * ratio,
            groen   =   kleur_begin.groen * (1-ratio) + kleur_eind.groen * ratio,
            blauw   =   kleur_begin.blauw * (1-ratio) + kleur_eind.blauw * ratio,
            alfa    =   kleur_begin.alfa  * (1-ratio) + kleur_eind.alfa  * ratio,
            )
        
        kleuren.append(kleur)
    
    return kleuren

def kleurtinten(
    grondkleur          :   Kleur,
    helderheid_limiet   :   Tuple[float, float] =   (0.25, 0.75),
    aantal              :   int                 =   2,
    ) -> List[Kleur]:
    
    min_helderheid = min(helderheid_limiet)
    max_helderheid = max(helderheid_limiet)
    
    assert 0 <= min_helderheid < max_helderheid <= 1.0
    assert aantal >= 2
    
    grondkleur_hsl = grondkleur.hsl
    
    kleuren = []
    
    for helderheid in linspace(min_helderheid, max_helderheid, aantal):
        kleur = Kleur.van_hsl(
            tint        =   grondkleur_hsl[0],
            verzadiging =   grondkleur_hsl[1],
            helderheid  =   helderheid,
            )
        kleuren.append(kleur)
        
    return kleuren

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

standaard = RGBCMY(
    Kleur.van_hex("#ae2020"),
    Kleur.van_hex("#20ae20"),
    Kleur.van_hex("#2020ae"),
    Kleur.van_hex("#20aeae"),
    Kleur.van_hex("#ae20ae"),
    Kleur.van_hex("#aeae20"),
    )