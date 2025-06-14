import tkinter as tk
from comunica_rasp import SerialReader


def on_serial_message(msg):
    print(f"Recebido do Raspberry Pi: {msg}")

root = tk.Tk()
root.title("Interface Serial Blank")

serial_thread = SerialReader(on_serial_message)
serial_thread.start()

def on_close():
    serial_thread.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()

