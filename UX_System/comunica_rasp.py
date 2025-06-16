import serial
import threading
from time import sleep

# Substitua 'COM3' pela porta correta (ex: 'COM4', '/dev/ttyUSB0', etc.)
SERIAL_PORT = 'COM14'
BAUD_RATE = 9600  # Use a mesma taxa configurada no Raspberry Pi

def main():
    print("# Comunica rasp rodando em teste (main.py)")
    serial_thread = SerialReader(on_rd, on_rr, on_br, on_bb)
    serial_thread.start()
    print("# Thread de leitura serial iniciada...")
    while True:
        try:
            sleep(0.05)
        except KeyboardInterrupt:
            serial_thread.stop()
            break


def on_bb():
    print("- Botão azul pressionado")

def on_br():
    print("- Botão vermelho pressionado")

def on_rd(msg):
    print(f"- ID detectado no modo padrão: {msg}")

def on_rr(msg):
    print(f"- ID detectado no modo de leitura: {msg}")


class SerialReader(threading.Thread):
    def __init__(self, Rd, Rr, Br, Bb):
        super().__init__(daemon=True)
        self.rd = Rd
        self.rr = Rr
        self.br = Br
        self.bb = Bb
        self.running = True

    def run(self):
        while True:
            try:
                with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
                    print(f"## Conectado à porta serial {SERIAL_PORT}!")
                    while self.running:
                        linha = ser.readline().decode('utf-8').strip()
                        if not linha:
                            continue
                        if linha[0] == 'R':
                            if linha[1] == 'd':
                                self.rd(linha[3:])
                            elif linha[1] == 'r':
                                self.rr(linha[3:])
                        elif linha[0] == 'B':
                            if linha[1] == 'r':
                                self.br()
                            elif linha[1] == 'b':
                                self.bb()

            except serial.SerialException as e:
                print(f"** Erro ao abrir a porta serial: {e}")
                input("** Pressione Enter para tentar novamente...")

    def stop(self):
        self.running = False

if __name__ == "__main__":
    main()