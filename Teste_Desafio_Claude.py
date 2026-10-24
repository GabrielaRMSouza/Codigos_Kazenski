# -*- coding: utf-8 -*-
# Coração feito de palavras! 💗
# O contorno e o interior são formados por frases, e o coração bate.
#
# Como rodar:  python coracao.py     (aperte ESC para fechar)

import math
import tkinter as tk
import tkinter.font as tkfont
from bisect import bisect_right

# ---------- ✏️ PERSONALIZE AQUI ----------
# Troque, adicione ou remova frases à vontade (o nome de alguém, uma data, um apelido...)
FRASES = ["Amo-te", "Para Sempre", "Meu Coração", "Só Tu", "Contigo", "Amor", "Eternamente"]

LARGURA, ALTURA = 760, 700
FUNDO = "#12040a"                                    # cor do fundo (quase preto)
COR_CONTORNO = "#ff0a3c"                             # vermelho forte do contorno
CORES_INTERIOR = ["#ff4d6d", "#ff1744", "#e0102f", "#c9082a", "#ff6b81"]  # tons de vermelho
TAMANHO_FONTE = 12
FAMILIA_FONTE = "Arial"
SEPARADOR = "  ·  "                                 # o que fica entre as frases
ESCALA = 17                                          # tamanho do coração (pixels por unidade)

# ---------- Janela ----------
janela = tk.Tk()
janela.title("Coração de palavras")
janela.configure(bg=FUNDO)
janela.resizable(False, False)
janela.bind("<Escape>", lambda evento: janela.destroy())

tela = tk.Canvas(janela, width=LARGURA, height=ALTURA, bg=FUNDO, highlightthickness=0)
tela.pack()

fonte = tkfont.Font(family=FAMILIA_FONTE, size=TAMANHO_FONTE)
fonte_negrito = tkfont.Font(family=FAMILIA_FONTE, size=TAMANHO_FONTE + 2, weight="bold")

CENTRO_X, CENTRO_Y = LARGURA / 2, ALTURA / 2


# ---------- 1. A forma do coração ----------
def curva_do_coracao(pontos=240):
    """Fórmula matemática clássica do coração (x e y em 'unidades')."""
    curva = []
    for i in range(pontos):
        t = 2 * math.pi * i / pontos
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        curva.append((x, y + 2.5))   # +2.5 deixa o coração centralizado
    return curva


CURVA = curva_do_coracao()


def poligono(escala, fator=1.0):
    """Transforma a curva em pontos da tela. 'fator' menor que 1 faz um coração menor por dentro."""
    k = ESCALA * escala * fator
    return [(CENTRO_X + k * x, CENTRO_Y - k * y) for x, y in CURVA]


# ---------- 2. Descobrindo onde há "coração" em cada linha da tela ----------
def intervalos(pol, y):
    """Para uma altura y, devolve os trechos [x1, x2] que estão DENTRO do coração."""
    cruzamentos = []
    for i in range(len(pol)):
        x1, y1 = pol[i]
        x2, y2 = pol[(i + 1) % len(pol)]
        if (y1 <= y < y2) or (y2 <= y < y1):          # a linha horizontal cruza essa aresta?
            t = (y - y1) / (y2 - y1)
            cruzamentos.append(x1 + t * (x2 - x1))
    cruzamentos.sort()
    return [(cruzamentos[i], cruzamentos[i + 1]) for i in range(0, len(cruzamentos) - 1, 2)]


def estreitar(trecho, outros):
    """Garante que o texto (que tem altura) cabe dentro do coração, em cima e embaixo."""
    a, b = trecho
    for lista in outros:
        achou = False
        for oa, ob in lista:
            if oa < b and ob > a:                      # trechos que se sobrepõem
                a, b = max(a, oa), min(b, ob)
                achou = True
                break
        if not achou:
            return None
    return (a, b)


# ---------- 3. Palavras no INTERIOR ----------
def desenhar_interior(escala):
    pol = poligono(escala, fator=0.85)                 # um pouco menor para sobrar espaço p/ o contorno
    altura_linha = TAMANHO_FONTE * 1.9
    meio = altura_linha * 0.35
    ys = [p[1] for p in pol]
    k_ini = math.floor((min(ys) - CENTRO_Y) / altura_linha)
    k_fim = math.ceil((max(ys) - CENTRO_Y) / altura_linha)

    for k in range(k_ini, k_fim + 1):                  # k = número da linha (fixo, não "pula" no batimento)
        y = CENTRO_Y + k * altura_linha
        cima, baixo = intervalos(pol, y - meio), intervalos(pol, y + meio)
        for trecho in intervalos(pol, y):
            ok = estreitar(trecho, (cima, baixo))
            if ok is None:
                continue
            a, b = ok
            disponivel = (b - a) - 10

            # Vai juntando frases enquanto couberem na largura da linha
            linha, j = "", 0
            while True:
                frase = FRASES[(k * 2 + j) % len(FRASES)]
                teste = frase if not linha else linha + SEPARADOR + frase
                if fonte.measure(teste) > disponivel:
                    break
                linha, j = teste, j + 1
            if linha:
                tela.create_text((a + b) / 2, y, text=linha, font=fonte,
                                 fill=CORES_INTERIOR[k % len(CORES_INTERIOR)])


# ---------- 4. Palavras no CONTORNO (giradas seguindo a curva) ----------
def desenhar_contorno(escala):
    base = poligono(escala)
    n4 = len(base) // 4                                # começa numa lateral (não numa ponta)
    base = base[n4:] + base[:n4]
    pts = base + [base[0]]                             # fecha a curva
    acumulado = [0.0]
    for i in range(1, len(pts)):
        acumulado.append(acumulado[-1] + math.dist(pts[i - 1], pts[i]))
    total = acumulado[-1]

    def ponto_em(s):
        i = min(max(bisect_right(acumulado, s) - 1, 0), len(pts) - 2)
        seg = acumulado[i + 1] - acumulado[i] or 1
        t = (s - acumulado[i]) / seg
        return (pts[i][0] + t * (pts[i + 1][0] - pts[i][0]),
                pts[i][1] + t * (pts[i + 1][1] - pts[i][1]))

    colocadas = []                                      # pontos já ocupados por outras palavras

    def amostras(s, w):
        return [ponto_em(s + w * f) for f in (0, 0.25, 0.5, 0.75, 1)]

    def bate_em_outra(pontos):
        return any(math.dist(p, q) < 17 for p in pontos for q in colocadas)

    s, i = 6, 0
    while True:
        frase = FRASES[i % len(FRASES)]
        w = fonte_negrito.measure(frase)
        # Nas pontas do coração a curva dobra rápido: anda um pouquinho até a palavra
        # ficar reta e sem encostar em outra.
        while s + w < total and (math.dist(ponto_em(s), ponto_em(s + w)) < 0.93 * w
                                 or bate_em_outra(amostras(s, w))):
            s += 3
        if s + w > total - 6:
            break
        colocadas.extend(amostras(s, w))
        x, y = ponto_em(s + w / 2)
        (x1, y1), (x2, y2) = ponto_em(s), ponto_em(s + w)
        angulo = math.degrees(math.atan2(-(y2 - y1), x2 - x1))
        if angulo > 90:                                 # evita texto de cabeça para baixo
            angulo -= 180
        elif angulo <= -90:
            angulo += 180
        tela.create_text(x, y, text=frase, font=fonte_negrito, fill=COR_CONTORNO, angle=angulo)
        s += w + 18
        i += 1


# ---------- 5. Animação: o coração bate ----------
tempo = 0.0


def batimento(t):
    """Duas batidinhas seguidas: 'tum-tum' ... 'tum-tum'."""
    return 1 + 0.045 * math.sin(t) ** 12 + 0.025 * math.sin(t - 0.8) ** 12


def animar():
    global tempo
    tempo += 0.12
    escala = batimento(tempo)
    tela.delete("all")
    desenhar_interior(escala)
    desenhar_contorno(escala)
    janela.after(40, animar)                            # ~25 quadros por segundo


animar()
janela.mainloop()