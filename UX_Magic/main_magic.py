from UX_Magic.magic_logic.carta_magic import CartaMagic, TipoCarta
from UX_Magic.magic_logic.jogador import Jogador, IDJogador
from UX_Magic.cartas_demo import *
from UX_System.uxsystem import UXSystem
from UX_Magic.magic_ui import TextHolder
from time import sleep

def setup(_uxs: UXSystem, holder: TextHolder):
    global ID_to_card, player_golgari, player_red, players, current_player, p1cards, p2cards, uxs, main_count, atacantes, ID_to_player, ui, player_count
    player_count = 0
    main_count = 1
    uxs = _uxs
    ID_to_card = dict()
    ID_to_player = dict()
    p1cards = p2cards = 0
    player_golgari = Jogador(IDJogador.GOLGARI)
    player_red = Jogador(IDJogador.RED)
    players = [player_golgari, player_red]
    current_player = -1
    atacantes = []

    ui = holder

    ui.title.set("Magic: The Gathering")
    ui.msg1.set("Identificação de jogadores")
    ui.warning.set("Jogador 1, passe seu identificador")

    uxs.ON_RFID.append(identificar_player)

    uxs.ON_LEITURA.append(visualizar_carta)

def visualizar_carta(rfid):
    global ID_to_card, player_golgari, player_red, players, current_player, p1cards, p2cards, uxs
    if rfid not in ID_to_card.keys():
        ui.mostrar_carta("O identificador não corresponde\na uma carta associada")
        return
    ui.mostrar_carta(f"Carta do jogador {ID_to_card[rfid][1].ID.value}:", ID_to_card[rfid][0].img_code)

def identificar_player(rfid):
    global players, player_count, ID_to_player
    if rfid in ID_to_player.keys():
        return
    ID_to_player[rfid] = players[player_count]
    player_count += 1
    ui.warning.set(f"- Jogador {player_count+1}, passe seu identificador")
    ui.refresh()
    if(player_count >= 2):
        uxs.clear_all_callbacks()
        ui.title.set("Magic: The Gathering")
        ui.msg1.set("Identificação de cartas\nCada jogador deve associar 3 cartas")
        ui.msg2.set("- Jogador 1:  0 / 3 cartas associadas")
        ui.msg3.set("- Jogador 2:  0 / 3 cartas associadas")
        ui.warning.set("Jogador 1, passe uma carta em branco no leitor")
        ui.refresh()
        uxs.ON_RFID.append(associar_cartas)

def associar_cartas(rfid):
    global ID_to_card, player_golgari, player_red, players, current_player, p1cards, p2cards, uxs

    if rfid in ID_to_card.keys() or rfid in ID_to_player.keys():
        ui.msg1.set("")
        ui.msg2.set("")
        ui.msg3.set("")
        ui.warning("Essa carta já foi cadastrada")
        return

    if p1cards < 3:
        ID_to_card[rfid] = (CardList[p1cards], player_golgari)
        player_golgari.cards_hand.append(CardList[p1cards])
        p1cards += 1
        ui.msg2.set(f"- Jogador 1:  {p1cards} / 3 cartas associadas")
        ui.refresh()
        if p1cards >= 3:
            ui.warning.set("Jogador 2, passe uma carta em branco no leitor")
            ui.refresh()
    else:
        ID_to_card[rfid] = (CardList[3 + p2cards], player_red)
        player_golgari.cards_hand.append(CardList[3 + p2cards])
        p2cards += 1
        ui.msg3.set(f"- Jogador 2:  {p2cards} / 3 cartas associadas")
        ui.refresh()
        if p2cards >= 3:
            uxs.clear_all_callbacks()
            # Esperando início do jogo
            ui.warning.set("Aperte o botão azul para iniciar o jogo")
            uxs.ON_B_AZUL.append(iniciar_turno)
            ui.refresh()

def iniciar_turno():
    global players, current_player, uxs, main_count, atacantes
    atacantes.clear()
    main_count = 1
    current_player = (current_player + 1) % 2
    players[current_player].iniciar_turno()

    ui.title.set(f"Turno do Jogador {current_player + 1}")
    ui.msg1.set("Fase de manutenção")
    ui.msg2.set(f"(Desvirar permanentes)")
    ui.msg3.set("")
    ui.warning.set("Aperte o botão azul para prosseguir")
    ui.refresh()

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(main_phase)
    
def main_phase():
    global main_count, uxs, players, current_player, ID_to_card
    ui.msg1.set(f"Fase principal")
    ui.msg2.set("Passe cartas no leitor para conjurá-las ou ativar habilidades")
    ui.msg3.set("Aperte o botão azul para prosseguir de fase\n e o botão vermelho para encerrar o turno")
    ui.warning.set("")

    uxs.clear_all_callbacks()
    sleep(0.1)
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
            ui.warning.set("")
        except KeyError:
            ui.warning.set("Passe uma carta válida")

        if carta in players[current_player].cards_hand:
            conjurar_magica(carta)
        elif carta in players[current_player].cards_bf:
            ativar_habilidade(carta)

    uxs.ON_RFID.append(handle_card_read_mp)

def declare_attacks():
    global uxs, atacantes

    ui.msg1.set("Fase de combate")
    ui.msg2.set("Declare seus atacantes")
    ui.msg3.set("atacantes: " + ", ".join([carta.nome for carta in atacantes]) if atacantes else "Nenhum atacante declarado")
    

    uxs.clear_all_callbacks()

    uxs.ON_B_AZUL.append(declare_blocks)

    def handle_card_read_da(rfid):
        try:
            carta: CartaMagic = ID_to_card[rfid][0]
        except KeyError:
            ui.msg1.set("")
            ui.msg2.set("")
            ui.msg3.set("")
            ui.warning("Passe uma carta válida para a leitura")
            # TODO: informar que a carta é inválida
            declare_attacks()

        if carta.tipo != TipoCarta.CRIATURA:
            ui.msg1.set("")
            ui.msg2.set("")
            ui.msg3.set("")
            ui.warning("Essa carta não é uma criatura")
            # TODO: informar que a carta não é uma criatura
            declare_attacks()
        else:
            atacantes.append(carta)
            declare_attacks()

    uxs.ON_RFID.append(handle_card_read_da)

def declare_blocks():
    global uxs
    ui.msg1.set("Você está sendo atacado")
    ui.msg2.set("")
    ui.msg3.set("")
    ui.warning.set("Declare bloqueadores!")
    # TODO: pedir pro jogador declarar bloqueadores

    uxs.clear_all_callbacks()

    uxs.ON_B_AZUL.append(resultados_combate)

def resultados_combate():
    global uxs, atacantes, main_count, players
    dano_causado = 0
    for carta in atacantes:
        dano_causado += carta.poder


    # TODO: informar ao jogador o resultado do combate

    if BloodletterOfAclazotz in players[current_player].cards_bf:
        players[(current_player + 1)%2].vida =  0
        uxs.clear_all_callbacks()
        uxs.ON_B_AZUL.append(fim_jogo)
        return
    else:
        players[(current_player + 1)%2].vida -= dano_causado
    

    main_count = 2

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(main_phase)

def conjurar_magica(carta: CartaMagic):
    global players, uxs
    jogador_atual = players[current_player]
    if jogador_atual.mana_extra + jogador_atual.terrenos_desvirados >= carta.custo:      
        jogador_atual.consumir_mana(carta.custo)
        jogador_atual.cards_hand.remove(carta)
    else:
        # TODO: avisar ao jogador que ele não tem mana o suficiente
        ui.msg1.set("")
        ui.msg2.set("")
        ui.msg3.set("")
        ui.warning.set(f"Mana insuficiente para conjurar {carta.nome}")
        # uxs.clear_all_callbacks()
        # uxs.ON_B_AZUL.append(main_phase)
        return
    
    ui.warning.set('')
    ui.msg1.set('')
    ui.msg2.set('')
    ui.msg3.set('')

    if carta.tipo == TipoCarta.CRIATURA:
        jogador_atual.cards_bf.append(carta)
        ui.msg1.set(f"A criatura {carta.nome} foi conjurada!")
        ui.msg2.set("Pressione o botão azul para prosseguir")
        uxs.clear_all_callbacks()
        uxs.ON_B_AZUL.append(main_phase)

    elif carta == MonstrousRage:
        ui.msg1.set('')
        ui.msg2.set('')
        ui.msg3.set('')
        ui.warning.set("Declare uma criatura alvo!")

        # TODO: informar que está aguardando uma criatura alvo

        def await_HH(rfid):
            if ID_to_card[rfid] == HeartfireHero:
                MR_trigger_HH(ID_to_card[rfid])

        uxs.clear_all_callbacks()
        uxs.ON_RFID.append(await_HH)
    elif carta == BurnTogether:
        ui.msg1.set('')
        ui.msg2.set('')
        ui.msg3.set('')
        ui.warning("Declare uma criatura alvo!")
        # TODO: informar que está aguardando uma criatura alvo

        def await_HH(rfid):
            if ID_to_card[rfid] == HeartfireHero:
                ui.msg1.set('')
                ui.msg2.set('')
                ui.msg3.set('')
                ui.warning("Declare um jogador alvo")
                # TODO: informar que está aguardando jogador alvo

                uxs.clear_all_callbacks()
                uxs.ON_RFID.append(BT_getplayer)

        uxs.clear_all_callbacks()
        uxs.ON_RFID.append(await_HH)

def MR_trigger_HH():
    global uxs
    ui.msg1.set('')
    ui.msg2.set('')
    ui.msg3.set('')
    ui.warning.set("carata   ")
    # TODO: informar ao jogador sobre o trigger sendo colocado no stack
    # O trigger "Adicione um contador +1/+1 a Heartfire Hero" foi adicionado ao stack

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

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(BT_cause_damage_sac)

def BT_cause_damage_sac():
    player_golgari.vida -= HeartfireHero.poder

    # TODO: jogador golgari recebe dano, hh é sacrificado (trigger adicionado ao stack)

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append()

def BT_hh_death_trigger():
    player_golgari.vida -= HeartfireHero.poder

    # TODO: resolução do trigger, dano ao jogador golgari

    uxs.clear_all_callbacks()
    uxs.ON_B_AZUL.append(main_phase)

def fim_jogo():
    # TODO: informar que o jogador golgari venceu
    uxs.clear_all_callbacks()
    # TODO: Voltar à tela inicial do UX System

# TODO: remover pass
def ativar_habilidade(carta: CartaMagic):
    if carta != LlanowarElves:
        # TODO: informar ao jogador que a carta não tem habilidades
        ui.warning.set(f"{carta.nome} não tem habilidades")
        return
    
    # TODO: perguntar o jogador se ele quer ativar a habilidade da carta
    uxs.clear_all_callbacks()
    ui.msg1.set(f'Deseja ativar a habilidade de {carta.nome}?')
    ui.msg2.set('')
    ui.msg3.set('')
    
    def habilidade():
        player_golgari.mana_extra += 1

        # TODO: informar ao jogador golgari que ele recebeu uma mana extra

        uxs.clear_all_callbacks()
        uxs.ON_B_AZUL.append(main_phase)
    
    uxs.ON_B_AZUL.append(habilidade)
    uxs.ON_B_VERMELHO.append(main_phase)