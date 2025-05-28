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
    poder_base: int = 0
    resistencia_base: int = 0
    poder: int = 0
    resistencia: int = 0

    def __post_init__(self):
        self.poder = self.poder_base
        self.resistencia = self.resistencia_base

    def __str__(self) -> str:
        texto = f"--- {self.nome} - ({self.custo})---\n--- {self.tipo.value}\n{self.descricao}"
        if self.tipo == TipoCarta.CRIATURA:
            texto += f"\n{self.poder}/{self.resistencia}"
        texto += "\n"
        return texto

