from __future__ import annotations
from typing import Any, List, Literal

from .cel import Cel


class Kolom:
    
    # DUNDER METHODS
    
    def __init__(
        self,
        kolom_naam: str,
        cellen: List[Any] | None = None,
        kolom_breedte: int = 0,
        uitlijning: Literal["links", "midden", "rechts"] = "links",
        ) -> Kolom:
        
        self.kolom_naam = kolom_naam
        self.kolom_breedte = kolom_breedte
        self.uitlijning = uitlijning
        
        self.cellen = cellen
    
    def __repr__(self) -> str:
        return self.cellen.__repr__()
    
    def __getitem__(self, sleutel: int) -> Kolom:
        return self.cellen[sleutel]
    
    def __setitem__(self, sleutel: int, waarde: Cel) -> None:
        self._cellen[sleutel] = waarde
    
    def __iter__(self):
        for cel in self.cellen:
            yield cel
    
    # PROPERTIES
    
    @property
    def uitlijnings_teken(self) -> str:
        if self.uitlijning == "links":
            return "<"
        elif self.uitlijning == "midden":
            return "^"
        elif self.uitlijning == "rechts":
            return ">"
    
    @property
    def cellen(self) -> List[Cel]:
        return self._cellen
    
    @cellen.setter
    def cellen(self, waardes: List[Any] | None) -> None:
        if waardes is None:
            self._cellen = []
        else:
            cellen = []
            for waarde in waardes:
                if isinstance(waarde, Cel):
                    cellen.append(waarde)
                else:
                    cel = Cel(
                        tekst = str(waarde),
                        uitlijning = self.uitlijning,
                        )
                    cellen.append(cel)
            self._cellen = cellen
    
    @property
    def kolom_breedte(self) -> int:
        if self._kolom_breedte == 0:
            return max(len(self.kolom_naam), max(len(cel) for cel in self.cellen))
        return self._kolom_breedte
    
    @kolom_breedte.setter
    def kolom_breedte(self, kolom_breedte: int) -> None:
        self._kolom_breedte = kolom_breedte
    
    @property
    def _naar_tekst(self) -> List[str]:
        
        tekst_links = []
        tekst = []
        tekst_rechts = []
        
        for cel in self.cellen:
            
            if cel.uitlijning == "links":
                tekst_links.append("")
                tekst.append(f"{cel.tekst[:self.kolom_breedte]:{f"{cel.uitlijnings_teken}"}{self.kolom_breedte}}")
                tekst_rechts.append(f"{cel.tekst[self.kolom_breedte:]}")
            
            elif cel.uitlijning == "midden":
                tekst_gecentreerd = f"{cel.tekst:{f"{cel.uitlijnings_teken}"}{self.kolom_breedte}}"
                
                if len(tekst_gecentreerd) > self.kolom_breedte:
                    index_links = (len(tekst_gecentreerd) - self.kolom_breedte) // 2 + 1
                    index_rechts = index_links + self.kolom_breedte
                    
                    tekst_links.append(tekst_gecentreerd[:index_links])
                    tekst.append(tekst_gecentreerd[index_links:index_rechts])
                    tekst_rechts.append(tekst_gecentreerd[index_rechts:])
                
                else:
                    tekst_links.append("")
                    tekst.append(tekst_gecentreerd)
                    tekst_rechts.append("")
            
            elif cel.uitlijning == "rechts":
                tekst_links.append(f"{cel.tekst[:-self.kolom_breedte]}")
                tekst.append(f"{cel.tekst[-self.kolom_breedte:]:{f"{cel.uitlijnings_teken}"}{self.kolom_breedte}}")
                tekst_rechts.append("")
        
        return tekst_links, tekst, tekst_rechts
    
    @property
    def tekst(self) -> List[str]:
        return self._naar_tekst[1]
    
    @property
    def tekst_overloop_links(self) -> List[str]:
        return self._naar_tekst[0]
    
    @property
    def tekst_overloop_rechts(self) -> List[str]:
        return self._naar_tekst[2]