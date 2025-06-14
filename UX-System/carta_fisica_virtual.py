class CartaGenerica:
    cartas_em_uso = {}

    def __init__(self, id_rfid: str, tipo_carta, id_jogador: str):
        self.id_rfid = id_rfid
        self.tipo_carta = tipo_carta
        self.id_jogador = id_jogador
        
        if id_jogador in cartas_em_uso;
            

    def __str__(self):
        return (f"Carta ID: {self.id_rfid}\n"
                f"Tipo: {self.tipo_carta}\n"
                f"Pertence ao jogador: {self.id_jogador}")