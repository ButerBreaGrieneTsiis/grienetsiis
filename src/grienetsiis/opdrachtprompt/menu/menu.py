from __future__ import annotations
from typing import Callable, ClassVar, Dict

from grienetsiis.opdrachtprompt.invoer import kiezen
from grienetsiis.opdrachtprompt import commando
from grienetsiis.opdrachtprompt.constantes import TEKST_INDENTATIE


class Menu:
    
    # class variables
    _TEKST_ANNULEREN: ClassVar[str] = "terug naar"
    _TEKST_AFSLUITEN: ClassVar[str] = "afsluiten"
    
    # DUNDER METHODS
    
    def __init__(
        self,
        naam: str | Callable,
        naam_super: Menu | str | None = None,
        blijf_in_menu: bool = True,
        functie_start: Callable | None = None,
        functie_eind: Callable | None = None,
        ) -> None:
        
        self.naam = naam
        self.naam_super = naam_super
        self.blijf_in_menu = blijf_in_menu
        self.functie_start = functie_start
        self.functie_eind = functie_eind
        
        self._opties = None
    
    def __call__(self) -> None:
        
        if callable(self.functie_start): self.functie_start()
        
        while True:
            
            if not self.opties:
                if self.is_hoofdmenu:
                    raise RuntimeError("Menu bevat geen opties en is een hoofdmenu, kan niet uitgevoerd worden.")
                else:
                    print(f"{TEKST_INDENTATIE}menu {self.naam_super} bevat geen opties, terug naar menu erboven.")
                    break
            
            if self.is_hoofdmenu:
                tekst_annuleren = self._TEKST_AFSLUITEN
            else:
                tekst_annuleren = self._TEKST_ANNULEREN + f" {self.naam_super}"
            
            keuze = kiezen(
                opties = self.opties,
                tekst_beschrijving = f"{self.naam}: kies een optie",
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
        
        if callable(self.functie_eind): self.functie_eind()
    
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
    def naam(self) -> str:
        if callable(self._naam):
            return self._naam()
        else:
            return self._naam
    
    @naam.setter
    def naam(self, waarde: str | Callable) -> None:
        self._naam = waarde
    
    @property
    def naam_super(self) -> str:
        return self._naam_super
    
    @naam_super.setter
    def naam_super(self, waarde: Menu | str | None) -> None:
        if isinstance(waarde, Menu):
            self._naam_super = waarde.naam
        else:
            self._naam_super = waarde
    
    @property
    def opties(self) -> Dict[Callable, Callable | str]:
        return self._opties
    
    @property
    def is_hoofdmenu(self) -> bool:
        return self.naam_super is None
    
    @property
    def is_submenu(self) -> bool:
        return self.naam_super is not None