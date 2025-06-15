import tkinter as tk
from PIL import Image, ImageTk

def setup(janela, lista_jogos, lista_callbacks):
    global bg_img  # Variável global para a imagem de fundo
    # Caminho da imagem de fundo
    BG_IMAGE = "UX_UI/images/fundo.png"

    # Carrega e redimensiona a imagem para o tamanho da tela
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    img = Image.open(BG_IMAGE).resize((screen_width, screen_height))
    bg_img = ImageTk.PhotoImage(img)

    # Cria um label para a imagem de fundo
    background_label = tk.Label(janela, image=bg_img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Adicionar um rótulo
    rotulo = tk.Label(background_label, text="Olá, Tkinter!")
    rotulo.grid(row=1, column=0, padx=20, pady=20)  # Posicionado na primeira linha e primeira coluna

    for jogo, callback in zip(lista_jogos, lista_callbacks):
        # Cria um botão para cada jogo na lista
        botao_jogo = tk.Button(background_label, text=jogo, command=callback)
        botao_jogo.grid(row=lista_jogos.index(jogo) + 2, column=0, padx=20, pady=10)

    return background_label

def exibir_mensagem():
  print("O botão foi clicado!")