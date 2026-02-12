from __future__ import annotations
from typing import Dict, List, Literal, TYPE_CHECKING

from grienetsiis.opdrachtprompt.invoer import invoeren, kiezen
from grienetsiis.opdrachtprompt import commando

if TYPE_CHECKING:
    from .geregistreerd_object import GeregistreerdObject


class Subregister(dict):
    
    # DUNDER METHODS
    
    def __init__(
        self,
        geregistreerd_type: GeregistreerdObject
        ):
        
        self.geregistreerd_type = geregistreerd_type
    
    # INSTANCE METHODS
    
    def filter(
        self,
        methode: Literal["of", "en"] = "en",
        **filters,
        ) -> Subregister:
        
        subregister = Subregister(geregistreerd_type = self.geregistreerd_type)
        
        for id, geregistreerd_object in self.items():
            
            masker = []
            
            for sleutel, waardes in filters.items():
                if isinstance(waardes, list):
                    for waarde in waardes:
                        if getattr(geregistreerd_object, sleutel, None) == waarde:
                            masker.append(True)
                            break
                    else:
                        masker.append(False)
                
                else:
                    if getattr(geregistreerd_object, sleutel, None) == waardes:
                        masker.append(True)
                    else:
                        masker.append(False)
            
            if methode == "en":
                if all(masker):
                    subregister[id] = geregistreerd_object
            else:
                if any(masker):
                    subregister[id] = geregistreerd_object
        
        return subregister
    
    def selecteren(
        self,
        geef_id: bool = True,
        nieuw_toestaan: bool = True,
        ) -> str | GeregistreerdObject:
        
        opties = {id: f"{geregistreerd_object}" for id, geregistreerd_object in self.items()}
        
        if nieuw_toestaan:
            opties = {"nieuw": f"nieuw {self.geregistreerd_type.__name__.lower()}"} | opties
        
        keuze_optie = kiezen(
            opties = opties,
            tekst_beschrijving = f"{self.geregistreerd_type.__name__.lower()}",
            )
        
        if keuze_optie is commando.STOP:
            return commando.STOP
        elif keuze_optie == "nieuw":
            id = self.nieuw()
        else:
            id = keuze_optie
        
        if geef_id:
            return id
        else:
            return self[id]
    
    def zoeken(
        self,
        veld: str | None = None,
        geef_id: bool = True,
        ) -> str | GeregistreerdObject:
        
        if not veld:
            veld = self.selecteren_veld()
        
        if veld is commando.STOP:
            return commando.STOP
        
        zoekterm = invoeren(
            tekst_beschrijving = veld,
            invoer_type = self.velden[veld],
            uitsluiten_leeg = True,
            )
        
        filter = {veld: zoekterm}
        subregister_gefilterd = self.filter(**filter)
        
        if len(subregister_gefilterd) == 0:
            print(f">>> geen {self.geregistreerd_type.__name__.lower()} aanwezig voor \"{veld} = {zoekterm}\"")
            return None
        if len(subregister_gefilterd) == 1:
            print(f">>> één {self.geregistreerd_type.__name__.lower()} aanwezig voor \"{veld} = {zoekterm}\"")
            if geef_id:
                return list(subregister_gefilterd.keys())[0]
            else:
                return list(subregister_gefilterd.values())[0]
        
        return subregister_gefilterd.selecteren(geef_id = geef_id)
    
    def nieuw(
        self,
        geef_id: bool = True,
        ):
        
        geregistreerd_object = self.geregistreerd_type.nieuw()
        
        if geef_id:
            return getattr(geregistreerd_object, geregistreerd_object._ID_VELD)
        return geregistreerd_object
    
    def verwijderen(
        self,
        id: str | None = None,
        ):
        
        if len(self) == 0:
            print(f"\n>>> geen {self.geregistreerd_type.__name__.lower()} aanwezig")
            return None
        
        if id is None:
            id = self.selecteren(nieuw_toestaan = False)
        
        if id is commando.STOP:
            return None
        
        del self[id]
    
    def weergeven(self) -> None:
        
        print()
        if len(self) == 0:
            print(f">>> geen {self.geregistreerd_type.__name__.lower()} aanwezig")
        else:
            for registreerd_object in self.lijst:
                print(f"    {registreerd_object}")
    
    def selecteren_veld(self) -> str | commando.Commando:
        return kiezen(
            opties = list(self.velden.keys()),
            tekst_beschrijving = "veld",
            )
    
    # PROPERTIES
    
    @property
    def lijst(self) -> List[GeregistreerdObject]:
        return list(self.values())
    
    @property
    def velden(self) -> Dict[str, type]:
        return {veld: type for veld, type in self.geregistreerd_type.__annotations__.items() if type in ("int", "str", "float", "bool")}