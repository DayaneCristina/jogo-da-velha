class JogoDaVelha:
    def __init__(self):
        self.jogador_atual = 'X'
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    def fazer_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = self.jogador_atual

            if self.verificar_vitoria():
                return f"Jogador {self.jogador_atual} venceu!"
            elif all(self.tabuleiro[i][j] != ' ' for i in range(3) for j in range(3)):
                return "Empate"
            else:
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
                return None

    def verificar_vitoria(self):
        for i in range(3):
            if all(self.tabuleiro[i][j] == self.jogador_atual for j in range(3)) or \
                    all(self.tabuleiro[j][i] == self.jogador_atual for j in range(3)):
                return True

        if all(self.tabuleiro[i][i] == self.jogador_atual for i in range(3)) or \
                all(self.tabuleiro[i][2 - i] == self.jogador_atual for i in range(3)):
            return True

        return False

    def reiniciar_jogo(self):
        self.jogador_atual = 'X'
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
