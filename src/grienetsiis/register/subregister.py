from __future__ import annotations
from typing import Dict, List, Literal, TYPE_CHECKING

from grienetsiis.opdrachtprompt.invoer import invoeren, kiezen
from grienetsiis.opdrachtprompt import commando

if TYPE_CHECKING:
    from grienetsiis.register import GeregistreerdObject


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
        filters_inclusief: bool = True,
        filters_exact_overeenkomend: bool = True,
        **filters,
        ) -> Subregister:
        
        subregister_gefilterd = Subregister(geregistreerd_type = self.geregistreerd_type)
        
        for id, geregistreerd_object in self.items():
            
            masker = []
            
            for sleutel, waardes in filters.items():
                
                if not hasattr(geregistreerd_object, sleutel):
                    masker.append(False)
                    continue
                
                if not isinstance(waardes, list):
                    waardes = [waardes]
                for waarde in waardes:
                    if filters_exact_overeenkomend:
                        if waarde == getattr(geregistreerd_object, sleutel):
                            masker.append(True)
                            break
                    else:
                        if waarde in getattr(geregistreerd_object, sleutel):
                            masker.append(True)
                            break
                else:
                    masker.append(False)
            
            if filters_inclusief:
                if all(masker):
                    subregister_gefilterd[id] = geregistreerd_object
            else:
                if any(masker):
                    subregister_gefilterd[id] = geregistreerd_object
        
        return subregister_gefilterd
    
    def selecteren(
        self,
        geef_id: bool = True,
        toestaan_nieuw: bool = True,
        terug_naar: str = "terug",
        ) -> str | GeregistreerdObject | None | commando.Stop:
        
        if len(self) == 0:
            print(f"\n>>> geen {self.geregistreerd_type.__name__.lower()} aanwezig")
            if toestaan_nieuw:
                id = self.nieuw()
            else:
                return None
        
        else:
            opties = {id: f"{geregistreerd_object}" for id, geregistreerd_object in self.items()}
            
            if toestaan_nieuw:
                opties = {"nieuw": f"nieuw {self.geregistreerd_type.__name__.lower()}"} | opties
            
            keuze_optie = kiezen(
                opties = opties,
                tekst_beschrijving = f"{self.geregistreerd_type.__name__.lower()}",
                tekst_annuleren = terug_naar,
                )
            
            if keuze_optie is commando.STOP:
                return commando.STOP
            elif keuze_optie == "nieuw":
                id = self.nieuw(geef_id = True)
                if id is commando.STOP:
                    return commando.STOP
            else:
                id = keuze_optie
        
        if id is None:
            return None
        if geef_id:
            return id
        return self[id]
    
    def zoeken(
        self,
        veld: str | None = None,
        veld_exact_overeenkomend: bool = True,
        geef_id: bool = True,
        ) -> str | GeregistreerdObject | None | commando.Stop:
        
        if len(self) == 0:
            print(f"\n>>> geen {self.geregistreerd_type.__name__.lower()} aanwezig")
            return None
        
        if not veld:
            veld = self.selecteren_veld()
            if veld is commando.STOP:
                return commando.STOP
        
        zoekterm = invoeren(
            tekst_beschrijving = veld,
            invoer_type = self.velden[veld],
            uitsluiten_leeg = True,
            )
        if zoekterm is commando.STOP:
            return commando.STOP
        
        filter = {veld: zoekterm}
        subregister_gefilterd = self.filter(
            filters_inclusief = True,
            filters_exact_overeenkomend = veld_exact_overeenkomend,
            **filter,
            )
        
        if len(subregister_gefilterd) == 0:
            print(f">>> geen {self.geregistreerd_type.__name__.lower()} aanwezig voor \"{veld} = {zoekterm}\"")
            return None
        if len(subregister_gefilterd) == 1:
            print(f">>> één {self.geregistreerd_type.__name__.lower()} aanwezig voor \"{veld} = {zoekterm}\" ({list(subregister_gefilterd.values())[0]})")
            if geef_id:
                return list(subregister_gefilterd.keys())[0]
            else:
                return list(subregister_gefilterd.values())[0]
        
        return subregister_gefilterd.selecteren(geef_id = geef_id)
    
    def nieuw(
        self,
        geef_id: bool = True,
        ) -> str | GeregistreerdObject | None:
        
        geregistreerd_object = self.geregistreerd_type.nieuw()
        
        if not isinstance(geregistreerd_object, self.geregistreerd_type):
            return None
        
        if geef_id:
            return geregistreerd_object._id
        return geregistreerd_object
    
    def verwijderen(
        self,
        id: str | None = None,
        ) -> None:
        
        if len(self) == 0:
            print(f"\n>>> geen {self.geregistreerd_type.__name__.lower()} aanwezig")
            return None
        
        if id is None:
            id = self.selecteren(toestaan_nieuw = False)
        
        if id is not commando.STOP and id is not None:
            print(f"\n>>> {self[id]} verwijderd")
            del self[id]
    
    def weergeven(self) -> None:
        
        print()
        if len(self) == 0:
            print(f">>> geen {self.geregistreerd_type.__name__.lower()} aanwezig")
        else:
            for registreerd_object in self.lijst:
                print(f"    {registreerd_object}")
    
    def selecteren_veld(self) -> str | commando.Stop:
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