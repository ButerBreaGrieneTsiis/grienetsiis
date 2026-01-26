import datetime as dt
from enum import Enum
import json
from pathlib import Path
from typing import Callable, Dict, FrozenSet, List, NamedTuple


class Ontcijferaar(NamedTuple):
    velden: FrozenSet[str]
    ontcijfer_functie: Callable

def openen_json(
    bestandspad: Path,
    bestandsnaam: str | None = None,
    extensie: str | None = None,
    ontcijfer_functie_object: Callable | None = None,
    ontcijfer_functie_subobjecten: List[Ontcijferaar] | None = None,
    ontcijfer_standaard_objecten: Dict[str, Callable] | None = None,
    ontcijfer_standaard_naam: str = "__class__",
    ontcijfer_enum: Dict[str, Enum] | None = None,
    ontcijfer_enum_naam: str = "__enum__",
    ontcijfer_datum: bool = True,
    ontcijfer_datum_naam: str = "__datum__",
    ontcijfer_datum_formaat: str = "%Y-%m-%d",
    ontcijfer_datumtijd_naam: str = "__datumtijd__",
    ontcijfer_datumtijd_formaat: str = "%Y-%m-%d %H:%M:%S",
    encoding: str = "utf-8",
    ) -> object:
    
    ontcijfer_functie_subobjecten = [] if ontcijfer_functie_subobjecten is None else ontcijfer_functie_subobjecten
    ontcijfer_standaard_objecten = {} if ontcijfer_standaard_objecten is None else ontcijfer_standaard_objecten
    ontcijfer_enum = {} if ontcijfer_enum is None else ontcijfer_enum
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    def ontcijferaar(
        object,
        ontcijfer_functie_object: Callable | None,
        ontcijfer_functie_subobjecten: List[Ontcijferaar],
        ontcijfer_standaard_objecten: Dict[str, Callable],
        ontcijfer_standaard_naam: str,
        ontcijfer_enum: Dict[str, Enum],
        ontcijfer_enum_naam: str,
        ontcijfer_datum: bool,
        ontcijfer_datum_naam: str,
        ontcijfer_datum_formaat: str,
        ontcijfer_datumtijd_naam: str,
        ontcijfer_datumtijd_formaat: str,
        ) -> object:
        
        if object:
            
            if ontcijfer_enum_naam in object:
                enum_veld, enum_waarde = object[ontcijfer_enum_naam].split(".")
                if enum_veld in ontcijfer_enum:
                    return getattr(ontcijfer_enum[enum_veld], enum_waarde)
            
            if ontcijfer_datum:
                if ontcijfer_datum_naam in object:
                    return dt.datetime.strptime(object[ontcijfer_datum_naam], ontcijfer_datum_formaat).date()
                
                if ontcijfer_datumtijd_naam in object:
                    return dt.datetime.strptime(object[ontcijfer_datumtijd_naam], ontcijfer_datumtijd_formaat)
            
            if ontcijfer_functie_object:
                try:
                    if ontcijfer_standaard_naam in object:
                        del object[ontcijfer_standaard_naam]
                    return ontcijfer_functie_object(**object)
                except:
                    pass
            
            if ontcijfer_standaard_naam in object:
                for object_class_naam, ontcijfer_functie in ontcijfer_standaard_objecten.items():
                    if object[ontcijfer_standaard_naam] == object_class_naam:
                        del object[ontcijfer_standaard_naam]
                        return ontcijfer_functie(**object)
            
            if ontcijfer_standaard_naam in object:
                del object[ontcijfer_standaard_naam]
            
            for ontcijfer_functie_subobject in ontcijfer_functie_subobjecten:
                if ontcijfer_functie_subobject.velden.issuperset(object.keys()):
                    return ontcijfer_functie_subobject.ontcijfer_functie(**object)
        
        return object
    
    with open(bestandspad, "r", encoding = encoding) as bestand:
        return json.load(
            bestand,
            object_hook = lambda object: ontcijferaar(
                object = object,
                ontcijfer_functie_object = ontcijfer_functie_object,
                ontcijfer_functie_subobjecten = ontcijfer_functie_subobjecten,
                ontcijfer_standaard_objecten = ontcijfer_standaard_objecten,
                ontcijfer_standaard_naam = ontcijfer_standaard_naam,
                ontcijfer_enum = ontcijfer_enum,
                ontcijfer_enum_naam = ontcijfer_enum_naam,
                ontcijfer_datum = ontcijfer_datum,
                ontcijfer_datum_naam = ontcijfer_datum_naam,
                ontcijfer_datum_formaat = ontcijfer_datum_formaat,
                ontcijfer_datumtijd_naam = ontcijfer_datumtijd_naam,
                ontcijfer_datumtijd_formaat = ontcijfer_datumtijd_formaat,
                )
            )