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
    iniciativa: bool = False
    golpe_duplo: bool = False

    def __post_init__(self):
        self.poder = self.poder_base
        self.resistencia = self.resistencia_base

    def __str__(self) -> str:
        texto = f"--- {self.nome} - ({self.custo})---\n--- {self.tipo.value}\n{self.descricao}"
        if self.tipo == TipoCarta.CRIATURA:
            texto += f"\n{self.poder}/{self.resistencia}"
        texto += "\n"
        return texto

    def tomar_dano(self, dano: int) -> None:
        self.resistencia -= dano

    def dano_de_iniciativa(self) -> int:
        if self.iniciativa or self.golpe_duplo:
            return self.poder
        return 0

    def dano_basico(self) -> int:
        if self.iniciativa:
            return 0
        return self.poder
    
    def ataque(self, dano_infligido: int) -> None:
        self.poder -= dano_infligido
        if self.poder < 0:
            self.poder = 0
    
    def resetar_poder(self) -> None:
        self.poder = self.poder_base

    def morreu(self) -> bool:
        return self.resistencia <= 0
