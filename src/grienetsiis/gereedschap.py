from typing import Iterator


def jaar_maand_iterator(
    jaar_start: int,
    maand_start: int,
    jaar_eind: int,
    maand_eind: int,
    ) -> Iterator[int, int]:
    
    jaar_maand_start    =   12*jaar_start + maand_start-1
    jaar_maand_eind     =   12*jaar_eind + maand_eind-1
    
    for jaar_maand in range(jaar_maand_start, jaar_maand_eind + 1):
        jaar, maand = divmod(jaar_maand, 12)
        yield jaar, maand+1