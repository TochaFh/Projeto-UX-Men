from carta_magic import CartaMagic, TipoCarta
from batalha import batalha_criaturas

def main():

    # teste criando carta aleatória
    carta = CartaMagic(
        nome="Relâmpago",
        custo="R",
        tipo=TipoCarta.MAGICA_INSTANTANEA,
        descricao="Relâmpago causa 3 pontos de dano a qualquer alvo."
    )
    print(carta)

    # criando uma criatura 2/2 com iniciativa
    criatura1 = CartaMagic(
        nome="Urso Cinzento",
        custo="1G",
        tipo=TipoCarta.CRIATURA,
        descricao="Uma criatura simples.",
        poder_base=2,
        resistencia_base=2,
        iniciativa=True
    )
    print(criatura1)

    # criando uma criatura 1/1
    criatura2 = CartaMagic(
        nome="Goblin Selvagem",
        custo="R",
        tipo=TipoCarta.CRIATURA,
        descricao="Um goblin agressivo.",
        poder_base=1,
        resistencia_base=1
    )
    print(criatura2)

    # testando batalha entre as criaturas
    resumo_batalha = batalha_criaturas(criatura1, [criatura2])
    print()
    # TODO: fazer algo a respeito das criaturas que morreram
    # aqui neste ponto as criaturas que tomaram dano estão com a resitência alterada
    # (como se ainda não tivesse acabado o turno)
    # TODO: função de fim de turno que reseta as vidas das criaturas


if __name__ == "__main__":
    main()