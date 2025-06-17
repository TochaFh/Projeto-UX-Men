import tkinter as tk
from PIL import Image, ImageTk

def setup(janela):
    global bg_img, txt_leitura

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
    title_label = tk.Label(janela, textvariable=title_text, font=("Comic Sans MS", 29), bg="black", fg="white")
    title_label.grid(row=0, column=0, padx=20, pady=10)
    title_text.set("Título Foda")

    msg1_text = tk.StringVar()
    msg1_label = tk.Label(janela, textvariable=msg1_text, font=("Times New Roman", 23), bg="black", fg="white")
    msg1_label.grid(row=1, column=0, padx=20, pady=10)
    msg1_text.set("")

    msg2_text = tk.StringVar()
    msg2_label = tk.Label(janela, textvariable=msg2_text, font=("Times New Roman", 23), bg="black", fg="white")
    msg2_label.grid(row=2, column=0, padx=20, pady=10)
    msg2_text.set("")

    msg3_text = tk.StringVar()
    msg3_label = tk.Label(janela, textvariable=msg3_text, font=("Times New Roman", 23), bg="black", fg="white")
    msg3_label.grid(row=3, column=0, padx=20, pady=10)
    msg3_text.set("")

    warning_text = tk.StringVar()
    warning_label = tk.Label(janela, textvariable=warning_text, font=("Times New Roman", 23), bg="black", fg="yellow")
    warning_label.grid(row=2, column=2, padx=20, pady=10)
    warning_text.set("")

    txt_leitura = tk.StringVar()
    txt_leitura_label = tk.Label(janela, textvariable=txt_leitura, font=("Times New Roman", 18), bg="black", fg="white")
    txt_leitura_label.place(relx=0.85, rely=0.1, anchor="n")
    txt_leitura.set("")

    lbls = [tk.Label(janela, image=p, bg="black") for p in PHOTOS_IMG_CARTAS]
    holder = TextHolder(title_text, msg1_text, msg2_text, msg3_text, warning_text, lbls, janela)


    return background, holder

class TextHolder:
    def __init__(self, _title_label, _msg1_label, _msg2_label, _msg3_label, _warning_label, lbls, _janela):
        self.title = _title_label
        self.msg1 = _msg1_label
        self.msg2 = _msg2_label
        self.msg3 = _msg3_label
        self.warning = _warning_label
        self.LABELS_IMG_CARTAS = lbls
        self.janela = _janela
        self.task_hide = None

    def mostrar_carta(self, txt, img_code=None):
        global txt_leitura
        self.esconder_carta()
        txt_leitura.set(txt)
        if img_code != None:
            self.LABELS_IMG_CARTAS[img_code].place(relx=0.85, rely=0.2, anchor="n")
        
        if self.task_hide:
            self.janela.after_cancel(self.task_hide)
        self.task_hide = self.janela.after(5000, self.esconder_carta)
        self.janela.update_idletasks()

    def esconder_carta(self):
        global txt_leitura
        txt_leitura.set("")
        for lbl in self.LABELS_IMG_CARTAS:
            lbl.place_forget()
        self.janela.update_idletasks()
    
    def refresh(self):
        self.janela.update_idletasks()

URL_IMGS_CARTAS = [ # 0 1 2 3 4 5
    "UX_Magic/magic_assets/blb-138-heartfire-hero.jpg",
    "UX_Magic/magic_assets/dsk-119-unstoppable-slasher.jpg",
    "UX_Magic/magic_assets/fdn-227-llanowar-elves.jpg",
    "UX_Magic/magic_assets/lci-92-bloodletter-of-aclazotz.jpg",
    "UX_Magic/magic_assets/woe-142-monstrous-rage.jpg",
    "UX_Magic/magic_assets/woe-221-callous-sell-sword.jpg"
]

PHOTOS_IMG_CARTAS = [ImageTk.PhotoImage(Image.open(url).resize((672 // 2, 936 // 2))) for url in URL_IMGS_CARTAS]