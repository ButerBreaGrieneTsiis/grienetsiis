from __future__ import annotations

from grienetsiis.types import Singleton


class Commando(metaclass = Singleton):
    def __call__(self, *args, **kwargs) -> Commando: return Commando()
    def __repr__(self) -> str: return self.__class__.__name__.replace("_", "").upper()
    def __str__(self) -> str: return self.__class__.__name__.replace("_", "").upper()