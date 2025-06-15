from comunica_rasp import SerialReader

_ID = {}
id_count = 0

ON_RFID = []
ON_LEITURA = []
ON_B_VERMELHO = []
ON_B_AZUL = []

# ID detectado no modo PADRÃO
def _on_rd(rfid):
    global id_count
    if not _ID.get(rfid):
        id_count += 1
        _ID[rfid] = id_count
        print(f"Nova carta detectada: {_ID[rfid]}")

    for callback in ON_RFID:
        try:
            callback(_ID[rfid])
        except Exception as e:
            print(f"** Erro ao chamar callback em _on_rd: {e}")

# ID detectado no modo de LEITURA
def _on_rr(rfid):
    if _ID.get(rfid):
        print(f"Leitura de carta: {_ID[rfid]}")
    
    for callback in ON_LEITURA:
        try:
            callback(_ID.get(rfid, None))
        except Exception as e:
            print(f"** Erro ao chamar callback em _on_rr: {e}")

# Botão azul pressionado
def _on_bb():
    for callback in ON_B_AZUL:
        try:
            callback()
        except Exception as e:
            print(f"** Erro ao chamar callback em _on_bb: {e}")

# Botão vermelho pressionado
def _on_br():
    for callback in ON_B_VERMELHO:
        try:
            callback()
        except Exception as e:
            print(f"** Erro ao chamar callback em _on_br: {e}")

def start():
    global serial_thread
    serial_thread = SerialReader(_on_rd, _on_rr, _on_br, _on_bb)
    serial_thread.start()

def close():
    global serial_thread
    serial_thread.stop()

def teste():
    from time import sleep
    start()
    try:
        print("# UX-System rodando...")
        while True:
            sleep(0.05)
    except KeyboardInterrupt:
        close()
        print("# UX-System encerrado.")
    except Exception as e:
        close()
        print(f"** Erro inesperado: {e}")
    pass

if __name__ == "__main__":
    teste()