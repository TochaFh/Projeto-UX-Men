from machine import Pin
from utime import sleep

SIGNAL_PIN = Pin(2, Pin.OUT)

def main():
    pisca_3()
    SIGNAL_PIN.on()
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