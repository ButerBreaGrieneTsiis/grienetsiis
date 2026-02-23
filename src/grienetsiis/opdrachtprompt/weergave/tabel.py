from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List, Literal


class Kolom:
    
    # DUNDER METHODS
    
    def __init__(
        self,
        kolom_naam: str,
        waardes: List[Any],
        kolom_breedte: int = 0,
        uitlijning: Literal["links", "midden", "rechts"] = "links",
        ) -> None:
        
        self.kolom_naam = kolom_naam
        self.waardes = waardes
        self.kolom_breedte = kolom_breedte
        self.uitlijning = uitlijning
    
    # PROPERTIES
    
    @property
    def uitlijnings_teken(self) -> str:
        if self.uitlijning == "links":
            return "<"
        elif self.uitlijning == "midden":
            return "^"
        return ">"
    
    @property
    def kolom_breedte(self) -> int:
        if self._kolom_breedte == 0:
            return max(len(self.kolom_naam), max(len(str(waarde)) for waarde in self.waardes))
        return self._kolom_breedte
    
    @kolom_breedte.setter
    def kolom_breedte(self, kolom_breedte: int) -> None:
        self._kolom_breedte = kolom_breedte

@dataclass
class Tabel:
    
    kolommen: Dict[str, Kolom] | None = None
    tussen_breedte: int = 1
    prefix: str = ""
    suffix: str = ""
    scheidingsteken_kolom: str = ""
    tekst_overloop: bool = False
    
    # DUNDER METHODS
    
    def __post_init__(self) -> None:
        if self.kolommen is None:
            self.kolommen = {}
    
    # CLASS METHODS
    
    # PROPERTIES
    
    @property
    def kolom_lijst(self) -> List[Kolom]:
        return list(self.kolommen.values())
    
    @property
    def kolom_namen(self) -> List[str]:
        return [kolom_naam for kolom_naam in self.kolommen]
    
    @property
    def lengte(self) -> int:
        return len(self.kolom_lijst[0].waardes)
    
    @property
    def rijen(self) -> List[List[str]]:
        
        rijen = [["" for _ in range(len(self.kolommen))] for _ in range(self.lengte)]
        
        for index_kolom, kolom in enumerate(self.kolom_lijst):
            for index_waarde, waarde in enumerate(kolom.waardes):
                rijen[index_waarde][index_kolom] = str(waarde)
        return rijen
    
    # INSTANCE METHODS
    
    def toevoegen_kolom(self, kolom: Kolom) -> None:
        if len(self.kolommen) > 0:
            if self.lengte != len(kolom.waardes):
                raise ValueError("kolommen zijn ongelijk")
        
        self.kolommen[kolom.kolom_naam] = kolom
    
    def toevoegen_rij(self, **rij) -> None:
        
        for kolom_naam, waarde in rij.items():
            if kolom_naam not in self.kolommen:
                self.kolommen[kolom_naam] = Kolom(
                    kolom_naam = kolom_naam,
                    waardes = [],
                    )
            self.kolommen[kolom_naam].waardes.append(waarde)
    
    def weergeven(self) -> None:
        
        if self.scheidingsteken_kolom:
            tekst_tussen = f"{" "*self.tussen_breedte}{self.scheidingsteken_kolom}{" "*self.tussen_breedte}"
        else:
            tekst_tussen = f"{" "*self.tussen_breedte}"
        
        tekst_koppen = self.prefix + tekst_tussen.join(f"{kolom.kolom_naam:{f"{kolom.uitlijnings_teken}"}{kolom.kolom_breedte}}" for kolom in self.kolom_lijst) + self.suffix
        print(tekst_koppen)
        
        for rij in self.rijen:
            if self.tekst_overloop:
                tekst_rij = self.prefix + tekst_tussen.join(f"{waarde:{f"{kolom.uitlijnings_teken}"}{kolom.kolom_breedte}}" for kolom, waarde in zip(self.kolom_lijst, rij)) + self.suffix
            else:
                tekst_rij = self.prefix + tekst_tussen.join(f"{waarde[:kolom.kolom_breedte]:{f"{kolom.uitlijnings_teken}"}{kolom.kolom_breedte}}" for kolom, waarde in zip(self.kolom_lijst, rij)) + self.suffix
            print(tekst_rij)

if __name__ == "__main__":
    
    import datetime as dt
    
    tabel = Tabel(
        prefix = "||",
        scheidingsteken_kolom = "|",
        suffix = "||",
        )
    
    kolom_datum = Kolom(
        kolom_naam = "datum",
        waardes = [dt.date.today() - dt.timedelta(days = dag) for dag in range(5)],
        )
    kolom_waardes = Kolom(
        kolom_naam = "dagen",
        waardes = [(dt.date.today() - dt.timedelta(days = dag)).strftime("%A") for dag in range(5)],
        )
    
    tabel.toevoegen_kolom(kolom_datum)
    tabel.toevoegen_kolom(kolom_waardes)
    tabel.weergeven()