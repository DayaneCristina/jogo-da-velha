import tkinter as tk
from tkinter import messagebox
from jogodavelha import JogoDaVelha

class JogoDaVelhaGUI:
    def __init__(self, master, jogo):
        self.master = master
        self.master.title("Jogo da Velha")
        self.jogo = jogo

        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(master, text='', font=('normal', 20), width=8, height=3,
                                            command=lambda linha=i, coluna=j: self.fazer_jogada(linha, coluna))
                self.botoes[i][j].grid(row=i, column=j)

    def fazer_jogada(self, linha, coluna):
        resultado = self.jogo.fazer_jogada(linha, coluna)

        if resultado:
            messagebox.showinfo("Fim de Jogo", resultado)
            self.jogo.reiniciar_jogo()
            self.atualizar_interface()

        self.atualizar_interface()

    def atualizar_interface(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=self.jogo.tabuleiro[i][j])

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha()
    app = JogoDaVelhaGUI(root, jogo)
    root.mainloop()
