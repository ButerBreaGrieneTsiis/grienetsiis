from grienetsiis.types import Singleton


class _Terug(metaclass = Singleton):
    def __repr__(self) -> str: return "TERUG"
    def __str__(self) -> str: return "TERUG"
    def __bool__(self) -> bool: return False