from grienetsiis.types import Singleton


class Commando(metaclass = Singleton):
    def __call__(self, *args, **kwargs) -> RuntimeError: raise RuntimeError("Commando kan niet uitgevoerd worden.")
    def __repr__(self) -> str: return self.__class__.__name__.replace("_", "").upper()
    def __str__(self) -> str: return self.__class__.__name__.replace("_", "").upper()