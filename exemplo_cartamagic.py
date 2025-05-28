from carta_magic import CartaMagic, TipoCarta
from batalha import batalha_criaturas

if __name__ == "__main__":
    carta = CartaMagic(
        nome="Relâmpago",
        custo="R",
        tipo=TipoCarta.MAGICA_INSTANTANEA,
        descricao="Relâmpago causa 3 pontos de dano a qualquer alvo."
    )
    print(carta)
    criatura1 = CartaMagic(
        nome="Urso Cinzento",
        custo="1G",
        tipo=TipoCarta.CRIATURA,
        descricao="Uma criatura simples.",
        poder_base=2,
        resistencia_base=2
    )
    print(criatura1)
    criatura2 = CartaMagic(
        nome="Goblin Selvagem",
        custo="R",
        tipo=TipoCarta.CRIATURA,
        descricao="Um goblin agressivo.",
        poder_base=1,
        resistencia_base=1
    )
    print(criatura2)

    print(batalha_criaturas(criatura1, criatura2))