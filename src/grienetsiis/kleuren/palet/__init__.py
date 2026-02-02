"""
grienetsiis.kleuren.palet
"""
from typing import List, Literal

from grienetsiis.kleuren.codering import HEX, HSL, HSV, CMYK, RGB
from grienetsiis.kleuren.tinten import kleur_tint_hsv
from grienetsiis.wiskunde.interpolatie import Interpolatie


def palet_regenboog(
    aantal_kleuren: int,
    codering: Literal["hex", "hsl", "hsv", "cmyk", "rgb"] = "hex",
    helderheid: float = 1.0,
    ) -> List[HEX | HSL | HSV | CMYK | RGB]:
    
    grondkleur = HSV(
        tint = 0.0,
        verzadiging = 1.0,
        waarde = helderheid,
        )
    
    kleuren =  kleur_tint_hsv(
        grondkleur = grondkleur,
        aantal_kleuren = aantal_kleuren,
        tint = Interpolatie.lineair("min", "max"),
        verzadiging = Interpolatie.constant(1.0),
        waarde = Interpolatie.constant(1.0),
        )
    
    if codering == "hex":
        return [kleur.hex for kleur in kleuren]
    if codering == "hsl":
        return [kleur.hsl for kleur in kleuren]
    if codering == "hsv":
        return [kleur.hsv for kleur in kleuren]
    if codering == "cmyk":
        return [kleur.cmyk for kleur in kleuren]
    if codering == "rgb":
        return [kleur.rgb for kleur in kleuren]




# wit_gebroken        =   Kleur.van_hex("#e9e8d3")

# grijs_donkerder     =   Kleur.van_hex("#231f20")
# grijs_donker        =   Kleur.van_hex("#564b4f")
# grijs               =   Kleur.van_hex("#231f20")
# grijs_licht         =   Kleur.van_hex("#bfbfbf")
# grijs_lichter       =   Kleur.van_hex("#d9d9d9")

# groen_donkerst      =   Kleur.van_hex("#18563f")
# groen_donkerder     =   Kleur.van_hex("#217455")
# groen_donker        =   Kleur.van_hex("#29926a")
# groen               =   Kleur.van_hex("#2eab7b")
# groen_licht         =   Kleur.van_hex("#44cc99")

# @dataclass
# class RGBCMY:
#     rood: Kleur
#     groen: Kleur
#     blauw: Kleur
#     cyaan: Kleur
#     magenta: Kleur
#     geel: Kleur



# standaard = RGBCMY(
#     Kleur.van_hex("#ae2020"),
#     Kleur.van_hex("#20ae20"),
#     Kleur.van_hex("#2020ae"),
#     Kleur.van_hex("#20aeae"),
#     Kleur.van_hex("#ae20ae"),
#     Kleur.van_hex("#aeae20"),
#     )