from machine import Pin
from utime import sleep, sleep_ms, ticks_ms
from mfrc522 import MFRC522

# modulo rfid
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

# pinos do led
SIGNAL_PIN = Pin(15, Pin.OUT)

# pinos botões
RED_BUTTON = Pin(10, Pin.IN, Pin.PULL_UP)
BLUE_BUTTON = Pin(12, Pin.IN, Pin.PULL_UP)
YELLOW_BUTTON = Pin(11, Pin.IN, Pin.PULL_UP)

# handler dos botões
click_time = 0
def button_handler(pin):
    global click_time
    if ticks_ms() - click_time > 500:
        click_time = ticks_ms()
        pisca()
        if pin == RED_BUTTON:
            print("Br")
        elif pin == BLUE_BUTTON:
            print("Bb")
        #elif pin == YELLOW_BUTTON:
            # para o UX system não é necessário o evento do botão amarelo
            #print("By")

def main():

    # sinal de vida
    pisca_3()

    # triggers dos botões
    RED_BUTTON.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
    BLUE_BUTTON.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
    YELLOW_BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

    SIGNAL_PIN.on()

    # rotina de leitura do RFID
    print("Rolando leitura")
    while True:
        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid), "little", False)
                if YELLOW_BUTTON.value() == 0:
                    print("Rr-"+str(card))
                else:
                    print("Rd-"+str(card))
                sleep(2)
        sleep_ms(500)

def pisca():
    SIGNAL_PIN.toggle()
    sleep(0.05)
    SIGNAL_PIN.toggle()

def pisca_3():
    SIGNAL_PIN.off()
    for _ in range(3):
        pisca()
        sleep(0.15)

if __name__ == "__main__":
    main()