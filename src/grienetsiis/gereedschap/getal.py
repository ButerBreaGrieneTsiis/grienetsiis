def formatteer_getal(
    getal: float,
    decimaal_teken: str = ",",
    decimalen_automatisch: bool = True,
    decimalen: int = 3,
    groeperen: bool = True,
    groeperen_per: int = 3,
    absoluut: bool = False,
    decimalen_limiet: int = 12,
    prefix: str = "",
    prefix_spatie: bool = True,
    suffix: str = "",
    suffix_spatie: bool = True,
    ) -> str:
    
    THIN_SPACE = u"\u2009"
    
    if not decimalen_automatisch:
        getal_tekst = f"{abs(getal):.{decimalen}f}"
    else:
        getal_tekst = f"{abs(getal):.{decimalen_limiet}f}"
        
        while getal_tekst.endswith("0"):
            getal_tekst = getal_tekst.removesuffix("0")
            if getal_tekst.endswith("."):
                getal_tekst += "0"
                break
    
    integer = getal_tekst.split(".")[0]
    decimalen = getal_tekst.split(".")[1]
    
    if groeperen:
        integer_geformatteerd = THIN_SPACE.join([integer[::-1][index:index+groeperen_per] for index in range(0, len(integer), groeperen_per)])[::-1]
        decimalen_geformatteerd = THIN_SPACE.join([decimalen[index:index+groeperen_per] for index in range(0, len(decimalen), groeperen_per)])
    else:
        integer_geformatteerd = integer
        decimalen_geformatteerd = decimalen
    
    teken = "-" if (getal < 0.0 and not absoluut) else ""
    
    prefix = prefix + " " if prefix_spatie and prefix else prefix
    suffix = " " + suffix if suffix_spatie and suffix else suffix
    
    return f"{prefix}{teken}{integer_geformatteerd}{decimaal_teken}{decimalen_geformatteerd}{suffix}"