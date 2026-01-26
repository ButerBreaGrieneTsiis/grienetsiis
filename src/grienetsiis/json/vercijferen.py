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
    vercijfer_functie: Callable | None = None,
    vercijfer_objecten_standaard: List[str] | None = None,
    vercijfer_objecten_functie: List[Vercijferaar] | None = None,
    vercijfer_enum: Dict[str, Enum] | None = None,
    vercijfer_datum: bool = True,
    encoding: str = "utf-8",
    ) -> None:
    
    vercijfer_objecten_standaard = [] if vercijfer_objecten_standaard is None else vercijfer_objecten_standaard
    vercijfer_objecten_functie = [] if vercijfer_objecten_functie is None else vercijfer_objecten_functie
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
            
            if vercijfer_functie:
                try:
                    return getattr(object, vercijfer_functie.__name__)()
                except:
                    pass
            
            for object_class_naam in vercijfer_objecten_standaard:
                if object.__class__.__name__ == object_class_naam:
                    return {
                        "__class__": object.__class__.__name__,
                        **object.__dict__,
                        }
            
            for vercijfer_object_functie in vercijfer_objecten_functie:
                if object.__class__.__name__ == vercijfer_object_functie.class_naam:
                    return getattr(object, vercijfer_object_functie.vercijfer_functie_naam)()
            
            try:
                return object.__dict__
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