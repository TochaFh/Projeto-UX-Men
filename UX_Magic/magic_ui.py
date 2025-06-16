import tkinter as tk
from PIL import Image, ImageTk

def setup(janela):
    global bg_img

    # Caminho da imagem de fundo
    BACKGROUND_IMAGE = "UX_UI/images/magic_BG.png"

    # Carrega e redimensiona a imagem para o tamanho da tela
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    img = Image.open(BACKGROUND_IMAGE).resize((screen_width, screen_height))
    bg_img = ImageTk.PhotoImage(img)

    # Cria um label para a imagem de fundo
    background = tk.Label(janela, image=bg_img)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    title_text = tk.StringVar()
    title_label = tk.Label(background, textvariable=title_text, font=("Comic Sans MS", 29), bg="black", fg="white")
    title_label.grid(row=0, column=0, padx=20, pady=10)
    title_text.set("Título Foda")

    msg1_text = tk.StringVar()
    msg1_label = tk.Label(background, textvariable=msg1_text, font=("Times New Roman", 23), bg="black", fg="white")
    msg1_label.grid(row=1, column=0, padx=20, pady=10)
    msg1_text.set("")

    msg2_text = tk.StringVar()
    msg2_label = tk.Label(background, textvariable=msg2_text, font=("Times New Roman", 23), bg="black", fg="white")
    msg2_label.grid(row=2, column=0, padx=20, pady=10)
    msg2_text.set("")

    msg3_text = tk.StringVar()
    msg3_label = tk.Label(background, textvariable=msg3_text, font=("Times New Roman", 23), bg="black", fg="white")
    msg3_label.grid(row=3, column=0, padx=20, pady=10)
    msg3_text.set("")

    warning_text = tk.StringVar()
    warning_label = tk.Label(background, textvariable=warning_text, font=("Arial", 23), bg="black", fg="yellow")
    warning_label.grid(row=2, column=2, padx=20, pady=10)
    warning_text.set("")

    holder = TextHolder(title_text, msg1_text, msg2_text, msg3_text, warning_text)

    return background, holder

class TextHolder:
    def __init__(self, _title_label, _msg1_label, _msg2_label, _msg3_label, _warning_label):
        self.title = _title_label
        self.msg1 = _msg1_label
        self.msg2 = _msg2_label
        self.msg3 = _msg3_label
        self.warning = _warning_label