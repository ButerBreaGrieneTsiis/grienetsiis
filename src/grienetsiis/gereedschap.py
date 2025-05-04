from typing import Iterator


def jaar_maand_iterator(
    jaar_start: int,
    maand_start: int,
    jaar_eind: int,
    maand_eind: int,
    ) -> Iterator[int]:
    
    jaar_maand_start    =   12*jaar_start + maand_start-1
    jaar_maand_eind     =   12*jaar_eind + maand_eind-1
    
    for jaar_maand in range(jaar_maand_start, jaar_maand_eind + 1):
        jaar, maand = divmod(jaar_maand, 12)
        yield jaar, maand+1

def decimaal_getal(
    getal               :   float,
    decimalen_precisie  :   int = 2,
    groeperen_per       :   int = 3,
    absolute            :   bool = False,
    ) -> str:
    
    getal_tekst = f"{abs(getal):.{decimalen_precisie}f}"
    
    integer = getal_tekst.split(".")[0]
    decimalen = getal_tekst.split(".")[1]
    
    integer_geformatteerd = u"\u2009".join([integer[::-1][index:index+groeperen_per] for index in range(0, len(integer), groeperen_per)])[::-1]
    decimalen_geformatteerd = u"\u2009".join([decimalen[index:index+groeperen_per] for index in range(0, len(decimalen), groeperen_per)])
    
    teken = "-" if (getal < 0 and not absolute) else ""
    
    return f"{teken}{integer_geformatteerd},{decimalen_geformatteerd}"

def toon_bedrag(
    bedrag          :   float,
    symbool         :   str     =   u"\u20ac",
    symbool_ervoor  :   bool    =   True,
    spatie          :   bool    =   True,
    ) -> str:
    
    bedrag_geformateerd = decimaal_getal(bedrag, absolute = True)
    
    bedrag_tekst    =   bedrag_geformateerd.split(",")[0]+",- " if abs(bedrag) % 1 == 0 else bedrag_geformateerd
    bedrag_teken    =   "" if bedrag > 0 else "-"
    
    if symbool_ervoor:
        return f"{bedrag_teken}{symbool}{" "*spatie}{bedrag_tekst}"
    else:
        return f"{bedrag_teken}{bedrag}{" "*spatie}{bedrag_tekst}"