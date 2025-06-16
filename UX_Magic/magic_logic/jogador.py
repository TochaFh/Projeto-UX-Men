from dataclasses import dataclass, field
from enum import Enum

class IDJogador(Enum):
    GOLGARI: str = 'Golgari'
    RED: str = 'Mono Red'


class InvalidManaCost(Exception):
    def __init__(self, *args):
        super().__init__(*args)

@dataclass
class Jogador:
    ID: IDJogador
    vida: int = 20
    terrenos_virados: int = 0
    terrenos_desvirados: int = 0
    mana_extra: int = 0
    criaturas: list = field(default_factory=list)
    cards_hand: list = field(default_factory=list)
    cards_bf: list = field(default_factory=list)
    cards_grave: list = field(default_factory=list)

    def iniciar_turno(self):
        self.terrenos_desvirados += self.terrenos_virados + 1
        self.terrenos_virados = 0
        self.mana_extra = 0
    
    @property
    def mana_total(self):
        return self.terrenos_desvirados + self.mana_extra
    
    def __virar_terrenos(self, quantidade):
        self.terrenos_virados += quantidade
        self.terrenos_desvirados -= quantidade
    
    def consumir_mana(self, consumo):
        if consumo > self.mana_total:
            raise InvalidManaCost(f"Consumo = {consumo} > {self.mana_total} = Mana")

        if consumo >= self.mana_extra:
            consumo -= self.mana_extra
            self.mana_extra = 0
        else:
            self.mana_extra -= consumo
            return
        
        self.__virar_terrenos(consumo)
