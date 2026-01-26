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
    vercijfer_enum: Dict[str, Enum] | None = None,
    vercijfer_datum: bool = True,
    encoding: str = "utf-8",
    ) -> None:
    
    vercijfer_standaard_objecten = [] if vercijfer_standaard_objecten is None else vercijfer_standaard_objecten
    vercijfer_functie_subobjecten = [] if vercijfer_functie_subobjecten is None else vercijfer_functie_subobjecten
    vercijfer_enum = {} if vercijfer_enum is None else vercijfer_enum
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    class vercijferaar(json.JSONEncoder):
        
        def default(self, object):
            
            if type(object) in vercijfer_enum.values():
                return {"__enum__": str(object)}
            
            if vercijfer_datum:
                if isinstance(object, dt.date):
                    return {"__datum__": object.strftime("%Y-%m-%d")}
                
                if isinstance(object, dt.datetime):
                    return {"__datumtijd__": object.strftime("%Y-%m-%d %H:%M:%S")}
            
            if vercijfer_functie_object:
                try:
                    return getattr(object, vercijfer_functie_object.__name__)()
                except:
                    pass
            
            for object_class_naam in vercijfer_standaard_objecten:
                if object.__class__.__name__ == object_class_naam:
                    object_dict = {
                        "__class__": object.__class__.__name__,
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