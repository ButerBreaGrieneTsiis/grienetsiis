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
    ontcijfer_functie: Callable | None = None,
    ontcijfer_objecten_standaard: Dict[str, Callable] | None = None,
    ontcijfer_objecten_functie: List[Ontcijferaar] | None = None,
    ontcijfer_enum: Dict[str, Enum] | None = None,
    ontcijfer_datum: bool = True,
    encoding: str = "utf-8",
    ) -> object:
    
    ontcijfer_objecten_standaard = {} if ontcijfer_objecten_standaard is None else ontcijfer_objecten_standaard
    ontcijfer_objecten_functie = [] if ontcijfer_objecten_functie is None else ontcijfer_objecten_functie
    ontcijfer_enum = {} if ontcijfer_enum is None else ontcijfer_enum
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    def ontcijferaar(
        object,
        ontcijfer_functie: Callable,
        ontcijfer_objecten_standaard: Dict[str, Callable],
        ontcijfer_objecten_functie: List[Ontcijferaar],
        ontcijfer_enum: Dict[str, Enum],
        ontcijfer_datum: bool,
        ) -> object:
        
        if object:
            
            if "__enum__" in object:
                enum_veld, enum_waarde = object["__enum__"].split(".")
                if enum_veld in ontcijfer_enum:
                    return getattr(ontcijfer_enum[enum_veld], enum_waarde)
            
            if ontcijfer_datum:
                if "__datum__" in object:
                    return dt.datetime.strptime(object["__datum__"], "%Y-%m-%d").date()
                
                if "__datumtijd__" in object:
                    return dt.datetime.strptime(object["__datumtijd__"], "%Y-%m-%d %H:%M:%S")
            
            if ontcijfer_functie:
                try:
                    if "__class__" in object:
                        del object["__class__"]
                    return ontcijfer_functie(**object)
                except:
                    pass
            
            if "__class__" in object:
                for object_class_naam, ontcijfer_functie in ontcijfer_objecten_standaard.items():
                    if object["__class__"] == object_class_naam:
                        del object["__class__"]
                        return ontcijfer_functie(**object)
            
            if "__class__" in object:
                del object["__class__"]
            
            for ontcijfer_object_functie in ontcijfer_objecten_functie:
                if ontcijfer_object_functie.velden.issuperset(object.keys()):
                    return ontcijfer_object_functie.ontcijfer_functie(**object)
        
        return object
    
    with open(bestandspad, "r", encoding = encoding) as bestand:
        return json.load(
            bestand,
            object_hook = lambda object: ontcijferaar(
                object,
                ontcijfer_functie,
                ontcijfer_objecten_standaard,
                ontcijfer_objecten_functie,
                ontcijfer_enum,
                ontcijfer_datum,
                )
            )