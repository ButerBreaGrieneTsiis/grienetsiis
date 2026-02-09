from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, Dict, List, TypeVar

from grienetsiis.opdrachtprompt.invoer import kiezen
from grienetsiis.opdrachtprompt import commando
from grienetsiis.opdrachtprompt.constantes import TEKST_INDENTATIE


OPTIE = TypeVar("optie")
INDEX = TypeVar("index")

@dataclass
class Menu:
    
    naam: str
    super_menu: Menu | None = None
    
    # interne variabelen
    _opties: Dict[INDEX, OPTIE] | None = None
    
    # class variables
    _TEKST_ANNULEREN: ClassVar[str] = "terug naar"
    _TEKST_AFSLUITEN: ClassVar[str] = "afsluiten"
    _UITVOER_ANNULEREN: ClassVar[commando] = commando.TERUG
    _UITVOER_AFSLUITEN: ClassVar[commando] = commando.STOP
    
    # DUNDER METHODS
    
    def __call__(self):
        
        if self.opties:
            
            if self.is_submenu:
                keuze = kiezen(
                    opties = self.opties,
                    tekst_beschrijving = f"{str(self).capitalize()}: kies een optie",
                    tekst_kies_een = False,
                    keuze_annuleren = True,
                    tekst_annuleren = self._TEKST_ANNULEREN + f" {self.super_menu.naam}",
                    uitvoer_annuleren = self._UITVOER_ANNULEREN,
                    )
            else:
                keuze = kiezen(
                    opties = self.opties,
                    tekst_beschrijving = f"{str(self).capitalize()}: kies een optie",
                    tekst_kies_een = False,
                    keuze_annuleren = True,
                    tekst_annuleren = self._TEKST_AFSLUITEN,
                    uitvoer_annuleren = self._UITVOER_AFSLUITEN,
                    )
            
            if keuze is self._UITVOER_AFSLUITEN:
                return 0
            
            if keuze is self._UITVOER_ANNULEREN:
                return self.super_menu()
            
            if callable(keuze):
                if not isinstance(keuze, Menu):
                    keuze()
                    return self()
                else:
                    return keuze()
            else:
                return keuze
        
        else:
            if self.is_hoofdmenu:
                raise RuntimeError("Menu bevat geen opties en is een hoofdmenu, kan niet uitgevoerd worden.")
            else:
                print(f"{TEKST_INDENTATIE}menu {self.naam} bevat geen opties, terug naar menu erboven.")
                self.super_menu()
    
    def __hash__(self) -> int:
        return hash(self.naam)
    
    def __repr__(self) -> str:
        return f"menu {self.naam}"
    
    # INSTANCE METHODS
    
    def toevoegen_optie(
        self,
        optie: OPTIE,
        index: INDEX | None = None,
        ):
        
        if self._opties is None:
            self._opties = {}
        
        if index is None:
            self._opties[optie] = optie
        else:
            self._opties[index] = optie
    
    # PROPERTIES
    
    @property
    def opties(self) -> Dict[INDEX, OPTIE]:
        return self._opties
    
    @property
    def is_hoofdmenu(self) -> bool:
        return self.super_menu is None
    
    @property
    def is_submenu(self) -> bool:
        return self.super_menu is not None

if __name__ == "__main__":
    
    menu = Menu("hoofdmenu")
    menu_kip = Menu("kip", super_menu = menu)
    menu_kaas = Menu("kaas", super_menu = menu)
    
    menu.toevoegen_optie(menu_kip)
    menu.toevoegen_optie(menu_kaas)
    menu.toevoegen_optie(lambda: print("1234"))
    
    menu_kaas.toevoegen_optie("jong")
    menu_kaas.toevoegen_optie("jong belegen", "kaas jonge")
    menu_kaas.toevoegen_optie("belegen")
    
    menu()