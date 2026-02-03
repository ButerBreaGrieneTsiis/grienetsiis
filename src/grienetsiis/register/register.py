from __future__ import annotations
import logging
from pathlib import Path
from typing import Any, Callable, ClassVar, Dict, List, Literal, TYPE_CHECKING
from uuid import uuid4

from .subregister import Subregister
from grienetsiis.json import Ontcijferaar, Vercijferaar, openen_json, opslaan_json
from grienetsiis.types import Singleton

if TYPE_CHECKING:
    from enum import Enum
    
    from .geregistreerd_object import GeregistreerdObject


logger = logging.getLogger(__name__)

class Register(dict, metaclass = Singleton):
    
    _SUBREGISTERS: ClassVar[Dict[str, Dict[str, Any]]] = {}
    _REGISTRATIE_METHODE: ClassVar[Literal["uuid"]] | None = None
    _BESTANDSMAP: ClassVar[Path] | None = None
    _INGESTELD: ClassVar[bool] = False
    
    _REGISTREER: ClassVar[bool] = True
    
    # DUNDER METHODS
    
    def __getattr__(self, naam):
        if naam not in self._SUBREGISTERS:
            raise ValueError(f"ongeregistreerd type \"{naam}\"")
        
        if naam not in self:
            self[naam] = Subregister(type = self.TYPES[naam])
        return self[naam]
    
    # CLASS METHODS
    
    @classmethod
    def openen(cls) -> Register:
        
        register = cls()
        
        register._REGISTREER = False
        
        for subregister_naam, subregister_dict in register._SUBREGISTERS.items():
            
            register[subregister_naam] = Subregister(subregister_dict["type"])
            
            if not subregister_dict["opslaan"]:
                continue
            
            bestandspad = subregister_dict["bestandsmap"] / f"{subregister_dict["bestandsnaam"]}.{subregister_dict["extensie"]}"
            
            for map in reversed(bestandspad.parents):
                if not map.exists():
                    map.mkdir()
            
            if bestandspad.is_file():
                
                if subregister_dict["vercijfer_methode"] == "standaard":
                    geregistreerde_objecten = openen_json(
                        bestandspad = bestandspad,
                        ontcijfer_standaard_objecten = subregister_dict["ontcijfer_standaard_objecten"],
                        ontcijfer_enum = subregister_dict["enums"],
                        )
                else:
                    geregistreerde_objecten = openen_json(
                        bestandspad = bestandspad,
                        ontcijfer_functie_object = subregister_dict["ontcijfer_functie_objecten"],
                        ontcijfer_functie_subobjecten = subregister_dict["ontcijfer_functie_subobjecten"],
                        ontcijfer_enum = subregister_dict["enums"],
                        )
                
                for uuid, geregistreerd_object in geregistreerde_objecten.items():
                    
                    geregistreerd_object.uuid = uuid
                    register[subregister_naam][uuid] = geregistreerd_object
        
        register._REGISTREER = True
        
        return register
    
    # INSTANCE METHODS
    
    def opslaan(self) -> None: 
        
        for subregister_naam, subregister_dict in self._SUBREGISTERS.items():
            
            if subregister_dict["opslaan"]:
                
                if subregister_dict["vercijfer_methode"] == "standaard":
                    opslaan_json(
                        object = self[subregister_naam],
                        bestandspad = subregister_dict["bestandsmap"],
                        bestandsnaam = subregister_dict["bestandsnaam"],
                        extensie = subregister_dict["extensie"],
                        vercijfer_standaard_objecten = subregister_dict["vercijfer_standaard_objecten"],
                        vercijfer_standaard_overslaan = subregister_dict["vercijfer_standaard_overslaan"],
                        vercijfer_enum = subregister_dict["enums"],
                        )
                else:
                    opslaan_json(
                        object = self[subregister_naam],
                        bestandspad = subregister_dict["bestandsmap"],
                        bestandsnaam = subregister_dict["bestandsnaam"],
                        extensie = subregister_dict["extensie"],
                        vercijfer_functie_object = subregister_dict["vercijfer_functie_objecten"],
                        vercijfer_functie_subobjecten = subregister_dict["vercijfer_functie_subobjecten"],
                        vercijfer_enum = subregister_dict["enums"],
                        )
    
    def registreer_instantie(
        self,
        instantie: object,
        ) -> None:
        
        if self._REGISTREER:
            
            if self._REGISTRATIE_METHODE == "uuid":
                instantie.uuid = str(uuid4())
            
            subregister_naam = instantie._SUBREGISTER_NAAM
            
            if subregister_naam not in self:
                self[subregister_naam] = Subregister(instantie.__class__)
            
            self[subregister_naam][instantie.uuid] = instantie
    
    # STATIC METHODS
    
    @staticmethod
    def instellen(
        registratie_methode: Literal["uuid"],
        bestandsmap: Path,
        ) -> None:
        
        Register._REGISTRATIE_METHODE = registratie_methode
        Register._BESTANDSMAP = bestandsmap
        Register._INGESTELD = True
    
    @staticmethod
    def registreer_type(
        geregistreerd_type: GeregistreerdObject,
        subregister_naam: str,
        opslaan: bool = True,
        bestandsmap: Path | None = None,
        bestandsnaam: str | None = None,
        extensie: str = "json",
        vercijfer_methode: Literal["functie", "standaard"] = "standaard",
        vercijfer_functie_objecten: Callable | None = None, # bij "functie", sla het object zelf op met deze functie (getattr(object, vercijfer_functie)())
        ontcijfer_functie_objecten: Callable | None = None,
        vercijfer_functie_subobjecten: List[Vercijferaar] | None = None,
        ontcijfer_functie_subobjecten: List[Ontcijferaar] | None = None,
        ontcijfer_standaard_objecten: Dict[str, Callable] | None = None,
        vercijfer_standaard_objecten: List[str] | None = None, # bij "standaard", sla deze types op met __class__
        vercijfer_standaard_overslaan: List[str] | None = ["uuid"],
        enums: Dict[str, Enum] | None = None,
        ) -> None:
        
        if not Register._INGESTELD:
            logger.error("Register moest eerst ingesteld worden met Register.instellen()")
        
        geregistreerd_type._id_veld = Register._REGISTRATIE_METHODE
        
        geregistreerd_type_naam = geregistreerd_type.__name__
        
        if subregister_naam not in Register._SUBREGISTERS:
            
            subregister_dict = {
                "type": geregistreerd_type,
                "opslaan": opslaan,
                }
            
            if opslaan:
                
                if bestandsmap is None:
                    bestandsmap = Register._BESTANDSMAP
                    logger.warning(f"type \"{geregistreerd_type_naam}\" geen bestandsmap: ingesteld als \"{Register._BESTANDSMAP}\"")
                
                if bestandsnaam is None:
                    bestandsnaam = subregister_naam
                    logger.warning(f"type \"{geregistreerd_type_naam}\" geen bestandsnaam: ingesteld als \"{subregister_naam}\"")
                
                subregister_dict["bestandsmap"] = bestandsmap
                subregister_dict["bestandsnaam"] = bestandsnaam
                subregister_dict["extensie"] = extensie
                subregister_dict["vercijfer_methode"] = vercijfer_methode
                subregister_dict["enums"] = enums
                
                if vercijfer_methode == "standaard":
                    if vercijfer_standaard_objecten is None:
                        subregister_dict["vercijfer_standaard_objecten"] = [geregistreerd_type_naam]
                    else:
                        if geregistreerd_type_naam not in vercijfer_standaard_objecten:
                            logger.warning(f"veld \"vercijfer_standaard\" afwezig voor type \"{geregistreerd_type_naam}\": toegevoegd")
                            vercijfer_standaard_objecten.append(geregistreerd_type_naam)
                        subregister_dict["vercijfer_standaard_objecten"] = vercijfer_standaard_objecten
                    
                    subregister_dict["vercijfer_standaard_overslaan"] = vercijfer_standaard_overslaan
                    
                    if ontcijfer_standaard_objecten is None:
                        logger.warning(f"veld \"ontcijfer_standaard\" afwezig voor type \"{geregistreerd_type_naam}\": standaardmethode \"{geregistreerd_type_naam}.van_json() toegevoegd\"")
                        subregister_dict["ontcijfer_standaard_objecten"] = {geregistreerd_type_naam: geregistreerd_type}
                    else:
                        subregister_dict["ontcijfer_standaard_objecten"] = ontcijfer_standaard_objecten
                
                elif vercijfer_methode == "functie":
                    subregister_dict["vercijfer_functie_objecten"] = vercijfer_functie_objecten
                    subregister_dict["vercijfer_functie_subobjecten"] = vercijfer_functie_subobjecten
                    subregister_dict["ontcijfer_functie_objecten"] = ontcijfer_functie_objecten
                    subregister_dict["ontcijfer_functie_subobjecten"] = ontcijfer_functie_subobjecten
            
            Register._SUBREGISTERS[subregister_naam] = subregister_dict