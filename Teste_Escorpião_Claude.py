# -*- coding: utf-8 -*-
# Escorpião 2.0 🦂 — segue o mouse, anda com passos de verdade, tem cauda curvada e pinças que abrem e fecham.
# (Melhorado a partir da versão do Atlas.)
#
# Como rodar:  python escorpiao_v2.py     |     mexa o mouse dentro da janela!

import math
import tkinter as tk

# ---------- ✏️ PERSONALIZE AQUI ----------
LARGURA, ALTURA = 900, 650
FUNDO = "#0b0b10"
COR_CORPO = "#d9952f"          # cor das placas do corpo
COR_CORPO_ESCURO = "#7a4a12"   # contorno das placas
COR_PERNA = "#e8b05a"
COR_FERRAO = "#ff5a3c"

QTD_SEGMENTOS = 14             # tamanho do corpo (menos = escorpião mais "curtinho")
ESPACO = 10                    # distância entre os segmentos
VELOCIDADE_MAX = 4.5           # velocidade máxima da cabeça (pixels por quadro)
QTD_CAUDA = 10                 # segmentos da cauda
TAM_CAUDA = 9                  # tamanho de cada segmento da cauda
# Largura (raio) de cada segmento do corpo: cabeça, tórax largo, abdômen afinando
RAIOS = [8, 11, 12, 12, 11.5, 11, 10, 9, 8.2, 7.4, 6.6, 5.8, 5, 4.4]

# Tamanho dos ossinhos das pernas
OSSO_1, OSSO_2 = 18, 22

# ---------- Janela e mouse ----------
janela = tk.Tk()
janela.title("Escorpião 2.0")
janela.configure(bg=FUNDO)
janela.resizable(False, False)

tela = tk.Canvas(janela, width=LARGURA, height=ALTURA, bg=FUNDO, highlightthickness=0)
tela.pack()

mouse = [LARGURA / 2, ALTURA / 2]


def mover_mouse(evento):
    mouse[0], mouse[1] = evento.x, evento.y


tela.bind("<Motion>", mover_mouse)


# ---------- Funções de ajuda ----------
def direcao(angulo, comprimento):
    """Dá o deslocamento (dx, dy) de um passo de certo tamanho num certo ângulo."""
    return math.cos(angulo) * comprimento, math.sin(angulo) * comprimento


def linha(a, b, cor, espessura):
    tela.create_line(a[0], a[1], b[0], b[1], fill=cor, width=espessura,
                     capstyle="round", joinstyle="round")


def bolinha(p, raio, cor, contorno="", espessura=1):
    tela.create_oval(p[0] - raio, p[1] - raio, p[0] + raio, p[1] + raio,
                     fill=cor, outline=contorno, width=espessura)


# ---------- A perna: o pé fica PARADO no chão até precisar dar um passo ----------
class Perna:
    def __init__(self, no, lado, grupo, avanco):
        self.no = no            # em qual segmento do corpo a perna está presa
        self.lado = lado        # -1 = um lado do corpo, +1 = o outro
        self.grupo = grupo      # 0 ou 1: um grupo anda enquanto o outro fica firme
        self.avanco = avanco    # pernas da frente apontam pra frente, as de trás pra trás
        self.pe = None          # onde o pé está
        self.alvo = None        # para onde o pé está indo
        self.andando = False
        self.quadril = (0, 0)
        self.lateral = (0, 0)


class Escorpiao:
    def __init__(self):
        x0, y0 = LARGURA / 2 - 220, ALTURA / 2   # começa à esquerda e caminha até o mouse
        self.nos = [[x0 - i * ESPACO, y0] for i in range(QTD_SEGMENTOS)]
        self.pernas = []
        for par, no in enumerate((2, 4, 6, 8)):          # 4 pares de pernas
            for lado in (-1, 1):
                grupo = (par + (1 if lado > 0 else 0)) % 2   # alterna: tipo "esquerda-direita"
                self.pernas.append(Perna(no, lado, grupo, avanco=14 - 8 * par))
        self.tempo = 0.0
        self.velocidade = 0.0

    # --- movimento do corpo ---
    def frente(self, i):
        """Direção (vetor unitário) para onde o segmento i está 'olhando'."""
        a = self.nos[max(i - 1, 0)]
        b = self.nos[min(i + 1, QTD_SEGMENTOS - 1)]
        dx, dy = a[0] - b[0], a[1] - b[1]
        d = math.hypot(dx, dy) or 1
        return dx / d, dy / d

    def mover(self, alvo_x, alvo_y):
        cabeca = self.nos[0]
        dx, dy = alvo_x - cabeca[0], alvo_y - cabeca[1]
        dist = math.hypot(dx, dy)
        self.velocidade = 0.0
        if dist > 4:                                      # perto demais? fica parado
            passo = min(dist * 0.12, VELOCIDADE_MAX)      # acelera suave, com limite de velocidade
            cabeca[0] += dx / dist * passo
            cabeca[1] += dy / dist * passo
            self.velocidade = passo

        # cada segmento "puxa" o próximo, mantendo sempre a mesma distância
        for i in range(1, QTD_SEGMENTOS):
            ax, ay = self.nos[i - 1]
            no = self.nos[i]
            dx, dy = no[0] - ax, no[1] - ay
            d = math.hypot(dx, dy) or 0.0001
            no[0] = ax + dx / d * ESPACO
            no[1] = ay + dy / d * ESPACO

    # --- passos das pernas ---
    def atualizar_pernas(self):
        andando = [False, False]
        for p in self.pernas:
            if p.andando:
                andando[p.grupo] = True

        for p in self.pernas:
            x, y = self.nos[p.no]
            fx, fy = self.frente(p.no)
            nx, ny = -fy * p.lado, fx * p.lado            # direção "para o lado" do corpo
            p.lateral = (nx, ny)
            p.quadril = (x + nx * 7, y + ny * 7)

            # posição de descanso: onde o pé "gostaria" de estar
            rx = p.quadril[0] + nx * 20 + fx * p.avanco
            ry = p.quadril[1] + ny * 20 + fy * p.avanco

            if p.pe is None:                              # primeira vez: pé já no lugar
                p.pe, p.alvo = [rx, ry], [rx, ry]

            if not p.andando:
                distancia = math.hypot(p.pe[0] - rx, p.pe[1] - ry)
                # Dá o passo se o pé está longe e o outro grupo está firme no chão.
                # (Se o pé ficou LONGE DEMAIS, anda de qualquer jeito, para não esticar a perna.)
                if distancia > 11 and (not andando[1 - p.grupo] or distancia > 22):
                    p.andando = True
                    andando[p.grupo] = True
                    # passa da posição de descanso, rumo à frente (mais quando o corpo anda rápido)
                    adiante = 8 + self.velocidade * 6
                    p.alvo = [rx + fx * adiante, ry + fy * adiante]
            else:
                p.pe[0] += (p.alvo[0] - p.pe[0]) * 0.5     # pé desliza até o alvo
                p.pe[1] += (p.alvo[1] - p.pe[1]) * 0.5
                if math.hypot(p.alvo[0] - p.pe[0], p.alvo[1] - p.pe[1]) < 1.5:
                    p.andando = False

    # --- desenho ---
    def desenhar_perna(self, p):
        hx, hy = p.quadril
        dx, dy = p.pe[0] - hx, p.pe[1] - hy
        dist = math.hypot(dx, dy) or 0.0001
        ux, uy = dx / dist, dy / dist
        d = min(max(dist, 4), OSSO_1 + OSSO_2 - 0.5)       # a perna não estica além do limite
        # Cinemática inversa de 2 ossos: acha onde fica o "joelho"
        a = (OSSO_1 ** 2 - OSSO_2 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(max(OSSO_1 ** 2 - a ** 2, 0))
        px, py = -uy, ux
        if px * p.lateral[0] + py * p.lateral[1] < 0:      # joelho dobra para fora do corpo
            px, py = -px, -py
        joelho = (hx + ux * a + px * h, hy + uy * a + py * h)
        pe = (hx + ux * d, hy + uy * d)
        linha((hx, hy), joelho, COR_PERNA, 3)
        linha(joelho, pe, COR_PERNA, 2)
        bolinha(joelho, 2.2, COR_CORPO)
        bolinha(pe, 1.8, COR_PERNA)

    def desenhar_pinca(self, lado):
        hx, hy = self.nos[0]
        fx, fy = self.frente(0)
        base = math.atan2(fy, fx)
        ombro = (hx + fx * 5 - fy * lado * 7, hy + fy * 5 + fx * lado * 7)

        balanco = math.sin(self.tempo * 2 + lado) * 0.08
        cotovelo = tuple(o + d for o, d in zip(ombro, direcao(base + lado * 0.85 + balanco, 15)))
        ang_mao = base - lado * 0.35 + balanco
        mao = tuple(o + d for o, d in zip(cotovelo, direcao(ang_mao, 14)))

        linha(ombro, cotovelo, COR_CORPO, 4)
        linha(cotovelo, mao, COR_CORPO, 4)

        aberta = 0.28 + 0.2 * math.sin(self.tempo * 2.2)    # abre e fecha
        for sinal in (1, -1):                                # dois "dedos" da pinça
            ang = ang_mao + sinal * aberta
            meio = tuple(m + d for m, d in zip(mao, direcao(ang, 8)))
            ponta = tuple(m + d for m, d in zip(meio, direcao(ang - sinal * 0.7, 8)))
            linha(mao, meio, COR_CORPO, 3)
            linha(meio, ponta, COR_CORPO, 2)
        bolinha(mao, 4.5, COR_CORPO, COR_CORPO_ESCURO, 1)

    def desenhar_cauda(self):
        fim = self.nos[-1]
        anterior = self.nos[-2]
        angulo = math.atan2(fim[1] - anterior[1], fim[0] - anterior[0])   # apontando para trás
        ponto = (fim[0], fim[1])
        pontos = [ponto]
        angulos = []
        for k in range(QTD_CAUDA):
            # a cada segmento a cauda curva um pouco mais (e balança de leve)
            angulo += 0.14 + 0.025 * k + 0.06 * math.sin(self.tempo * 2 + k * 0.6)
            dx, dy = direcao(angulo, TAM_CAUDA)
            ponto = (ponto[0] + dx, ponto[1] + dy)
            pontos.append(ponto)
            angulos.append(angulo)

        for k in range(len(pontos) - 1):
            raio = max(2.2, 4.2 - k * 0.2)
            linha(pontos[k], pontos[k + 1], COR_CORPO_ESCURO, raio * 2 + 2)
        for k in range(len(pontos) - 1):
            raio = max(2.2, 4.2 - k * 0.2)
            linha(pontos[k], pontos[k + 1], COR_CORPO, raio * 2)

        # Ferrão: bolinha + espinho pontudo
        ponta = pontos[-1]
        ang = angulos[-1]
        bolinha(ponta, 5, COR_CORPO, COR_CORPO_ESCURO, 2)
        (tx, ty), (lx, ly) = direcao(ang, 12), direcao(ang + math.pi / 2, 3.5)
        tela.create_polygon(ponta[0] + lx, ponta[1] + ly,
                            ponta[0] - lx, ponta[1] - ly,
                            ponta[0] + tx, ponta[1] + ty,
                            fill=COR_FERRAO, outline="")

    def desenhar(self):
        for p in self.pernas:                      # 1º as pernas (ficam por baixo)
            self.desenhar_perna(p)

        for i in range(QTD_SEGMENTOS - 1, -1, -1):  # corpo: de trás pra frente, a cabeça fica por cima
            cor = COR_CORPO if i % 2 == 0 else "#c2822a"
            bolinha(self.nos[i], RAIOS[i], cor, COR_CORPO_ESCURO, 2)

        # Olhinhos
        hx, hy = self.nos[0]
        fx, fy = self.frente(0)
        for lado in (-1, 1):
            bolinha((hx + fx * 3 - fy * lado * 3.5, hy + fy * 3 + fx * lado * 3.5), 1.6, "#101010")

        self.desenhar_pinca(-1)
        self.desenhar_pinca(1)
        self.desenhar_cauda()                      # cauda por cima, curvada sobre o corpo


escorpiao = Escorpiao()


def animar():
    escorpiao.tempo += 0.07
    escorpiao.mover(mouse[0], mouse[1])
    escorpiao.atualizar_pernas()

    tela.delete("all")
    escorpiao.desenhar()
    tela.create_text(15, 15, anchor="nw", fill="#888899", font=("Arial", 11),
                     text="Escorpião 2.0  //  mexa o mouse")
    janela.after(16, animar)                       # ~60 quadros por segundo


animar()
janela.mainloop()