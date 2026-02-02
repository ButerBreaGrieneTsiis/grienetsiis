import datetime as dt
from enum import Enum
import json
from pathlib import Path
from typing import Callable, Dict, List, NamedTuple


class Vercijferaar(NamedTuple):
    class_naam: str
    vercijfer_functie_naam: str

def opslaan_json(
    object: object,
    bestandspad: Path,
    bestandsnaam: str | None = None,
    extensie: str | None = None,
    vercijfer_functie_object: Callable | None = None,
    vercijfer_functie_subobjecten: List[Vercijferaar] | None = None,
    vercijfer_standaard_objecten: List[str] | None = None,
    vercijfer_standaard_overslaan: List[str] | None = None,
    vercijfer_standaard_naam: str = "__class__",
    vercijfer_enum: Dict[str, Enum] | None = None,
    vercijfer_enum_naam: str = "__enum__",
    vercijfer_datum: bool = True,
    vercijfer_datum_naam: str = "__datum__",
    vercijfer_datum_formaat: str = "%Y-%m-%d",
    vercijfer_datumtijd_naam: str = "__datumtijd__",
    vercijfer_datumtijd_formaat: str = "%Y-%m-%d %H:%M:%S",
    encoding: str = "utf-8",
    ) -> None:
    
    vercijfer_functie_subobjecten = [] if vercijfer_functie_subobjecten is None else vercijfer_functie_subobjecten
    vercijfer_standaard_objecten = [] if vercijfer_standaard_objecten is None else vercijfer_standaard_objecten
    vercijfer_enum = {} if vercijfer_enum is None else vercijfer_enum
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    class vercijferaar(json.JSONEncoder):
        
        def default(self, object):
            
            if type(object) in vercijfer_enum.values():
                return {vercijfer_enum_naam: str(object)}
            
            if vercijfer_datum:
                if isinstance(object, dt.date):
                    return {vercijfer_datum_naam: object.strftime(vercijfer_datum_formaat)}
                
                if isinstance(object, dt.datetime):
                    return {vercijfer_datumtijd_naam: object.strftime(vercijfer_datumtijd_formaat)}
            
            if vercijfer_functie_object:
                try:
                    return getattr(object, vercijfer_functie_object.__name__)()
                except:
                    pass
            
            for object_class_naam in vercijfer_standaard_objecten:
                if object.__class__.__name__ == object_class_naam:
                    object_dict = {
                        vercijfer_standaard_naam: object.__class__.__name__,
                        **object.__dict__,
                        }
                    for veld in vercijfer_standaard_overslaan:
                        object_dict.pop(veld, None)
                    return object_dict
            
            for vercijfer_functie_subobject in vercijfer_functie_subobjecten:
                if object.__class__.__name__ == vercijfer_functie_subobject.class_naam:
                    return getattr(object, vercijfer_functie_subobject.vercijfer_functie_naam)()
            
            try:
                object_dict = object.__dict__
                for veld in vercijfer_standaard_overslaan:
                    object_dict.pop(veld, None)
                return object_dict
            except:
                return json.JSONEncoder.default(self, object)
    
    for map in reversed(bestandspad.parents):
        if not map.exists():
            map.mkdir()
    
    with open(bestandspad, "w", encoding = encoding) as bestand:
        bestand.write(json.dumps(
            object,
            indent = 4,
            ensure_ascii = False,
            sort_keys = False,
            cls = vercijferaar,
            ))