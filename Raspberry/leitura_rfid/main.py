from machine import Pin
from utime import sleep, sleep_ms
from mfrc522 import MFRC522

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)


SIGNAL_PIN = Pin(15, Pin.OUT)

def main():
    pisca_3()
    SIGNAL_PIN.on()

    print("Rolando leitura")

    while True:
        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid),"little",False)
                print("CARD ID: "+str(card))
        sleep_ms(500)
    while True:
        dado = "Hello, World!"
        print(dado)
        sleep(1)

def pisca():
    SIGNAL_PIN.on()
    sleep(0.05)
    SIGNAL_PIN.off()

def pisca_3():
    for _ in range(3):
        pisca()
        sleep(0.15)

if __name__ == "__main__":
    main()