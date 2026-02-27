from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Literal

from .cel import Cel
from .kolom import Kolom


@dataclass
class Tabel:
    
    kolommen: Dict[str, Kolom] | None = None
    kolommen_letters: Literal["onveranderd", "kleine_letters", "hoofdletters", "gekapitaliseerd"] = "onveranderd"
    tussen_breedte: int = 1
    prefix: str = ""
    suffix: str = ""
    scheidingsteken_kolom: str = ""
    
    # DUNDER METHODS
    
    def __post_init__(self) -> None:
        if self.kolommen is None:
            self.kolommen = {}
    
    def __getitem__(self, sleutel: str) -> Kolom:
        return self.kolommen[sleutel]
    
    # PROPERTIES
    
    @property
    def kolom_lijst(self) -> List[Kolom]:
        return list(self.kolommen.values())
    
    @property
    def kolom_namen(self) -> List[str]:
        if self.kolommen_letters == "onveranderd":
            return [kolom_naam for kolom_naam in self.kolommen]
        if self.kolommen_letters == "kleine_letters":
            return [kolom_naam.lower() for kolom_naam in self.kolommen]
        if self.kolommen_letters == "hoofdletters":
            return [kolom_naam.upper() for kolom_naam in self.kolommen]
        if self.kolommen_letters == "gekapitaliseerd":
            return [kolom_naam.capitalize() for kolom_naam in self.kolommen]
    
    @property
    def aantal_rijen(self) -> int:
        return len(self.kolom_lijst[0].cellen)
    
    @property
    def naar_tekst(self) -> str:
        tabel_tekst = """"""
        
        if self.scheidingsteken_kolom:
            tekst_tussen = f"{" "*self.tussen_breedte}{self.scheidingsteken_kolom}{" "*self.tussen_breedte}"
        else:
            tekst_tussen = f"{" "*self.tussen_breedte}"
        
        tekst_koppen = self.prefix + tekst_tussen.join(f"{kolom_naam:{f"{kolom.uitlijnings_teken}"}{kolom.kolom_breedte}}" for kolom_naam, kolom in zip(self.kolom_namen, self.kolom_lijst)) + self.suffix
        tabel_tekst += tekst_koppen
        
        for index_rij in range(self.aantal_rijen):
            tekst_rij = "\n" + self.prefix + tekst_tussen.join(kolom.tekst[index_rij] for kolom in self.kolom_lijst) + self.suffix
            tabel_tekst += tekst_rij
        
        return tabel_tekst
    
    # INSTANCE METHODS
    
    def toevoegen_kolom(self, kolom: Kolom) -> None:
        if kolom.kolom_naam in self.kolommen:
            raise KeyError(f"kolom_naam \"{kolom.kolom_naam}\" bestaat al")
        
        if len(self.kolommen) > 0:
            if self.aantal_rijen != len(kolom.cellen):
                raise ValueError(f"kolom moet {self.aantal_rijen} rijen hebben, niet {len(kolom.cellen)} rijen")
        
        self.kolommen[kolom.kolom_naam] = kolom
    
    def toevoegen_rij(self, **rij) -> None:
        
        for kolom_naam, celwaarde in rij.items():
            if kolom_naam not in self.kolommen:
                self.kolommen[kolom_naam] = Kolom(
                    kolom_naam = kolom_naam,
                    )
                
            if isinstance(celwaarde, Cel):
                cel = celwaarde
            else:
                cel = Cel(
                    tekst = str(celwaarde),
                    uitlijning = self.kolommen[kolom_naam].uitlijning,
                    )
            
            self.kolommen[kolom_naam].cellen.append(cel)
    
    def toevoegen_leeg(self) -> None:
        for kolom_naam in self.kolom_namen:
            self.kolommen[kolom_naam].cellen.append(Cel(""))
    
    def weergeven(self) -> None:
        print(self.naar_tekst)