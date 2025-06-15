import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

BACKGROUND_IMAGE = "UX-UI/images/fundo.png"

janela = tk.Tk()
janela.title("Projeto UX-Man")
janela.minsize(800, 500)

# Pega tamanho da tela
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

# Carrega imagem de fundo
img = Image.open(BACKGROUND_IMAGE).resize((screen_width, screen_height))
bg_img = ImageTk.PhotoImage(img)

# Label de fundo
background_label = tk.Label(janela, image=bg_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Função de clique
def exibir_mensagem(texto):
    print(f"Botão '{texto}' foi clicado!")

# Fonte personalizada
titulo_font = font.Font(family='Helvetica', size=24, weight='bold')
botao_font = font.Font(family='Helvetica', size=16)

# Frame lateral esquerdo
menu_frame = tk.Frame(janela, bg='#222', width=300, height=screen_height)
menu_frame.pack(side='left', fill='y')

# Título
titulo = tk.Label(menu_frame, text="Projeto UX-Man", font=titulo_font, fg='white', bg='#222')
titulo.pack(pady=(30, 20), padx=20, anchor='w')

# Função para criar botões de menu
def criar_botao(texto):
    botao = tk.Button(
        menu_frame,
        text=texto,
        command=lambda: exibir_mensagem(texto),
        font=botao_font,
        bg='#444',
        fg='white',
        activebackground='#555',
        activeforeground='white',
        bd=0,
        padx=20,
        pady=10,
        anchor='w'
    )
    botao.pack(fill='x', padx=20, pady=10)
    # Efeito hover
    botao.bind("<Enter>", lambda e: botao.config(bg='#555'))
    botao.bind("<Leave>", lambda e: botao.config(bg='#444'))

# Botões com os mesmos textos
criar_botao("Magic: The Gathering")
criar_botao("Coup Disney")

janela.mainloop()
