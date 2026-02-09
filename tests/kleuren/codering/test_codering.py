from random import choice

from grienetsiis.kleuren import HEX, HSL, HSV, RGB, CMYK, Kleur


def test_codering():
    
    AANTAL_TESTS = 10
    
    for _ in range(AANTAL_TESTS):
        hexcode = "#"+"".join(choice("0123456789abcdef") for _ in range(8))
        hex = HEX(hexcode)
        
        hsl = HSL.van_hex(hex)
        hsv = HSV.van_hex(hex)
        cmyk = CMYK.van_hex(hex)
        rgb = RGB.van_hex(hex)
        kleur = Kleur(hex, "groen")
        
        assert hsl.hex == hsv.hex == cmyk.hex == rgb.hex == kleur.hex
        assert hex.hsl == hsv.hsl == cmyk.hsl == rgb.hsl == rgb.hsl == kleur.hsl
        assert hex.hsv == hsl.hsv == cmyk.hsv == rgb.hsv == kleur.hsv
        assert hex.cmyk == hsl.cmyk == hsv.cmyk == rgb.cmyk == kleur.cmyk
        assert hex.rgb == hsl.rgb == hsv.rgb == cmyk.rgb == hex.rgb == kleur.rgb
        assert hsl.grijswaarde == hsv.grijswaarde == cmyk.grijswaarde == rgb.grijswaarde == kleur.grijswaarde