from magic_logic.carta_magic import CartaMagic, TipoCarta
from magic_logic.jogador import Jogador, IDJogador
from cartas_demo import *
from game_states import GameState
from uxsystem import UXSystem

def setup(_uxs: UXSystem):
    global ID_to_card, player1, player2, players, current_player, current_state, p1cards, p2cards, uxs, main_count, atacantes
    main_count = 1
    uxs = _uxs
    ID_to_card = dict()
    p1cards = p2cards = 0
    player1 = Jogador(IDJogador.GOLGARI)
    player2 = Jogador(IDJogador.RED)
    players = [player1, player2]
    current_player = -1
    current_state = GameState.START
    atacantes: list[CartaMagic] = []

    # TODO: Pedir pros jogadores lerem as cartas

    uxs.ON_RFID.append(associar_cartas)
    

def associar_cartas(rfid):
    global ID_to_card, player1, player2, players, current_player, current_state, p1cards, p2cards, uxs

    if rfid in ID_to_card.keys():
        # TODO: avisar ao jogador que aquela carta já foi associada
        return

    if p1cards < 3:
        ID_to_card[rfid] = (CardList[p1cards], player1)
        player1.cards_hand.append(CardList[p1cards])
    elif p2cards < 3:
        ID_to_card[rfid] = (CardList[3 + p2cards], player2)
        player1.cards_hand.append(CardList[3 + p2cards])
    else:
        uxs.clear_all_callbacks()
        # Esperando início do jogo
        uxs.ON_B_AZUL.append(iniciar_turno)

def iniciar_turno():
    global players, current_player, uxs, main_count, atacantes
    atacantes.clear()
    main_count = 1
    current_player = (current_player + 1) % 2
    players[current_player].iniciar_turno()

    # TODO: informar início do turno do jogador e pedir pra ele desvirar seus permanentes

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(main_phase)
    
def main_phase():
    global main_count, uxs, players, current_player, ID_to_card
    # TODO: informar ao jogador que está na main phase, aguardando uma ação

    uxs.clear_all_callbacks()

    # LIDANDO COM OS BOTÕES
    if(main_count == 1):
        uxs.ON_B_AZUL.append(declare_attacks)
    else:
        uxs.ON_B_AZUL.append(iniciar_turno)
    
    uxs.ON_B_VERMELHO.append(iniciar_turno)
    
    # LIDANDO COM LEITURA DE CARTAS
    def handle_card_read_mp(rfid):
        try:
            carta = ID_to_card[rfid][0]
        except KeyError:
            # TODO: informar que a carta é inválida
            main_phase()

        if carta in players[current_player].cards_hand:
            conjurar_magica(carta)
        elif carta in players[current_player].cards_bf:
            ativar_habilidade(carta)

    uxs.ON_RFID.append(handle_card_read_mp)

def declare_attacks():
    global uxs, atacantes

    # TODO: informar ao jogador que ele está declarando ataques e mostrar quais são os atacantes atuais

    uxs.clear_all_callbacks()

    uxs.ON_B_AZUL.append(declare_blocks)

    def handle_card_read_da(rfid):
        try:
            carta: CartaMagic = ID_to_card[rfid][0]
        except KeyError:
            # TODO: informar que a carta é inválida
            declare_attacks()

        if carta.tipo != TipoCarta.CRIATURA:
            # TODO: informar que a carta não é uma criatura
            declare_attacks()
        else:
            atacantes.append(carta)
            declare_attacks(carta)

    uxs.ON_RFID.append(handle_card_read_da)

def declare_blocks():
    global uxs
    # TODO: pedir pro jogador declarar bloqueadores

    uxs.clear_all_callbacks()

    uxs.ON_B_AZUL.append(resultados_combate)

def resultados_combate():
    global uxs, atacantes, main_count
    dano_causado = 0
    for carta in atacantes:
        dano_causado += carta.poder
    
    # TODO: informar ao jogador o resultado do combate

    main_count = 2

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(main_phase)

def conjurar_magica(carta):
    jogador_atual = players[current_player]
    match carta:
        case LlanowarElves:
            

def ativar_habilidade(carta):
    pass