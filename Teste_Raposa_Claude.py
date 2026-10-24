# -*- coding: utf-8 -*-
# Raposa animada com a biblioteca turtle (já vem instalada com o Python!)
#
# Como rodar:  python raposa.py
# O que acontece: a raposa é desenhada passo a passo e depois pisca de tempos em tempos.

import turtle

# ---------- 1. Preparando a tela ----------
tela = turtle.Screen()
tela.setup(600, 500)            # largura e altura da janela
tela.bgcolor("#cfe8f3")         # cor do fundo (azul clarinho)
tela.title("Raposa")

# ---------- 2. A "caneta" que desenha ----------
pena = turtle.Turtle()
pena.hideturtle()               # esconde a setinha
pena.speed(6)                   # 1 = lento, 10 = rápido, 0 = instantâneo
pena.pensize(3)

# Cores (em hexadecimal)
LARANJA = "#e8742a"
MARROM = "#3b2314"
BRANCO = "#fff7ec"


# ---------- 3. Funções para não repetir código ----------
def preencher(pontos, cor):
    """Desenha um polígono ligando os pontos e pinta por dentro."""
    pena.penup()
    pena.goto(pontos[0])        # vai até o primeiro ponto sem desenhar
    pena.pendown()
    pena.color(MARROM, cor)     # (cor do contorno, cor do preenchimento)
    pena.begin_fill()
    for ponto in pontos[1:]:    # liga cada ponto seguinte
        pena.goto(ponto)
    pena.goto(pontos[0])        # fecha a forma
    pena.end_fill()


def circulo(x, y, raio, cor):
    """Desenha um círculo com centro em (x, y)."""
    pena.penup()
    pena.goto(x, y - raio)      # o turtle começa o círculo pela parte de baixo
    pena.pendown()
    pena.color(cor, cor)
    pena.begin_fill()
    pena.circle(raio)
    pena.end_fill()


# ---------- 4. Desenhando a raposa ----------
# Orelhas (cada uma é um triângulo)
preencher([(-125, 60), (-115, 170), (-30, 90)], LARANJA)   # esquerda
preencher([(125, 60), (115, 170), (30, 90)], LARANJA)      # direita

# Cabeça
preencher([(-125, 60), (-30, 90), (30, 90), (125, 60), (0, -130)], LARANJA)

# Parte de dentro das orelhas
preencher([(-105, 85), (-100, 140), (-60, 95)], MARROM)
preencher([(105, 85), (100, 140), (60, 95)], MARROM)

# Bochechas brancas
preencher([(-125, 60), (-18, -20), (0, -130)], BRANCO)
preencher([(125, 60), (18, -20), (0, -130)], BRANCO)

# Focinho
circulo(0, -118, 12, MARROM)

# Nome embaixo
pena.penup()
pena.goto(0, -190)
pena.color(MARROM)
pena.write("Raposa", align="center", font=("Arial", 20, "bold"))

# ---------- 5. Os olhos (cada olho é uma tartaruga em forma de círculo) ----------
olhos = []
for x in (-55, 55):
    olho = turtle.Turtle()
    olho.shape("circle")
    olho.color(MARROM)
    olho.penup()
    olho.speed(0)
    olho.goto(x, 25)
    olho.shapesize(1.2, 1.2)    # (altura, largura)
    olhos.append(olho)


# ---------- 6. Animação: piscar ----------
def fechar_olhos():
    for olho in olhos:
        olho.shapesize(0.1, 1.2)    # achata o olho = olho fechado
    tela.update()
    tela.ontimer(abrir_olhos, 150)  # daqui a 150 ms, abre de novo


def abrir_olhos():
    for olho in olhos:
        olho.shapesize(1.2, 1.2)    # volta ao tamanho normal
    tela.update()
    tela.ontimer(fechar_olhos, 2500)  # daqui a 2,5 segundos, pisca outra vez


tela.ontimer(fechar_olhos, 1500)    # primeira piscada
tela.mainloop()                     # mantém a janela aberta