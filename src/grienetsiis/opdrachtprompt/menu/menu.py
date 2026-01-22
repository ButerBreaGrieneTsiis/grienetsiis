from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, ClassVar, Dict, List, TypeVar

from grienetsiis.opdrachtprompt.invoer import kiezen
import grienetsiis.opdrachtprompt.commando as commando
from grienetsiis.opdrachtprompt.constantes import TEKST_INDENTATIE


OPTIE = TypeVar("optie")
INDEX = TypeVar("index")

@dataclass
class Menu:
    
    naam: str
    super_menu: Menu | None = None
    
    # interne variabelen
    _opties: List[OPTIE] | Dict[INDEX, OPTIE] | None = None
    
    # class variables
    __TEKST_ANNULEREN: ClassVar[str] = "terug naar"
    __UITVOER_ANNULEREN: ClassVar[str] = commando.TERUG
    
    # DUNDER METHODS
    
    def __call__(self):
        
        if self.opties:
            
            if self.is_submenu:
                keuze = kiezen(
                    opties = self.opties,
                    keuze_annuleren = True,
                    tekst_annuleren = self.__TEKST_ANNULEREN + f" {self.super_menu.naam}",
                    uitvoer_annuleren = self.__UITVOER_ANNULEREN,
                    )
            else:
                keuze = kiezen(
                    opties = self.opties,
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
                print(f"{TEKST_INDENTATIE}menu {self.naam} bevat geen opties, terug naar menu erboven.\n")
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
        
        if index is not None and isinstance(self, list):
            raise ValueError(f"geïndexeerde opties niet mogelijk")
        
        if index is None:
            if self._opties is None:
                self._opties = []
            self._opties.append(optie)
        else:
            if self._opties is None:
                self._opties = {}
            self._opties[index] = optie
    
    # PROPERTIES
    
    @property
    def opties(self) -> Dict[INDEX, OPTIE]:
        if self._opties is None:
            return None
        
        if isinstance(self._opties, list):
            return {_optie: _optie for _optie in self._opties}
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
    menu_kaas.toevoegen_optie("jong belegen")
    menu_kaas.toevoegen_optie("belegen")
    
    menu()