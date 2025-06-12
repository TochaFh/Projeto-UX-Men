class CartaGenerica:
    def __init__(self, id_rfid: str, tipo_carta, id_jogador: str):
        self.id_rfid = id_rfid
        self.tipo_carta = tipo_carta
        self.id_jogador = id_jogador

    def __str__(self):
        return (f"Carta ID: {self.id_rfid}\n"
                f"Tipo: {self.tipo_carta}\n"
                f"Pertence ao jogador: {self.id_jogador}")