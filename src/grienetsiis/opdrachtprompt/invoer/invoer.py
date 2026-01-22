import re
from typing import Dict, List, Literal, Tuple, TypeVar

import grienetsiis.opdrachtprompt.commando as commando
from grienetsiis.opdrachtprompt.constantes import TEKST_INDENTATIE


def invoeren(
    tekst_beschrijving: str,
    invoer_type: Literal["int", "float", "str", "bool"],
    invoer_annuleren: bool = True,
    tekst_annuleren: str = "stop",
    uitvoer_annuleren: commando.Commando = commando.STOP,
    tekst_indentatie: str = TEKST_INDENTATIE,
    uitsluiten_leeg: bool = False,
    valideren: bool = False,
    waardes_lijst: List[int | str | float] | None = None,
    waardes_bereik: Tuple[float, float] | None = None,
    waardes_regex: str | None = None,
    waardes_waar: Tuple[str, ...] = ("true", "waar", "juist", "1"),
    waardes_onwaar: Tuple[str, ...] = ("false", "onwaar", "onjuist", "0"),
    uitvoer_kleine_letters: bool = False,
    ) -> int | str | float:
    
    while True:
        
        invoer = input(f"{tekst_beschrijving}: ")
        
        if invoer_annuleren and invoer == tekst_annuleren:
            return uitvoer_annuleren
        
        if not invoer.strip() and uitsluiten_leeg:
            print(f"{tekst_indentatie}invoer mag niet leeg zijn")
            continue
        
        if valideren:
            if not kiezen(
                keuzes = {
                    "ja": True,
                    "nee": False,
                    },
                tekst_beschrijving = f"bevestig {tekst_beschrijving} \"{invoer}\"",
                tekst_kies_een = False,
                ):
                
                continue
        
        if invoer_type == "int":
            
            try:
                invoer = int(invoer)
            except ValueError:
                print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, enkel type \"{invoer_type}\" toegestaan")
                continue
            else:
                
                if waardes_lijst:
                    if invoer not in waardes_lijst:
                        print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, niet binnen de opties ({", ".join(f"{waarde}" for waarde in waardes_lijst)})")
                        continue
                
                if waardes_bereik:
                    if min(waardes_bereik) <= invoer <= max(waardes_bereik):
                        print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, moet tussen {min(waardes_bereik)} en {max(waardes_bereik)} liggen")
                        continue
                
                return invoer
        
        elif invoer_type == "float":
            
            try:
                invoer = float(invoer)
            except ValueError:
                print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, enkel type \"{invoer_type}\" toegestaan")
                continue
            else:
                
                if waardes_lijst:
                    if invoer not in waardes_lijst:
                        print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, niet binnen de opties ({", ".join(f"{float(waarde)}" for waarde in waardes_lijst)})")
                        continue
                
                if waardes_bereik:
                    if min(waardes_bereik) <= invoer <= max(waardes_bereik):
                        print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, moet tussen {min(waardes_bereik)} en {max(waardes_bereik)} liggen")
                        continue
                
                return invoer
        
        elif invoer_type == "str":
            
            if waardes_lijst:
                if invoer not in waardes_lijst:
                    print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, niet binnen de opties ({", ".join(f"\"{waarde}\"" for waarde in waardes_lijst)})")
                    continue
            
            if waardes_regex:
                patroon = re.compile(waardes_regex)
                match = patroon.match(invoer)
                
                if match:
                    return match.groupdict("")
                else:
                    print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, komt niet overeen met patroon \"{waardes_regex}\"")
                    continue
            
            if uitvoer_kleine_letters:
                return invoer.casefold()
            
            return invoer
        
        elif invoer_type == "bool":
            
            if invoer.casefold() in waardes_waar:
                return True
            elif invoer.casefold() in waardes_onwaar:
                return False
            
            print(f"{tekst_indentatie}invoer \"{invoer}\" incorrect, niet binnen de opties ({", ".join(f"\"{waarde}\"" for waarde in waardes_waar)}) of ({", ".join(f"\"{waarde}\"" for waarde in waardes_onwaar)})")

OPTIE = TypeVar("optie")
INDEX = TypeVar("index")

def kiezen(
    opties: Tuple[OPTIE] | List[OPTIE] | Dict[INDEX, OPTIE],
    tekst_beschrijving: str | None = None,
    tekst_kies_een: bool = True,
    keuze_annuleren: bool = True,
    tekst_annuleren: str = "stop",
    uitvoer_annuleren: commando.Commando = commando.STOP,
    tekst_indentatie: str = TEKST_INDENTATIE,
    keuze_meerdere: bool = False,
    keuze_terugkoppeling: bool = True,
    ) -> OPTIE | List[OPTIE]:
    
    if tekst_beschrijving:
        if tekst_kies_een:
            if keuze_meerdere:
                print(f"\nkies een {tekst_beschrijving} (één of meerdere)\n")
            else:
                print(f"\nkies een {tekst_beschrijving}\n")
        else:
            print(f"\n{tekst_beschrijving}\n")
    
    if isinstance(opties, (list, tuple)):
        
        opties_tonen = opties
        opties_geven = opties
    
    elif isinstance(opties, dict):
        
        opties_tonen = list(opties.keys())
        opties_geven = list(opties.values())
    
    index_minimaal = 1
    index_maximaal = len(opties)
    
    aantal_tekens = len(f"{index_maximaal}") + 2
        
    if keuze_annuleren:
        print(f" {f"[0]":>{aantal_tekens}} {tekst_annuleren}")

    [print(f" {f"[{ikeuze}]":>{aantal_tekens}} {keuze}") for ikeuze, keuze in enumerate(opties_tonen, 1)]
    print()
    
    if keuze_meerdere:
        
        while True:
            
            invoer_keuzes = invoeren(
                tekst_beschrijving = "keuze",
                invoer_type = "str",
                tekst_indentatie = tekst_indentatie,
                uitsluiten_leeg = True,
                )
            
            if keuze_annuleren and invoer_keuzes == "0":
                return uitvoer_annuleren
            
            index_keuzes = []
            
            invoer_keuzes_lijst = invoer_keuzes.split(",")
            
            for invoer_keuze in invoer_keuzes_lijst:
                
                if invoer_keuze.count("-") == 1:
                    getal_begin = invoer_keuze.split("-")[0]
                    getal_eind = invoer_keuze.split("-")[1]
                    
                    if not getal_begin.isnumeric():
                        print(f"{tekst_indentatie}invoer \"{invoer_keuzes}\" incorrect, startindex \"{getal_begin}\" in bereik \"{invoer_keuze}\" is geen index")
                        index_keuzes = []
                        break
                    
                    if not getal_eind.isnumeric():
                        print(f"{tekst_indentatie}invoer \"{invoer_keuzes}\" incorrect, eindindex \"{getal_eind}\" in bereik \"{invoer_keuze}\" is geen index")
                        index_keuzes = []
                        break
                    
                    if int(getal_begin) >= int(getal_eind):
                        print(f"{tekst_indentatie}invoer \"{invoer_keuzes}\" incorrect, eindindex \"{getal_eind}\" moet groter zijn dan startindex \"{getal_begin}\" in bereik \"{invoer_keuze}\"")
                        index_keuzes = []
                        break
                    
                    if int(getal_begin) < index_minimaal:
                        print(f"{tekst_indentatie}invoer \"{invoer_keuzes}\" incorrect, startindex \"{getal_begin}\" moet groter dan of gelijk zijn aan \"{index_minimaal}\" in bereik \"{invoer_keuze}\"")
                        index_keuzes = []
                        break
                    
                    if int(getal_eind) > index_maximaal:
                        print(f"{tekst_indentatie}invoer \"{invoer_keuzes}\" incorrect, eindindex \"{getal_eind}\" moet kleiner dan of gelijk zijn aan \"{index_maximaal}\" in bereik \"{invoer_keuze}\"")
                        index_keuzes = []
                        break
                    
                    for index in range(int(getal_begin), int(getal_eind) + 1):
                        index_keuzes.append(index)
                
                elif invoer_keuze.count("-") > 1:
                    print(f"{tekst_indentatie}invoer \"{invoer_keuzes}\" incorrect, bereik \"{invoer_keuze}\" bevat meer dan twee strepen")
                    index_keuzes = []
                    break
                
                elif invoer_keuze.isnumeric():
                    if index_minimaal <= int(invoer_keuze) <= index_maximaal:
                        index_keuzes.append(int(invoer_keuze))
                    else:
                        print(f"{tekst_indentatie}invoer \"{invoer_keuzes}\" incorrect, waarde \"{invoer_keuze}\" moet tussen {index_minimaal} en {index_maximaal} liggen")
                        index_keuzes = []
                        break
                
                else:
                    print(f"{tekst_indentatie}invoer \"{invoer_keuzes}\" incorrect, waarde \"{invoer_keuze}\" is geen index")
                    index_keuzes = []
                    break
            
            if not index_keuzes:
                continue
            
            keuze = [opties_geven[index_keuze-1] for index_keuze in set(index_keuzes)]
            break
    
    else:
        
        if keuze_annuleren:
            index_keuze = invoeren(
                tekst_beschrijving = "keuze",
                invoer_type = "int",
                waardes_lijst = range(index_maximaal+1),
                )
        
        else:
            index_keuze = invoeren(
                tekst_beschrijving = "keuze",
                invoer_type = "int",
                waardes_lijst = range(index_minimaal, index_maximaal+1),
                )
        
        keuze =  opties_geven[index_keuze-1] if bool(index_keuze) else uitvoer_annuleren
    
    if keuze_terugkoppeling:
        if isinstance(keuze, list):
            print(f"{tekst_indentatie}gekozen: ({", ".join(_keuze for _keuze in keuze)})")
        else:
            print(f"{tekst_indentatie}gekozen: {keuze}")
    
    return keuze