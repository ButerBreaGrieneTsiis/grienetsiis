from typing import ClassVar, Dict, Type


class Singleton(type):
    
    __OBJECTEN: ClassVar[Dict[Type, object]] = {}
    
    def __call__(cls, *args, **kwargs):
        
        if cls not in Singleton.__OBJECTEN:
            Singleton.__OBJECTEN[cls] = super().__call__(*args, **kwargs)
        
        return Singleton.__OBJECTEN[cls]