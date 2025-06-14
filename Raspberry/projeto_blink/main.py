from machine import Pin
from utime import sleep

pin = Pin(2, Pin.OUT)

def pisca():
    pin.on()
    sleep(0.05)
    pin.off()

for _ in range(3):
    pisca()
    sleep(0.15)

print("LED is ready to flash.")

sleep(2)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
