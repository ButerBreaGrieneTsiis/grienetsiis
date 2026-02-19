from __future__ import annotations
import datetime as dt
import logging
from pathlib import Path
from typing import Any, Callable, ClassVar, Dict, List, Literal, TYPE_CHECKING
from uuid import uuid4

from grienetsiis.json import Ontcijferaar, Vercijferaar, openen_json, opslaan_json
from grienetsiis.register import Subregister
from grienetsiis.types import Singleton

if TYPE_CHECKING:
    from enum import Enum
    
    from grienetsiis.register import GeregistreerdObject


logger = logging.getLogger(__name__)

class Register(dict, metaclass = Singleton):
    
    _SUBREGISTERS: ClassVar[Dict[str, Dict[str, Any]]] = {}
    _BESTANDSMAP: ClassVar[Path] | None = None
    _BESTANDSMAP_KOPIE: ClassVar[Path] | None = None
    _INGESTELD: ClassVar[bool] = False
    
    _REGISTREER: ClassVar[bool] = True
    
    # DUNDER METHODS
    
    def __getattr__(self, naam):
        if naam not in self._SUBREGISTERS:
            raise ValueError(f"ongeregistreerd type \"{naam}\"")
        
        if naam not in self:
            self[naam] = Subregister(type = self.TYPES[naam])
        return self[naam]
    
    # STATIC METHODS
    
    @staticmethod
    def openen() -> Register:
        
        register = Register()
        
        Register._REGISTREER = False
        
        for subregister_naam, subregister_dict in register._SUBREGISTERS.items():
            
            register[subregister_naam] = Subregister(subregister_dict["type"])
            
            if subregister_dict["opslaan"] == "niet":
                continue
            
            bestandspad = subregister_dict["bestandsmap"] / f"{subregister_dict["bestandsnaam"]}.{subregister_dict["extensie"]}"
            
            for map in reversed(bestandspad.parents):
                if not map.exists():
                    map.mkdir()
            
            if not bestandspad.is_file():
                continue
            
            if subregister_dict["opslaan"] == "register":
                
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
                
                for id, geregistreerd_object in geregistreerde_objecten.items():
                    
                    if geregistreerd_object._REGISTRATIE_METHODE in ("uuid", "datum", "datumtijd"):
                        geregistreerd_object._id = id
                    register[subregister_naam][id] = geregistreerd_object
                    register[subregister_naam].geregistreerde_instanties.append(id)
            
            elif subregister_dict["opslaan"] == "instantie":
                
                geregistreerde_instanties = openen_json(
                    bestandspad = bestandspad,
                    )
                register[subregister_naam].geregistreerde_instanties = geregistreerde_instanties
        
        Register._REGISTREER = True
        
        return register
    
    @staticmethod
    def openen_instantie(
        subregister_naam: str,
        id: str,
        ) -> None:
        
        register = Register()
        
        Register._REGISTREER = False
        
        subregister_dict = register._SUBREGISTERS[subregister_naam]
        
        bestandspad = subregister_dict["bestandsmap"] / f"{subregister_dict["bestandsnaam"]}_{id}.{subregister_dict["extensie"]}"
        
        if subregister_dict["vercijfer_methode"] == "standaard":
            geregistreerd_object = openen_json(
                bestandspad = bestandspad,
                ontcijfer_standaard_objecten = subregister_dict["ontcijfer_standaard_objecten"],
                ontcijfer_enum = subregister_dict["enums"],
                )
        else:
            geregistreerd_object = openen_json(
                bestandspad = bestandspad,
                ontcijfer_functie_object = subregister_dict["ontcijfer_functie_objecten"],
                ontcijfer_functie_subobjecten = subregister_dict["ontcijfer_functie_subobjecten"],
                ontcijfer_enum = subregister_dict["enums"],
                )
        
        register[subregister_naam][id] = geregistreerd_object
        
        Register._REGISTREER = True
        
        return geregistreerd_object
    
    @staticmethod
    def opslaan(relatief_pad: Path = Path()) -> None:
        
        register = Register()
        
        for subregister_naam, subregister_dict in register._SUBREGISTERS.items():
            
            if subregister_dict["opslaan"] == "register":
                
                if subregister_dict["vercijfer_methode"] == "standaard":
                    opslaan_json(
                        object = register[subregister_naam],
                        bestandspad = relatief_pad / subregister_dict["bestandsmap"],
                        bestandsnaam = subregister_dict["bestandsnaam"],
                        extensie = subregister_dict["extensie"],
                        vercijfer_standaard_objecten = subregister_dict["vercijfer_standaard_objecten"],
                        vercijfer_standaard_overslaan = subregister_dict["vercijfer_standaard_overslaan"],
                        vercijfer_enum = subregister_dict["enums"],
                        )
                else:
                    opslaan_json(
                        object = register[subregister_naam],
                        bestandspad = relatief_pad / subregister_dict["bestandsmap"],
                        bestandsnaam = subregister_dict["bestandsnaam"],
                        extensie = subregister_dict["extensie"],
                        vercijfer_functie_object = subregister_dict["vercijfer_functie_objecten"],
                        vercijfer_functie_subobjecten = subregister_dict["vercijfer_functie_subobjecten"],
                        vercijfer_enum = subregister_dict["enums"],
                        )
            
            elif subregister_dict["opslaan"] == "instantie":
                
                opslaan_json(
                    object = register[subregister_naam].geregistreerde_instanties,
                    bestandspad = relatief_pad / subregister_dict["bestandsmap"],
                    bestandsnaam = subregister_dict["bestandsnaam"],
                    extensie = subregister_dict["extensie"],
                    )
                
                for id, geregistreerd_object in register[subregister_naam].items():
                    
                    if subregister_dict["vercijfer_methode"] == "standaard":
                        opslaan_json(
                            object = geregistreerd_object,
                            bestandspad = relatief_pad / subregister_dict["bestandsmap"],
                            bestandsnaam = f"{subregister_dict["bestandsnaam"]}_{id}",
                            extensie = subregister_dict["extensie"],
                            vercijfer_standaard_objecten = subregister_dict["vercijfer_standaard_objecten"],
                            vercijfer_standaard_overslaan = subregister_dict["vercijfer_standaard_overslaan"],
                            vercijfer_enum = subregister_dict["enums"],
                            )
                    else:
                        opslaan_json(
                            object = geregistreerd_object,
                            bestandspad = relatief_pad / subregister_dict["bestandsmap"],
                            bestandsnaam = f"{subregister_dict["bestandsnaam"]}_{id}",
                            extensie = subregister_dict["extensie"],
                            vercijfer_functie_object = subregister_dict["vercijfer_functie_objecten"],
                            vercijfer_functie_subobjecten = subregister_dict["vercijfer_functie_subobjecten"],
                            vercijfer_enum = subregister_dict["enums"],
                            )
    
    @staticmethod
    def kopie_opslaan() -> None:
        
        register = Register()
        
        for subregister_naam, subregister_dict in register._SUBREGISTERS.items():
            if subregister_dict["opslaan"] == "instantie":
                for geregistreerde_instantie in register[subregister_naam].geregistreerde_instanties:
                    Register.openen_instantie(
                        subregister_naam = subregister_naam,
                        id = geregistreerde_instantie,
                        )
        
        datum_tekst = dt.date.today().strftime("%Y-%m-%d")
        
        if Register._BESTANDSMAP_KOPIE is None:
            relatief_pad = Path("kopie") / datum_tekst
        else:
            relatief_pad = Register._BESTANDSMAP_KOPIE / datum_tekst
        
        Register.opslaan(relatief_pad)
    
    @staticmethod
    def registreer_instantie(
        instantie: object,
        ) -> None:
        
        register = Register()
        
        if Register._REGISTREER:
            
            if instantie._REGISTRATIE_METHODE == "uuid":
                instantie._id = str(uuid4())
            if instantie._REGISTRATIE_METHODE == "datum":
                instantie._id = dt.date.today().strftime("%Y-%m-%d")
            if instantie._REGISTRATIE_METHODE == "datumtijd":
                instantie._id = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
            
            subregister_naam = instantie._SUBREGISTER_NAAM
            
            if subregister_naam not in register:
                register[subregister_naam] = Subregister(instantie.__class__)
            
            register[subregister_naam][instantie._id] = instantie
            register[subregister_naam].geregistreerde_instanties.append(instantie._id)
    
    @staticmethod
    def instellen(
        bestandsmap: Path,
        bestandsmap_kopie: Path | None = None
        ) -> None:
        
        Register._BESTANDSMAP = bestandsmap
        Register._BESTANDSMAP_KOPIE = bestandsmap_kopie
        Register._INGESTELD = True
    
    @staticmethod
    def registreer_type(
        geregistreerd_type: GeregistreerdObject,
        subregister_naam: str,
        registratie_methode: Literal["uuid", "datum", "datumtijd", "property"] = "uuid",
        opslaan: Literal["register", "instantie", "niet"] = "register",
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
        vercijfer_standaard_overslaan: List[str] | None = ["_id"],
        enums: Dict[str, Enum] | None = None,
        ) -> None:
        
        if not Register._INGESTELD:
            logger.error("Register moest eerst ingesteld worden met Register.instellen()")
        
        geregistreerd_type._SUBREGISTER_NAAM = subregister_naam
        geregistreerd_type._REGISTRATIE_METHODE = registratie_methode
        
        geregistreerd_type_naam = geregistreerd_type.__name__
        
        if subregister_naam not in Register._SUBREGISTERS:
            
            subregister_dict = {
                "type": geregistreerd_type,
                "opslaan": opslaan,
                }
            
            if opslaan in ("register", "instantie"):
                
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