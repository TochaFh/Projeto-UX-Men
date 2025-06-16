import tkinter as tk
from PIL import Image, ImageTk

def setup(janela):
    frame = tk.Frame(janela)

    # Caminho da imagem de fundo
    BACKGROUND_IMAGE = "UX-UI/images/magic_BG.png"

    # Carrega e redimensiona a imagem para o tamanho da tela
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()
    img = Image.open(BACKGROUND_IMAGE).resize((screen_width, screen_height))
    bg_img = ImageTk.PhotoImage(img)

    # Cria um label para a imagem de fundo
    background_label = tk.Label(frame, image=bg_img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    return background_label

# frame ux
