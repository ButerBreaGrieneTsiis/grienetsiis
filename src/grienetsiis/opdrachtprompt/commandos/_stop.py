from grienetsiis.types import Singleton


class _Stop(metaclass = Singleton):
    def __repr__(self) -> str: return "STOP"
    def __str__(self) -> str: return "STOP"
    def __bool__(self) -> bool: return False