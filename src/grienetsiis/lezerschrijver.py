import json
from pathlib import Path
from typing import Callable, Dict, FrozenSet, List, NamedTuple


class ObjectWijzer(NamedTuple):
    van_json: Callable
    velden: FrozenSet

def openen_json(
    bestandspad     :   Path,
    bestandsnaam    :   str                 =   None,
    extensie        :   str                 =   None,
    object_wijzers  :   List[ObjectWijzer]  =   None,
    encoding        :   str                 =   "utf-8",
    ) -> object:
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    object_wijzers   =   list() if object_wijzers is None else object_wijzers
    
    def decoder(
        object,
        object_wijzers: List[ObjectWijzer],
        ) -> object:
        
        for object_wijzer in object_wijzers:
            if object_wijzer.velden.issuperset(object.keys()):
                return object_wijzer.van_json(**object)
        else:
            return object
    
    with open(bestandspad, "r", encoding = encoding) as bestand:
        return json.load(bestand, object_hook = lambda object: decoder(object, object_wijzers))
    
def opslaan_json(
    object          :   object,
    bestandspad     :   Path,
    bestandsnaam    :   str             =   None,
    extensie        :   str             =   None,
    encoder_dict    :   Dict[str, str]  =   None,
    encoding        :   str             =   "utf-8",
    ) -> None:
    
    class Encoder(json.JSONEncoder):
        
        def default(self, object):
            
            if isinstance(encoder_dict, dict):
                if object.__class__.__name__ in encoder_dict.keys():
                    return getattr(object, encoder_dict[object.__class__.__name__])()
            
            try:
                object.__dict__
            except:
                return json.JSONEncoder.default(self, object)
            else:
                return object.__dict__
    
    if extensie is None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}"
    elif extensie is not None and bestandsnaam is not None:
        bestandspad /= f"{bestandsnaam}.{extensie}"
    
    with open(bestandspad, "w", encoding = encoding) as bestand:
        bestand.write(json.dumps(object, indent = 4, ensure_ascii = False, sort_keys = False, cls = Encoder))