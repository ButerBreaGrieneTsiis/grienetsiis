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
    __TEKST_ANNULEREN: ClassVar[str] = "terug naar"
    __UITVOER_ANNULEREN: ClassVar[str] = commando.TERUG
    
    # DUNDER METHODS
    
    def __call__(self):
        
        if self.opties:
            
            if self.is_submenu:
                keuze = kiezen(
                    opties = self.opties,
                    tekst_beschrijving = f"{str(self).capitalize()}: kies een optie",
                    tekst_kies_een = False,
                    keuze_annuleren = True,
                    tekst_annuleren = self.__TEKST_ANNULEREN + f" {self.super_menu.naam}",
                    uitvoer_annuleren = self.__UITVOER_ANNULEREN,
                    )
            else:
                keuze = kiezen(
                    opties = self.opties,
                    tekst_beschrijving = f"{str(self).capitalize()}: kies een optie",
                    tekst_kies_een = False,
                    keuze_annuleren = False,
                    )
            
            if self.is_submenu and keuze is self.__UITVOER_ANNULEREN:
                self.super_menu()
            else:
                if callable(keuze):
                    keuze()
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