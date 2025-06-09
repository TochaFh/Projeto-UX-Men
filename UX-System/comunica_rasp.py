import serial

# Substitua 'COM3' pela porta correta (ex: 'COM4', '/dev/ttyUSB0', etc.)
SERIAL_PORT = 'COM14'
BAUD_RATE = 9600  # Use a mesma taxa configurada no Raspberry Pi

def main():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Lendo dados da porta serial {SERIAL_PORT}...")
            while True:
                linha = ser.readline().decode('utf-8').strip()
                if linha:
                    print(f"Recebido do Raspberry Pi: \n\t{linha}")
    except serial.SerialException as e:
        print(f"Erro ao abrir a porta serial: {e}")

if __name__ == "__main__":
    main()

