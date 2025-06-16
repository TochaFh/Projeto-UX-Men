import tkinter as tk
from PIL import Image, ImageTk

# Caminho da imagem de fundo
BACKGROUND_IMAGE = "UX_UI/images/magic_BG.png"

janela = tk.Tk()
#janela.attributes('-fullscreen', True)  # Janela em tela cheia
def pogers_function():
  if play_of_the_game:
    pog()
# Carrega e redimensiona a imagem para o tamanho da tela
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
img = Image.open(BACKGROUND_IMAGE).resize((screen_width, screen_height))
bg_img = ImageTk.PhotoImage(img)

# Cria um label para a imagem de fundo
background_label = tk.Label(janela, image=bg_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Função para exibir uma mensagem quando o botão for clicado
def exibir_mensagem():
  print("O botão foi clicado!")

janela.title("Posicionamento com Grid")

# Adicionar um rótulo
rotulo = tk.Label(background_label, text="Olá, Tkinter!")
rotulo.grid(row=1, column=0, padx=20, pady=20)  # Posicionado na primeira linha e primeira coluna

# Adicionar um botão
botao = tk.Button(background_label, text="Clique Aqui", command=exibir_mensagem)
botao.grid(row=2, column=0, padx=20, pady=20)  # Posicionado na segunda linha e primeira coluna

# Define um tamanho mínimo inicial para a janela
janela.minsize(800, 500)

# Executar o loop principal
janela.mainloop()