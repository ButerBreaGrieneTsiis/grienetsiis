from __future__ import annotations

from grienetsiis.opdrachtprompt.commando import Commando


class Stop(Commando):
    def __call__(self) -> Stop: return Stop()
    def __bool__(self) -> bool: return False