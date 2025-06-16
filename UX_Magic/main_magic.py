from UX_Magic.magic_logic.carta_magic import CartaMagic, TipoCarta
from UX_Magic.magic_logic.jogador import Jogador, IDJogador
from UX_Magic.cartas_demo import *
from UX_System.uxsystem import UXSystem
from UX_Magic.magic_ui import TextHolder

def setup(_uxs: UXSystem, holder: TextHolder):
    global ID_to_card, player1, player2, players, current_player, p1cards, p2cards, uxs, main_count, atacantes, ID_to_player, ui, player_count
    player_count = 0
    main_count = 1
    uxs = _uxs
    ID_to_card = dict()
    ID_to_player = dict()
    p1cards = p2cards = 0
    player1 = Jogador(IDJogador.GOLGARI)
    player2 = Jogador(IDJogador.RED)
    players = [player1, player2]
    current_player = -1
    atacantes = []

    ui = holder

    ui.title.set("Magic: The Gathering")
    ui.msg1.set("Identificação de jogadores")
    ui.warning.set("Jogador 1, passe seu identificador")

    uxs.ON_RFID.append(identificar_player)


def identificar_player(rfid):
    global players, player_count, ID_to_player
    if rfid in ID_to_player.keys():
        return
    ID_to_player[rfid] = players[player_count]
    player_count += 1
    ui.warning.set(f"- Jogador {player_count+1}, passe seu identificador")
    if(player_count >= 2):
        uxs.clear_all_callbacks()
        ui.title.set("Magic: The Gathering")
        ui.msg1.set("Identificação de cartas\nCada jogador deve associar 3 cartas")
        ui.msg2.set("- Jogador 1:  0 / 3 cartas associadas")
        ui.msg3.set("- Jogador 2:  0 / 3 cartas associadas")
        ui.warning.set("Jogador 1, passe uma carta em branco no leitor")
        uxs.ON_RFID.append(associar_cartas)

def associar_cartas(rfid):
    global ID_to_card, player1, player2, players, current_player, p1cards, p2cards, uxs

    if rfid in ID_to_card.keys() or rfid in ID_to_player.keys():
        # TODO: avisar ao jogador que aquela carta já foi associada
        return

    if p1cards < 3:
        ID_to_card[rfid] = (CardList[p1cards], player1)
        player1.cards_hand.append(CardList[p1cards])
        p1cards += 1
        ui.msg2.set(f"- Jogador 1:  {p1cards} / 3 cartas associadas")
    elif p2cards < 3:
        ID_to_card[rfid] = (CardList[3 + p2cards], player2)
        player1.cards_hand.append(CardList[3 + p2cards])
        p2cards += 1
        ui.msg3.set(f"- Jogador 2:  {p2cards} / 3 cartas associadas")
    else:
        uxs.clear_all_callbacks()
        # Esperando início do jogo
        ui.warning.set("novo estado iniciado")
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

def conjurar_magica(carta: CartaMagic):
    global players, uxs
    jogador_atual = players[current_player]
    if jogador_atual.mana_extra + jogador_atual.terrenos_desvirados >= carta.custo:      
        jogador_atual.consumir_mana(carta.custo)
    else:
        # TODO: avisar ao jogador que ele não tem mana o suficiente
        uxs.clear_all_callbacks()
        uxs.ON_B_AZUL.append(main_phase)
        return
    
    if carta.tipo == TipoCarta.CRIATURA:
        jogador_atual.cards_bf.append(carta)

    elif carta == MonstrousRage:
        # TODO: informar que está aguardando uma criatura alvo

        def await_HH(rfid):
            if ID_to_card[rfid] == HeartfireHero:
                MR_trigger_HH(ID_to_card[rfid])

        uxs.clear_all_callbacks()
        uxs.ON_RFID.append(await_HH)
    elif carta == BurnTogether:
        # TODO: informar que está aguardando uma criatura alvo

        def await_HH(rfid):
            if ID_to_card[rfid] == HeartfireHero:
                # TODO: informar que está aguardando jogador alvo

                uxs.clear_all_callbacks()
                uxs.ON_RFID.append(BT_getplayer)

        uxs.clear_all_callbacks()
        uxs.ON_RFID.append(await_HH)

def MR_trigger_HH():
    global uxs
    # TODO: informar ao jogador sobre o trigger sendo colocado no stack
    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(MR_addcounters_HH)

def MR_addcounters_HH():
    HeartfireHero.poder_base += 1
    HeartfireHero.resistencia_base += 1

    # TODO: informar ao jogador que Heartfire Hero recebeu um contador +1/+1

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(MR_createtoken_HH)

def MR_createtoken_HH():
    HeartfireHero.poder_base += 2

    # TODO: informar ao jogador que o monster role token foi criado e atrelado a heartfire hero. avisar que o stack acabou

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(main_phase)

def BT_getplayer(rfid):
    if rfid not in ID_to_player.keys():
        # TODO: ID invalido
        return
    
    alvo: Jogador = ID_to_player[rfid]
    alvo.vida -= 

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append()

# TODO: remover pass
def ativar_habilidade(carta):
    pass