from __future__ import annotations
from typing import List, Literal, Type, TYPE_CHECKING

from grienetsiis.opdrachtprompt.invoer import kiezen

if TYPE_CHECKING:
    from .geregistreerd_object import GeregistreerdObject


class Subregister(dict):
    
    # DUNDER METHODS
    
    def __init__(
        self,
        geregistreerd_type: Type
        ):
        
        self.geregistreerd_type = geregistreerd_type
    
    # INSTANCE METHODS
    
    def filter(
        self,
        methode: Literal["of", "en"] = "of",
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
    
    def kiezen(
        self,
        geef_id = True,
        nieuw_toestaan = True,
        ) -> str:
        
        opties = {f"{geregistreerd_object}": id for id, geregistreerd_object in self.items()}
        
        if nieuw_toestaan:
            opties = {f"nieuw {self.geregistreerd_type.__name__.lower()}": "nieuw"} | opties
        
        keuze_optie = kiezen(
            opties = opties,
            tekst_beschrijving = f"{self.geregistreerd_type.__name__.lower()}",
            )
        
        if keuze_optie == "nieuw":
            id = self.nieuw()
        else:
            id = keuze_optie
        
        if geef_id:
            return id
        else:
            return self[id]
    
    def nieuw(
        self,
        geef_id: bool = True,
        ):
        
        print(f"maak een nieuw {self.geregistreerd_type.__name__.lower()}")
        
        basis_type = self.geregistreerd_type.nieuw({sleutel: veld for sleutel, veld in self.geregistreerd_type.__annotations__.items() if sleutel not in self.geregistreerd_type.__dict__})
        
        if geef_id:
            return getattr(basis_type, basis_type._id_veld)
        return basis_type
    
    def verwijderen(self):
        
        id = self.kiezen(nieuw_toestaan = False)
        del self[id]
    
    # PROPERTIES
    
    @property
    def lijst(self) -> List[GeregistreerdObject]:
        return list(self.values())