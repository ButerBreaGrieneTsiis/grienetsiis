from ._commando import Commando


class _Stop(Commando):
    def __bool__(self) -> bool: return False