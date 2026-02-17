from __future__ import annotations

from grienetsiis.opdrachtprompt.commando import Commando


class Terug(Commando):
    def __call__(self) -> Terug: return Terug()
    def __bool__(self) -> bool: return False