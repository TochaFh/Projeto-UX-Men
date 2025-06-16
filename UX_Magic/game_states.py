from enum import Enum

class GameState(Enum):
    INVALID = (-1, -1)

    START = (0, 0)

    RDC_1_0 = (1, 0)
    RDC_1_1 = (1, 1)
    RDC_1_2 = (1, 2)
    RDC_1_3 = (1, 3)

    RDC_2_0 = (2, 0)
    RDC_2_1 = (2, 1)
    RDC_2_2 = (2, 2)
    RDC_2_3 = (2, 3)

    NEW_TURN = (3, 0)

    MAIN_FIRST = (4, 1)
    MAIN_SECOND = (4, 2)

    CONJURANDO_MAGICA = (5, 0)

    ATIVANDO_HABILIDADE = (6, 0)

    DECLARANDO_ATACANTES = (7, 0)
    CONFIRMANDO_ATACANTE = (7, 1)
    ADICIONANDO_ATACANTE = (7, 2)

    DECLARANDO_BLOQUEADORES = (8, 0)
