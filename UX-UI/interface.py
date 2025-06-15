import tkinter as tk

def exibir_mensagem():
    print("Botão clicado!")



janela = tk.Tk()
janela.title("Hello World")


label = tk.Label(janela, text="Oláaaaa!!")
botao = tk.Button(janela, text="Clique aqui", command=exibir_mensagem)
label.pack(
        padx=20,  # Espaçamento interno horizontal
        pady=20   # Espaçamento interno vertical
)
botao.pack()

janela.mainloop()
