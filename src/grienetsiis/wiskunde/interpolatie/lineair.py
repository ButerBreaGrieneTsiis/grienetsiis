from typing import List


def lineair(
    start: float,
    eind: float,
    aantal: int,
    ) -> List[float]:
    
    waardes = []
    
    afstand = eind - start
    
    for index_kleur in range(aantal):
        
        waarde = start + afstand/(aantal - 1) * (index_kleur)
        waardes.append(waarde)
    
    return waardes

def lineair_door_grenzen(
    start: float,
    eind: float,
    aantal: int,
    bovengrens: float = 1.0,
    ondergrens: float = 0.0,
    ) -> List[float]:
    
    if start != eind and ondergrens > bovengrens:
        raise ValueError("bovengrens moet boven ondergrens liggen")
    
    waardes = []
    
    if start == eind:
        for index_kleur in range(aantal):
            waardes.append(start)
        return waardes
    
    elif eind > start:
        
        if eind > bovengrens:
            raise ValueError(f"eindwaarde {eind} kan niet boven bovengrens {bovengrens} liggen")
        if start < ondergrens:
            raise ValueError(f"startwaarde {start} kan niet onder ondergrens {ondergrens} liggen")
        
        start_naar_ondergrens = start - ondergrens
        bovengrens_naar_eind = bovengrens - eind
        afstand = start_naar_ondergrens + bovengrens_naar_eind
        
        for index_kleur in range(aantal):
            
            waarde = start - afstand/(aantal - 1) * (index_kleur)
            
            if waarde < ondergrens:
                waarde = bovengrens - (ondergrens - waarde)
            
            waardes.append(waarde)
    
    else:
        
        if start > bovengrens:
            raise ValueError(f"startwaarde {start} kan niet boven bovengrens {bovengrens} liggen")
        if eind < ondergrens:
            raise ValueError(f"eindwaarde {eind} kan niet onder ondergrens {ondergrens} liggen")
        
        eind_naar_ondergrens = eind - ondergrens
        bovengrens_naar_start = bovengrens - start
        afstand = eind_naar_ondergrens + bovengrens_naar_start
        
        for index_kleur in range(aantal):
            
            waarde = start + afstand/(aantal - 1) * (index_kleur)
            
            if waarde > bovengrens:
                waarde = ondergrens - (bovengrens - waarde)
            
            waardes.append(waarde)
        
    return waardes