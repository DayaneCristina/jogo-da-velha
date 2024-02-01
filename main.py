from interface import JogoDaVelhaGUI
from jogodavelha import JogoDaVelha
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha()
    app = JogoDaVelhaGUI(root, jogo)
    root.mainloop()
