from dataclasses import dataclass

from grienetsiis.kleuren.kleurcodering import HEX, HSL, HSV, CMYK, RGB


@dataclass(repr = False)
class Kleur:
    
    codering: HEX | HSL | HSV | CMYK | RGB
    naam: str | None = None
    
    def __repr__(self) -> str:
        return f"Kleur({self.naam} {self.codering})"
    
    @property
    def hex(self) -> HEX:
        return self.codering.hex
    
    @property
    def hsl(self) -> HSL:
        return self.codering.hsl
    
    @property
    def hsv(self) -> HSV:
        return self.codering.hsv
    
    @property
    def cmyk(self) -> CMYK:
        return self.codering.cmyk
    
    @property
    def rgb(self) -> RGB:
        return self.codering.rgb
    
    @property
    def grijswaarde(self) -> float:
        return self.codering.hgrijswaardeex