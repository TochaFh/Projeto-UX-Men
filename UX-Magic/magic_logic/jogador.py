from dataclasses import dataclass
from enum import Enum

class IDJogador(Enum):
    GOLGARI: str = 'Golgari'
    RED: str = 'Mono Red'

@dataclass
class Jogador:
    ID: IDJogador
    vida: int
    terrenos_virados: int
    terrenos_desvirados: int
    mana_extra: int
    criaturas: list

    def iniciar_turno(self):
        self.terrenos_desvirados += self.terrenos_virados
        self.terrenos_virados = 0
        self.mana_extra = 0