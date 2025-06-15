from magic_logic.carta_magic import CartaMagic, TipoCarta
from magic_logic.jogador import Jogador, IDJogador
from cartas_demo import CardList
from _placeholders_ import ler_rfid, esperar_inicio_partida

ID_to_card = dict()

player1 = Jogador(IDJogador.GOLGARI)
player2 = Jogador(IDJogador.RED)
players = [player1, player2]
current_player = 0

def setup():
    # CARREGAR INFOS ANTES DO JOGO
    for card in CardList[0:3]:
        ID_to_card[ler_rfid()] = (card, player1)
    for card in CardList[3:]:
        ID_to_card[ler_rfid()] = (card, player2)
    