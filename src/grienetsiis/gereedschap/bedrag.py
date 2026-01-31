from grienetsiis.gereedschap.getal import formatteer_getal


def formatteer_bedrag(
    bedrag: float,
    symbool: str = u"\u20ac",
    symbool_ervoor: bool = True,
    spatie: bool = True,
    ) -> str:
    
    bedrag_geformateerd = formatteer_getal(
        getal = bedrag,
        decimalen_automatisch = False,
        decimalen = 2,
        absoluut = True,
        )
    
    bedrag_tekst = bedrag_geformateerd.split(",")[0]+",- " if abs(bedrag) % 1 == 0.0 else bedrag_geformateerd
    bedrag_teken = "" if bedrag > 0.0 else "-"
    
    if symbool_ervoor:
        return f"{bedrag_teken}{symbool}{" "*spatie}{bedrag_tekst}"
    else:
        return f"{bedrag_teken}{bedrag}{" "*spatie}{bedrag_tekst}"