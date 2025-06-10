import re
from typing import Any, Dict, List


class Singleton:
    def __new__(cls):
        if not hasattr(cls, "instantie"):
            cls.instantie = super(Singleton, cls).__new__(cls)
        return cls.instantie

class Stop(Singleton):
    
    def __repr__(self):
        return "Stop"
    
    def __bool__(self):
        return False

STOP = Stop()

def invoer_kiezen(
    beschrijving: str,
    keuzes: List[Any] | Dict[Any, Any],
    kies_een: bool =  True,
    **kwargs,
    ) -> Any:
    
    if kies_een:
        print(f"\nkies een {beschrijving}\n")
    else:
        print(f"\n{beschrijving}\n")
    
    if isinstance(keuzes, list):
        
        if kwargs.get("stoppen", False):
            print(f" [0] {kwargs.get("terug_naar", "TERUG")}")
        
        [print(f" [{ikeuze}] {keuze}") for ikeuze, keuze in enumerate(keuzes, 1)]
        print()
        
        if kwargs.get("stoppen", False):
            ikeuze  =   invoer_validatie("keuze", int, waardes = range(len(keuzes)+1))
        else:
            ikeuze  =   invoer_validatie("keuze", int, waardes = range(1, len(keuzes)+1))
        
        return keuzes[ikeuze-1] if bool(ikeuze) else STOP
    
    elif isinstance(keuzes, dict):
        
        if kwargs.get("stoppen", False):
            print(f" [0] {kwargs.get("terug_naar", "TERUG")}")
        
        [print(f" [{ikeuze}] {keuze}") for ikeuze, keuze in enumerate(keuzes.keys(), 1)]
        print()
        
        if kwargs.get("stoppen", False):
            ikeuze  =   invoer_validatie("keuze", int, waardes = range(len(keuzes)+1))
        else:
            ikeuze  =   invoer_validatie("keuze", int, waardes = range(1, len(keuzes)+1))
        
        return list(keuzes.values())[ikeuze-1] if bool(ikeuze) else STOP
    
    else:
        raise TypeError

def invoer_validatie(
    beschrijving: int,
    type: type,
    **kwargs,
    ) -> int | str | float:
    
    while True:
        
        invoer  =   input(f"{beschrijving}: ")
        
        if invoer == "" and kwargs.get("uitsluiten_leeg", False):
                print(f"invoer mag niet leeg zijn")
                continue
        
        if kwargs.get("valideren", False):
            invoer_kiezen(f"bevestig {beschrijving} \"{invoer}\"", ["ja", "nee"], kies_een = False)
        
        if type == int:
            
            try:
                invoer  =   int(invoer)
            except ValueError:
                print(f"invoer \"{invoer}\" incorrect, enkel type \"{type.__name__}\" toegestaan")
                continue
            else:
                
                if not invoer in kwargs.get("waardes", [invoer]):
                    print(f"invoer \"{invoer}\" incorrect, niet binnen ")
                    continue
                if not kwargs.get("bereik", [invoer, invoer])[0] <= invoer <= kwargs.get("bereik", [invoer, invoer])[1]:
                    print(f"invoer \"{invoer}\" incorrect, moet tussen {kwargs.get("bereik", [invoer, invoer])[0]} en {kwargs.get("bereik", [invoer, invoer])[1]} liggen")
                    continue
                
                return invoer
        
        elif type == str:
            
            if not invoer in kwargs.get("waardes", [invoer]):
                print(f"invoer \"{invoer}\" incorrect, niet binnen {kwargs.get("waardes")}")
                continue
            
            if "regex" in kwargs.keys():
                patroon     =   re.compile(kwargs.get("regex"))
                match       =   patroon.match(invoer)
                
                if match:
                    return match.groupdict("")
                else:
                    print(f"invoer \"{invoer}\" ongeldig")
                    continue
            
            if kwargs.get("kleine_letters", False):
                return invoer.casefold()
            
            return invoer
        
        elif type == float:
            
            try:
                invoer  =   float(invoer)
            except ValueError:
                print(f"invoer \"{invoer}\" incorrect, enkel type \"{type.__name__}\" toegestaan")
                continue
            else:
                
                if not invoer in kwargs.get("waardes", [invoer]):
                    print(f"invoer \"{invoer}\" incorrect, niet binnen ")
                    continue
                if not kwargs.get("bereik", [invoer, invoer])[0] <= invoer <= kwargs.get("bereik", [invoer, invoer])[1]:
                    print(f"invoer \"{invoer}\" incorrect, moet tussen {kwargs.get("bereik", [invoer, invoer])[0]} en {kwargs.get("bereik", [invoer, invoer])[1]} liggen")
                    continue
                
                return invoer
        
        else:
            raise NotImplementedError