# acabamos movendo essa parte do código para a lógica do magic
# seriam utilities legais pro UX-System ter no futuro para ser reaproveitado em outros jogos
# mas por enquanto ta bão assim

class CartaGenerica:
    cartas_em_uso = {}

    def __init__(self, id_rfid: str, tipo_carta, id_jogador: str):
        self.id_rfid = id_rfid
        self.tipo_carta = tipo_carta
        self.id_jogador = id_jogador
            

    def __str__(self):
        return (f"Carta ID: {self.id_rfid}\n"
                f"Tipo: {self.tipo_carta}\n"
                f"Pertence ao jogador: {self.id_jogador}")