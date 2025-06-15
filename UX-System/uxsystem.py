from comunica_rasp import SerialReader

_ID = {}
id_count = 0


class UXSystem:
    def __init__(self):
        self.serial_thread = None
        self.ON_RFID = []
        self.ON_LEITURA = []
        self.ON_B_VERMELHO = []
        self.ON_B_AZUL = []

    # ID detectado no modo PADRÃO
    def _on_rd(self, rfid):
        global id_count
        if not _ID.get(rfid):
            id_count += 1
            _ID[rfid] = id_count
            print(f"Nova carta detectada: {_ID[rfid]}")

        for callback in self.ON_RFID:
            try:
                callback(_ID[rfid])
            except Exception as e:
                print(f"** Erro ao chamar callback em _on_rd: {e}")

    # ID detectado no modo de LEITURA
    def _on_rr(self, rfid):
        if _ID.get(rfid):
            print(f"Leitura de carta: {_ID[rfid]}")
        
        for callback in self.ON_LEITURA:
            try:
                callback(_ID.get(rfid, None))
            except Exception as e:
                print(f"** Erro ao chamar callback em _on_rr: {e}")

    # Botão azul pressionado
    def _on_bb(self):
        for callback in self.ON_B_AZUL:
            try:
                callback()
            except Exception as e:
                print(f"** Erro ao chamar callback em _on_bb: {e}")

    # Botão vermelho pressionado
    def _on_br(self):
        for callback in self.ON_B_VERMELHO:
            try:
                callback()
            except Exception as e:
                print(f"** Erro ao chamar callback em _on_br: {e}")

    def start(self):
        self.serial_thread = SerialReader(self._on_rd, self._on_rr, self._on_br, self._on_bb)
        self.serial_thread.start()

    def close(self):
        self.serial_thread.stop()

def teste():
    from time import sleep
    uxs = UXSystem()
    uxs.start()
    try:
        print("# UX-System rodando...")
        while True:
            sleep(0.05)
    except KeyboardInterrupt:
        uxs.close()
        print("# UX-System encerrado.")
    except Exception as e:
        uxs.close()
        print(f"** Erro inesperado no teste (raiz): {e}")

if __name__ == "__main__":
    teste()