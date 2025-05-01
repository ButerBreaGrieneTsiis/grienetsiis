import json
from typing import Tuple, FrozenSet,  Dict


def open_json(
    map             :   str,
    bestandsnaam    :   str,
    extensie        :   str                             =   None,
    class_mapper    :   Tuple[object, FrozenSet, str]   =   None,
    encoding        :   str                             =   "utf-8",
    ) -> object:
    
    def decoder(
        object,
        class_mapper:   Tuple[object, FrozenSet, str]   =   None,
        ) -> object:
        
        if class_mapper is not None:
            
            if class_mapper[1].issuperset(object.keys()):
                return getattr(class_mapper[0], class_mapper[2])(**object)
            else:
                return object
        
        else:
            return object
    
    bestandsnaam    =   bestandsnaam if extensie is None else f"{bestandsnaam}.{extensie}"
    
    with open(f"{map}\\{bestandsnaam}", "r", encoding = encoding) as bestand:
        if class_mapper is None:
            return json.load(bestand)
        else:
            return json.load(bestand, object_hook = lambda object: decoder(object, class_mapper))
    
def opslaan_json(
    object          :   object,
    map             :   str,
    bestandsnaam    :   str,
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
    
    bestandsnaam    =   bestandsnaam if extensie is None else f"{bestandsnaam}.{extensie}"
    
    with open(f"{map}\\{bestandsnaam}", "w", encoding = encoding) as bestand:
        bestand.write(json.dumps(object, indent = 4, ensure_ascii = False, sort_keys = False, cls = Encoder))