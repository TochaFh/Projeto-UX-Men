import tkinter as tk
from PIL import Image, ImageTk

def setup(janela, lista_jogos, lista_callbacks):
    global bg_img, logo_img  # Variável global para a imagem de fundo

    # Carrega e redimensiona a imagem para o tamanho da tela
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    img = Image.open("UX_UI/images/fundo.png").resize((screen_width, screen_height))
    bg_img = ImageTk.PhotoImage(img)

    # Cria um label para a imagem de fundo
    background = tk.Label(janela, image=bg_img)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Adicionar um rótulo
    #rotulo = tk.Label(background_label, )
    #rotulo.grid(row=1, column=0, padx=20, pady=20)  # Posicionado na primeira linha e primeira coluna
    
    img = Image.open("UX_UI/images/logo_ux_system.png").resize((150, 150))
    logo_img = ImageTk.PhotoImage(img)

    # Cria um label para a imagem de fundo
    logo_label = tk.Label(background, image=logo_img, bg="black")
    logo_label.grid(row=1, column=0, padx=20, pady=20)


    # canvas = tk.Canvas(frame, bg="black", width=500, height=500)
    # canvas.grid(row=1, column=0, padx=20, pady=20)

    # photoimage = ImageTk.PhotoImage(file="UX_UI/images/logo_ux_system.png")
    # canvas.create_image(100, 100, image=photoimage)

    for jogo, callback in zip(lista_jogos, lista_callbacks):
        # Cria um botão para cada jogo na lista
        botao_jogo = tk.Button(background, text=jogo, command=callback)
        botao_jogo.grid(row=lista_jogos.index(jogo) + 2, column=0, padx=20, pady=10)

    return background
