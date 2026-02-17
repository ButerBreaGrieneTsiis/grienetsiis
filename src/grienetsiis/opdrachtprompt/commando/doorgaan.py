from __future__ import annotations

from grienetsiis.opdrachtprompt.commando import Commando


class Doorgaan(Commando):
    def __call__(self) -> Doorgaan: return Doorgaan()
    def __bool__(self) -> bool: return False