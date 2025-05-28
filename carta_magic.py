from dataclasses import dataclass
from enum import Enum
from typing import Any

class TipoCarta(Enum):
    CRIATURA: str = "Criatura"
    MAGICA_INSTANTANEA: str = "Mágica Instantânea"
    FEITICO: str = "Feitiço"
    ENCANTAMENTO: str = "Encantamento"
    ARTEFATO: str = "Artefato"
    PLANESWALKER: str = "Planeswalker"
    TERRENO: str = "Terreno"

@dataclass
class CartaMagic:
    nome: str
    custo: str
    tipo: TipoCarta
    descricao: str
    poder: int = 0
    resistencia: int = 0

    def __str__(self) -> str:
        base = f"{self.nome} ({self.custo}) - {self.tipo.value}\n{self.descricao}"
        if self.poder or self.resistencia:
            base += f"\n{self.poder}/{self.resistencia}"
        return base

