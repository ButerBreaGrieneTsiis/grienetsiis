import json
from typing import Tuple, FrozenSet, Callable

def decoder(dictionary, class_mapper: Tuple[Callable, FrozenSet] = None):
    
    if class_mapper is not None:
        if class_mapper[1].issuperset(dictionary.keys()):
            return class_mapper[0](**dictionary)
        else:
            return dictionary
    else:
        return dictionary

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "naar_json"):
            return obj.naar_json()  
        try:
            obj.__dict__
        except:
            return json.JSONEncoder.default(self, obj)
        else:
            return obj.__dict__
            
def open_json(map : str, bestandsnaam : str, extensie : str = None, class_mapper: Tuple[Callable, FrozenSet] = None, encoding : str= "utf-8") -> dict:
    
    bestandsnaam    =   bestandsnaam if extensie is None else f"{bestandsnaam}.{extensie}"
    with open(f"{map}\\{bestandsnaam}", "r", encoding = encoding) as bestand:
        if class_mapper is None:
            return json.load(bestand)
        else:
            return json.load(bestand, object_hook = lambda x: decoder(x, class_mapper))
    
def opslaan_json(dictionary : dict, map : str, bestandsnaam : str, extensie : str = None, encoder = Encoder, encoding : str = "utf-8"):
    
    bestandsnaam    =   bestandsnaam if extensie is None else f"{bestandsnaam}.{extensie}"
    
    with open(f"{map}\\{bestandsnaam}", "w", encoding = encoding) as bestand:
        bestand.write(json.dumps(dictionary, indent = 4, ensure_ascii = False, sort_keys = False, cls = encoder))