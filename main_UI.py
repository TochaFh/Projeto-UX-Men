import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()

import UX_UI.menu_ux as menu

menu.setup(janela, [], [])


janela.title("Posicionamento com Grid")
janela.minsize(800, 500)
janela.mainloop()
