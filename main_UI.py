import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()

#import UX-UI.menu_ux




# Função para exibir uma mensagem quando o botão for clicado
def exibir_mensagem():
  print("O botão foi clicado!")

janela.title("Posicionamento com Grid")

frame_geral = tk.Frame(janela)

# Logo do app
logo = tk.Label(frame_geral, text="Projeto UX-Man")
logo.grid(row=1, column=0, padx=20, pady=20)

# Opções de jogos:

# magic
botao = tk.Button(frame_geral, text="Magic: The Gathering", command=exibir_mensagem)
botao.grid(row=2, column=0, padx=20, pady=20)

# coup disney
botao = tk.Button(frame_geral, text="Coup Disney", command=exibir_mensagem)
botao.grid(row=3, column=0, padx=20, pady=10)

frame_geral.pack()

# Define um tamanho mínimo inicial para a janela
janela.minsize(800, 500)

# Executar o loop principal
janela.mainloop()
