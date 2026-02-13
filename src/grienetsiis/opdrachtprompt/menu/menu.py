from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, ClassVar, Dict

from grienetsiis.opdrachtprompt.invoer import kiezen
from grienetsiis.opdrachtprompt import commando
from grienetsiis.opdrachtprompt.constantes import TEKST_INDENTATIE


@dataclass
class Menu:
    
    naam: str
    super_menu: Menu | None = None
    blijf_in_menu: bool = True
    
    # interne variabelen
    _opties: Dict[Callable, Callable | str] | None = None
    
    # class variables
    _TEKST_ANNULEREN: ClassVar[str] = "terug naar"
    _TEKST_AFSLUITEN: ClassVar[str] = "afsluiten"
    
    # DUNDER METHODS
    
    def __call__(self):
        
        while True:
            
            if not self.opties:
                if self.is_hoofdmenu:
                    raise RuntimeError("Menu bevat geen opties en is een hoofdmenu, kan niet uitgevoerd worden.")
                else:
                    print(f"{TEKST_INDENTATIE}menu {self.naam} bevat geen opties, terug naar menu erboven.")
                    break
            
            if self.is_submenu:
                tekst_annuleren = self._TEKST_ANNULEREN + f" {self.super_menu.naam}"
            else:
                tekst_annuleren = self._TEKST_AFSLUITEN
            
            keuze = kiezen(
                opties = self.opties,
                tekst_beschrijving = f"{str(self)}: kies een optie",
                tekst_kies_een = False,
                keuze_annuleren = True,
                tekst_annuleren = tekst_annuleren,
                )
            
            uitvoer = keuze()
            
            if uitvoer is commando.STOP:
                break
            if uitvoer is commando.DOORGAAN or self.blijf_in_menu:
                continue
            
            break
    
    def __hash__(self) -> int:
        return hash(self.naam)
    
    def __repr__(self) -> str:
        return f"{self.naam}"
    
    # INSTANCE METHODS
    
    def toevoegen_optie(
        self,
        optie: Callable,
        optie_tonen: str | None = None,
        ):
        
        if not callable(optie):
            raise TypeError(f"optie moet oproepbaar zijn, niet type {type(optie)}")
        
        if self._opties is None:
            self._opties = {}
        
        if optie_tonen is None:
            self._opties[optie] = optie
        else:
            self._opties[optie] = optie_tonen
    
    # PROPERTIES
    
    @property
    def opties(self) -> Dict[Callable, Callable | str]:
        return self._opties
    
    @property
    def is_hoofdmenu(self) -> bool:
        return self.super_menu is None
    
    @property
    def is_submenu(self) -> bool:
        return self.super_menu is not None