import tkinter as tk
from comunica_rasp import SerialReader


def on_serial_message(msg):
    print(f"Recebido do Raspberry Pi: {msg}")
    msg_var.set(f"Recebido: {msg}")

root = tk.Tk()
root.title("Interface Serial Blank")

# Exemplo de label para mostrar mensagens recebidas (opcional)
msg_var = tk.StringVar()
label = tk.Label(root, textvariable=msg_var)
label.pack(padx=20, pady=20)

serial_thread = SerialReader(on_serial_message, on_serial_message, on_serial_message, on_serial_message)
serial_thread.start()

def on_close():
    serial_thread.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()

