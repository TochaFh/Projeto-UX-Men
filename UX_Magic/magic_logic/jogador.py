from dataclasses import dataclass
from enum import Enum

class IDJogador(Enum):
    GOLGARI: str = 'Golgari'
    RED: str = 'Mono Red'

@dataclass
class Jogador:
    ID: IDJogador
    vida: int = 20
    terrenos_virados: int = 0
    terrenos_desvirados: int = 0
    mana_extra: int = 0
    criaturas: list = []
    cards_hand: list = []
    cards_bf: list = []
    cards_grave: list = []

    def iniciar_turno(self):
        self.terrenos_desvirados += self.terrenos_virados + 1
        self.terrenos_virados = 0
        self.mana_extra = 0