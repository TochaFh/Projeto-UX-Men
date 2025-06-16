import tkinter as tk
from PIL import Image, ImageTk
from UX_System.uxsystem import UXSystem

def main():
    global janela, uxsystem
    uxsystem = UXSystem()

    janela = tk.Tk()

    import UX_UI.menu_ux as menu
    menu.setup(janela, ["Magic: The Gathering", "Coup Disney"], [run_magic, run_coup_disney])

    #janela.wm_attributes('-transparentcolor','white')
    janela.title("Posicionamento com Grid")
    janela.minsize(800, 500)
    #janela.protocol("WM_DELETE_WINDOW", uxsystem.close)
    janela.mainloop()

def run_magic():
    global uxsystem

    uxsystem.start()

    import UX_Magic.magic_ui as magic_ui
    bg, holder = magic_ui.setup(janela)

    import UX_Magic.main_magic as main_magic
    main_magic.setup(uxsystem, holder)

def run_coup_disney():
    print("Coup Disney game setup not implemented yet.")

if __name__ == "__main__":
    main()