from magic_logic.carta_magic import CartaMagic, TipoCarta
from magic_logic.jogador import Jogador, IDJogador
from cartas_demo import CardList
from _placeholders_ import ler_rfid, esperar_inicio_partida

ID_to_card = dict()

player1 = Jogador(IDJogador.GOLGARI, 20, 0, 0, 0)
player2 = Jogador(IDJogador.RED, 20, 0, 0, 0)
players = [player1, player2]
current_player = 0

def demo_magic():
    # CARREGAR INFOS ANTES DO JOGO
    for card in CardList[0:3]:
        ID_to_card[ler_rfid()] = (card, player1)
    for card in CardList[3:]:
        ID_to_card[ler_rfid()] = (card, player2)

    # INICIO DA PARTIDA
    esperar_inicio_partida()

    while True:
        players[current_player].iniciar_turno()

        # Esperar evento de jogar carta ou passar vez
    