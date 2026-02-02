from ._commando import Commando


class _Terug(Commando):
    def __bool__(self) -> bool: return False