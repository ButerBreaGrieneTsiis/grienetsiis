import datetime as dt
from enum import Enum
import json
from pathlib import Path
from typing import Callable, Dict, FrozenSet, List, NamedTuple


class Decoder(NamedTuple):
    decoder_functie: Callable
    velden: FrozenSet[str]

class Encoder(NamedTuple):
    class_naam: str
    encoder_functie: str

def openen_json(
    bestandspad: Path,
    bestandsnaam: str | None = None,
    extensie: str | None = None,
    decoder_object: Callable | None = None,
    decoder_subobjecten: List[Decoder] | None = None,
    enum_dict: Dict[str, Enum] | None = None,
    encoding: str = "utf-8",
    ) -> object:
    
    decoder_subobjecten = [] if decoder_subobjecten is None else decoder_subobjecten
    enum_dict = {} if enum_dict is None else enum_dict
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    def decoder(
        object,
        decoder_object: Callable,
        decoder_subobjecten: List[Decoder],
        enum_dict: Dict[str, Enum],
        ) -> object:
        
        if object:
            
            if "__enum__" in object:
                enum_veld, enum_waarde = object["__enum__"].split(".")
                return getattr(enum_dict[enum_veld], enum_waarde)
            
            if "__datum__" in object:
                return dt.datetime.strptime(object["__datum__"], "%Y-%m-%d").date()
            
            if "__datumtijd__" in object:
                return dt.datetime.strptime(object["__datumtijd__"], "%Y-%m-%d %H:%M:%S")
            
            if decoder_object:
                try:
                    return decoder_object(**object)
                except:
                    pass
            for decoder_subobject in decoder_subobjecten:
                if decoder_subobject.velden.issuperset(object.keys()):
                    return decoder_subobject.decoder_functie(**object)
        
        return object
    
    with open(bestandspad, "r", encoding = encoding) as bestand:
        return json.load(
            bestand,
            object_hook = lambda object: decoder(
                object,
                decoder_object,
                decoder_subobjecten,
                enum_dict,
                )
            )
    
def opslaan_json(
    object: object,
    bestandspad: Path,
    bestandsnaam: str | None = None,
    extensie: str | None = None,
    encoder_object: Callable | None = None,
    encoder_subobjecten: List[Encoder] | None = None,
    enum_dict: Dict[str, Enum] | None = None,
    encoding: str = "utf-8",
    ) -> None:
    
    encoder_subobjecten = [] if encoder_subobjecten is None else encoder_subobjecten
    enum_dict = {} if enum_dict is None else enum_dict
    
    class JSONEncoder(json.JSONEncoder):
        
        def default(self, object):
            
            if type(object) in enum_dict.values():
                return {"__enum__": str(object)}
            
            if isinstance(object, dt.date):
                return {"__datum__": object.strftime("%Y-%m-%d")}
            
            if isinstance(object, dt.datetime):
                return {"__datumtijd__": object.strftime("%Y-%m-%d %H:%M:%S")}
            
            if encoder_object:
                try:
                    return getattr(object, encoder_object.__name__)()
                except:
                    pass
            
            for encoder_subobject in encoder_subobjecten:
                if object.__class__.__name__ == encoder_subobject.class_naam:
                    return getattr(object, encoder_subobject.encoder_functie)()
            
            try:
                return object.__dict__
            except:
                return json.JSONEncoder.default(self, object)
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    with open(bestandspad, "w", encoding = encoding) as bestand:
        bestand.write(json.dumps(
            object,
            indent = 4,
            ensure_ascii = False,
            sort_keys = False,
            cls = JSONEncoder,
            ))