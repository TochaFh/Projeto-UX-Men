import serial
import threading
from time import sleep

# Substitua 'COM3' pela porta correta (ex: 'COM4', '/dev/ttyUSB0', etc.)
SERIAL_PORT = 'COM14'
BAUD_RATE = 9600  # Use a mesma taxa configurada no Raspberry Pi

def main():
    print("# Comunica rasp rodando em teste (main.py)")
    serial_thread = SerialReader(on_serial_message)
    serial_thread.start()
    print("# Thread de leitura serial iniciada...")
    while True:
        try:
            sleep(0.05)
        except KeyboardInterrupt:
            serial_thread.stop()
            break

def on_serial_message(msg):
    print(f"- Recebido do Raspberry Pi: \n\t- {msg}")


class SerialReader(threading.Thread):
    def __init__(self, callback):
        super().__init__(daemon=True)
        self.callback = callback
        self.running = True

    def run(self):
        try:
            with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
                while self.running:
                    linha = ser.readline().decode('utf-8').strip()
                    if linha:
                        self.callback(linha)
        except serial.SerialException as e:
            self.callback(f"Erro ao abrir a porta serial: {e}")

    def stop(self):
        self.running = False

if __name__ == "__main__":
    main()