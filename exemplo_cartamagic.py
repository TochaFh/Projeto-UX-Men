from carta_magic import CartaMagic, TipoCarta

if __name__ == "__main__":
    carta = CartaMagic(
        nome="Relâmpago",
        custo="R",
        tipo=TipoCarta.MAGICA_INSTANTANEA,
        descricao="Relâmpago causa 3 pontos de dano a qualquer alvo."
    )
    print(carta)
    criatura = CartaMagic(
        nome="Urso Cinzento",
        custo="1G",
        tipo=TipoCarta.CRIATURA,
        descricao="Uma criatura simples.",
        poder=2,
        resistencia=2
    )
    print(criatura)