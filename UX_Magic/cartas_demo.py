from UX_Magic.magic_logic.carta_magic import CartaMagic, TipoCarta

LlanowarElves = CartaMagic(
    nome='Llanowar Elves',
    custo=1,
    tipo=TipoCarta.CRIATURA,
    descricao='Vire essa criatura: adicione 1 de mana.',
    poder_base=1,
    resistencia_base=1
    )

HeartfireHero = CartaMagic(
    nome='Heartfire Hero',
    custo=1,
    tipo=TipoCarta.CRIATURA,
    descricao='Quando essa criatura é alvo de um feitiço que você controla, ela recebe um marcador +1/+1. Isso ocorre apenas uma vez por turno.\n' \
    'Quando essa criatura morre, ela dá dano igual ao seu poder a todos os oponentes.',
    poder_base=1,
    resistencia_base=1
    )

UnstoppableSlasher = CartaMagic(
    nome='Unstoppable Slasher',
    custo=3,
    tipo=TipoCarta.CRIATURA,
    descricao='Quando essa criatura causa dano de combate a um jogador, esse jogador perde metade da sua vida, arredondado pra cima.\n' \
    'Quando essa criatura morre, se ela não tiver contadores, retorne-a ao campo de batalha com dois marcadores de atordoamento.',
    poder_base=2,
    resistencia_base=3
    )

MonstrousRage = CartaMagic(
    nome='Monstrous Rage',
    custo=1,
    tipo=TipoCarta.MAGICA_INSTANTANEA,
    descricao='Criatura alvo Recebe +2/+0 até o fim do turno. Crie uma ficha de função de monstro anexada à criatura.'
    )

BurnTogether = CartaMagic(
    nome='Burn Together',
    custo=1,
    tipo=TipoCarta.FEITICO,
    descricao='Criatura alvo que você controla causa dano igual ao seu poder a qualquer outro alvo. Depois sacrifique a criatura.',
    )

BloodletterOfAclazotz = CartaMagic(
    nome='Bloodletter of Aclazotz',
    custo=4,
    tipo=TipoCarta.CRIATURA,
    descricao='Voador\n' \
    'Se um oponente perderia vida durante o seu turno, em vez disso ele perde o dobro de vida',
    poder_base=2,
    resistencia_base=4
    )

CardList = [LlanowarElves, UnstoppableSlasher, BloodletterOfAclazotz, HeartfireHero, MonstrousRage, BurnTogether]