from dataclasses import dataclass
from enum import Enum

class IDJogador(Enum):
    GOLGARI: str = 'Golgari'
    RED: str = 'Mono Red'

@dataclass
class Jogador:
    ID: IDJogador
    vida: int
    terrenos: int
    mana_extra: int