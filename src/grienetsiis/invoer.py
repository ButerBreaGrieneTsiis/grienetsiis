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
    stoppen: bool = False,
    meerdere_keuzes: bool = False,
    terug_naar: str = "TERUG",
    ) -> Any:
    
    if kies_een:
        print(f"\nkies een {beschrijving}\n")
    else:
        print(f"\n{beschrijving}\n")
    
    if isinstance(keuzes, list):
        
        aantal_tekens = len(f"{len(keuzes)}") + 2
        
        if stoppen:
            print(f" {f"[0]":>{aantal_tekens}} {terug_naar}")
        
        [print(f" {f"[{ikeuze}]":>{aantal_tekens}} {keuze}") for ikeuze, keuze in enumerate(keuzes, 1)]
        print()
        
        if meerdere_keuzes:
            
            while True:
            
                invoer_keuzes = invoer_validatie("keuze", str, uitsluiten_leeg = True)
                print(invoer_keuzes)
                if invoer_keuzes == "0":
                    return STOP
                
                ikeuzes = []
                
                invoer_keuzes = invoer_keuzes.split(",")
                print(invoer_keuzes)
                for invoer_keuze in invoer_keuzes:
                    print(invoer_keuze)
                    if invoer_keuze.count("-") == 1:
                        if invoer_keuze.split("-")[0].isnumeric() and invoer_keuze.split("-")[1].isnumeric():
                            if int(invoer_keuze.split("-")[0]) < int(invoer_keuze.split("-")[1]):
                                [ikeuzes.append(index) for index in range(int(invoer_keuze.split("-")[0]), int(invoer_keuze.split("-")[1]) + 1)]
                        else:
                            continue
                    
                    elif invoer_keuze.isnumeric():
                        ikeuzes.append(int(invoer_keuze))
                
                return [keuzes[ikeuze-1] for ikeuze in set(ikeuzes)]
        else:
            
            if stoppen:
                ikeuze  =   invoer_validatie("keuze", int, waardes = range(len(keuzes)+1))
            else:
                ikeuze  =   invoer_validatie("keuze", int, waardes = range(1, len(keuzes)+1))
            
            return keuzes[ikeuze-1] if bool(ikeuze) else STOP
    
    elif isinstance(keuzes, dict):
        
        aantal_tekens = len(f"{len(keuzes)}") + 2
        
        if stoppen:
            print(f" {f"[0]":>{aantal_tekens}} {terug_naar}")
        
        [print(f" {f"[{ikeuze}]":>{aantal_tekens}} {keuze}") for ikeuze, keuze in enumerate(keuzes.keys(), 1)]
        print()
        
        if meerdere_keuzes:
            
            while True:
            
                invoer_keuzes = invoer_validatie("keuze", str, uitsluiten_leeg = True)
                
                if invoer_keuzes == "0":
                    return STOP
                
                ikeuzes = []
                
                invoer_keuzes = invoer_keuzes.split(",")
                
                for invoer_keuze in invoer_keuzes:
                    if invoer_keuze.count("-") == 1:
                        if invoer_keuze.split("-")[0].isnumeric() and invoer_keuze.split("-")[1].isnumeric():
                            if int(invoer_keuze.split("-")[0]) < int(invoer_keuze.split("-")[1]):
                                [ikeuzes.append(index) for index in range(int(invoer_keuze.split("-")[0]), int(invoer_keuze.split("-")[1]) + 1)]
                        else:
                            continue
                    
                    elif invoer_keuze.isnumeric():
                        ikeuzes.append(int(invoer_keuze))
                
                return [list(keuzes.values())[ikeuze-1] for ikeuze in set(ikeuzes)]
        
        else:
        
            if stoppen:
                ikeuze  =   invoer_validatie("keuze", int, waardes = range(len(keuzes)+1))
            else:
                ikeuze  =   invoer_validatie("keuze", int, waardes = range(1, len(keuzes)+1))
        
            return list(keuzes.values())[ikeuze-1] if bool(ikeuze) else STOP
    
    else:
        raise TypeError

def invoer_validatie(
    beschrijving: int,
    type: type,
    uitsluiten_leeg: bool = False,
    valideren: bool = False,
    **kwargs,
    ) -> int | str | float:
    
    while True:
        
        invoer  =   input(f"{beschrijving}: ")
        
        if invoer == "" and uitsluiten_leeg:
            print(f"invoer mag niet leeg zijn")
            continue
        
        if valideren:
            if not invoer_kiezen(f"bevestig {beschrijving} \"{invoer}\"", {"ja":  True, "nee": False}, kies_een = False):
                continue
        
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