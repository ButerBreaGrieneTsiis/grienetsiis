from enum import Enum
import json
from pathlib import Path
from typing import Callable, Dict, FrozenSet, List, NamedTuple


class Decoder(NamedTuple):
    decoder_functie: Callable
    velden: FrozenSet

def openen_json(
    bestandspad     :   Path,
    bestandsnaam    :   str                 =   None,
    extensie        :   str                 =   None,
    decoder_functie :   Callable            =   None,
    decoder_lijst   :   List[Decoder]       =   None,
    enum_dict       :   Dict[str, Enum]     =   None,
    encoding        :   str                 =   "utf-8",
    ) -> object:
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    decoder_lijst = list() if decoder_lijst is None else decoder_lijst
    enum_dict = dict() if enum_dict is None else enum_dict
    
    def decoder(
        object,
        decoder_functie: Callable,
        decoder_lijst: List[Decoder],
        enum_dict: Dict[str, Enum],
        ) -> object:
        
        if "__enum__" in object:
            enum_veld, enum_waarde = object["__enum__"].split(".")
            return getattr(enum_dict[enum_veld], enum_waarde)
        
        if decoder_functie:
            try:
                return decoder_functie(**object)
            except:
                pass
        for decoder in decoder_lijst:
            if decoder.velden.issuperset(object.keys()):
                return decoder.decoder_functie(**object)
        
        return object
    
    with open(bestandspad, "r", encoding = encoding) as bestand:
        return json.load(
            bestand,
            object_hook = lambda object: decoder(
                object,
                decoder_functie,
                decoder_lijst,
                enum_dict,
                )
            )
    
def opslaan_json(
    object          :   object,
    bestandspad     :   Path,
    bestandsnaam    :   str             =   None,
    extensie        :   str             =   None,
    encoder_functie :   Callable        =   None,
    encoder_dict    :   Dict[str, str]  =   None,
    enum_dict       :   Dict[str, Enum] =   None,
    encoding        :   str             =   "utf-8",
    ) -> None:
    
    enum_dict = dict() if enum_dict is None else enum_dict
    
    class Encoder(json.JSONEncoder):
        
        def default(self, object):
            
            if type(object) in enum_dict.values():
                return {"__enum__": str(object)}
            
            if encoder_functie:
                try:
                    return getattr(object, encoder_functie.__name__)()
                except:
                    pass
            
            if isinstance(encoder_dict, dict):
                if object.__class__.__name__ in encoder_dict.keys():
                    return getattr(object, encoder_dict[object.__class__.__name__])()
            
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
            cls = Encoder,
            ))