
import tkinter as tk
import math

LARGURA, ALTURA = 900, 650
SEGMENTOS = 65
DISTANCIA = 8

janela = tk.Tk()
janela.title("LimSystem - Scorpion Cursor")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.configure(bg="black")
janela.resizable(False, False)

tela = tk.Canvas(
    janela,
    width=LARGURA,
    height=ALTURA,
    bg="black",
    highlightthickness=0
)
tela.pack()

mouse = [LARGURA / 2, ALTURA / 2]
nos = [[mouse[0] - i * DISTANCIA, mouse[1]]
       for i in range(SEGMENTOS)]

tempo = 0


def mover_mouse(event):
    mouse[0] = event.x
    mouse[1] = event.y


tela.bind("<Motion>", mover_mouse)


class LimSystem:
    def __init__(self, nodes, creature):
        self.nodes = nodes
        self.creature = creature
        self.length = len(nodes)

    def moveTo(self, x, y):
        # A cabeça se move suavemente em direção ao mouse
        hx, hy = self.nodes[0]
        self.nodes[0] = (
            hx + (x - hx) * 0.35,
            hy + (y - hy) * 0.35
        )

        # Cada segmento acompanha o anterior
        for i in range(1, self.length):
            ax, ay = self.nodes[i - 1]
            bx, by = self.nodes[i]

            dx, dy = bx - ax, by - ay
            distancia = math.hypot(dx, dy)

            if distancia > DISTANCIA:
                self.nodes[i] = (
                    ax + dx / distancia * DISTANCIA,
                    ay + dy / distancia * DISTANCIA
                )

    def update(self):
        self.moveTo(mouse[0], mouse[1])


escorpiao = LimSystem(nos, "scorpion")


def linha(a, b, cor="#bcbcc8", espessura=1):
    tela.create_line(
        a[0], a[1], b[0], b[1],
        fill=cor, width=espessura
    )


def animar():
    global tempo
    tempo += 0.07
    tela.delete("all")

    escorpiao.update()
    pontos = escorpiao.nodes

    # Corpo segmentado
    for i in range(len(pontos) - 1):
        a, b = pontos[i], pontos[i + 1]

        linha(a, b, "#777783", 2)

        dx, dy = b[0] - a[0], b[1] - a[1]
        d = math.hypot(dx, dy) or 1
        nx, ny = -dy / d, dx / d

        largura = max(2, 6 - i * 0.055)

        p1 = (a[0] + nx * largura, a[1] + ny * largura)
        p2 = (a[0] - nx * largura, a[1] - ny * largura)

        linha(p1, p2, "#c3c3ce", 1)

        tela.create_oval(
            a[0] - 1.5, a[1] - 1.5,
            a[0] + 1.5, a[1] + 1.5,
            fill="#f1f1ff", outline=""
        )

    # Pernas articuladas
    for i in range(5, 33, 4):
        x, y = pontos[i]
        anterior = pontos[i - 1]
        seguinte = pontos[i + 1]

        angulo = math.atan2(
            seguinte[1] - anterior[1],
            seguinte[0] - anterior[0]
        )

        for lado in (-1, 1):
            fase = math.sin(tempo * 3 + i) * 0.15

            a = (
                x + math.cos(angulo + lado * 1.0 + fase) * 13,
                y + math.sin(angulo + lado * 1.0 + fase) * 13
            )

            b = (
                a[0] + math.cos(angulo + lado * 1.5 + fase) * 14,
                a[1] + math.sin(angulo + lado * 1.5 + fase) * 14
            )

            linha((x, y), a, "#aaaab8", 1)
            linha(a, b, "#ededff", 1)

            tela.create_oval(
                b[0] - 2, b[1] - 2,
                b[0] + 2, b[1] + 2,
                fill="#eeeeff", outline=""
            )

    # Cabeça
    x, y = pontos[0]
    tela.create_oval(
        x - 6, y - 5, x + 6, y + 5,
        outline="#eeeeff", width=2
    )

    # Pinças
    for lado in (-1, 1):
        a = (x + lado * 4, y + lado * 2)
        b = (x + lado * 15, y + lado * 8)
        c = (x + lado * 23, y + lado * 3)

        linha(a, b, "#eeeeff", 2)
        linha(b, c, "#eeeeff", 2)

    # Cauda com ponta levantada
    base = pontos[-1]
    anterior = pontos[-2]

    angulo = math.atan2(
        base[1] - anterior[1],
        base[0] - anterior[0]
    )

    p1 = (
        base[0] + math.cos(angulo - 0.5) * 12,
        base[1] + math.sin(angulo - 0.5) * 12
    )

    p2 = (
        p1[0] + math.cos(angulo - 1.4) * 14,
        p1[1] + math.sin(angulo - 1.4) * 14
    )

    linha(base, p1, "#dddded", 2)
    linha(p1, p2, "#eeeeff", 2)

    tela.create_oval(
        p2[0] - 3, p2[1] - 3,
        p2[0] + 3, p2[1] + 3,
        fill="#ffffff", outline=""
    )

    tela.create_text(
        15, 15,
        anchor="nw",
        text="LIMSYSTEM // CURSOR TRACKING",
        fill="#888899",
        font=("Consolas", 11)
    )

    janela.after(16, animar)


animar()
janela.mainloop()
