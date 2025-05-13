import json
from typing import Dict, FrozenSet, List, Tuple


def openen_json(
    map             :   str,
    bestandsnaam    :   str,
    extensie        :   str                                 =   None,
    class_mappers   :   List[Tuple[object, FrozenSet, str]] =   None,
    encoding        :   str                                 =   "utf-8",
    ) -> object:
    
    bestandsnaam    =   bestandsnaam if extensie is None else f"{bestandsnaam}.{extensie}"
    class_mappers   =   List() if class_mappers is None else class_mappers
    
    def decoder(
        object,
        class_mappers:  List[Tuple[object, FrozenSet, str]],
        ) -> object:
        
        for class_mapper in class_mappers:
            if class_mapper[1].issuperset(object.keys()):
                return getattr(class_mapper[0], class_mapper[2])(**object)
        else:
            return object
    
    with open(f"{map}\\{bestandsnaam}", "r", encoding = encoding) as bestand:
        return json.load(bestand, object_hook = lambda object: decoder(object, class_mappers))
    
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