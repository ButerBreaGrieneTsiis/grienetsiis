from __future__ import annotations
from dataclasses import dataclass
from typing import Literal


@dataclass
class Cel:
    
    tekst: str
    uitlijning: Literal["links", "midden", "rechts"] = "links"
    overloop: bool = False
    
    def __repr__(self) -> str:
        return self.tekst
    
    def __str__(self) -> str:
        return self.tekst
    
    def __len__(self) -> int:
        return len(self.tekst)
    
    @property
    def uitlijnings_teken(self) -> str:
        if self.uitlijning == "links":
            return "<"
        elif self.uitlijning == "midden":
            return "^"
        elif self.uitlijning == "rechts":
            return ">"