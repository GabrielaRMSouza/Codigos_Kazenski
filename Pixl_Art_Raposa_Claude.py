# -*- coding: utf-8 -*-
# Pixel art: "Raposa sob a lua vermelha" 🦊🌙
# A imagem é uma grade pequena (64x48 quadradinhos) que depois é ampliada.
# Precisa da biblioteca Pillow:  pip install pillow
# Como rodar:  python pixel_raposa.py   (gera um .png e um .gif animado)

import math
import random
from PIL import Image, ImageDraw

LARGURA, ALTURA, ZOOM = 64, 48, 12          # grade 64x48, ampliada 12 vezes
random.seed(7)


def cor(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# Matriz de "pontilhado": faz degradês parecerem pixel art em vez de borrados
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]

# ---------- Paleta ----------
CEU = [cor(c) for c in ("#0d0a1e", "#1a0f2e", "#2b1236", "#431538", "#5e1a3a")]
LUA_BASE, LUA_CLARA, LUA_CRATERA = cor("#d63a24"), cor("#f26b3a"), cor("#a8281c")
LUA_BRILHO = cor("#6b1c3a")
MONTANHA, CHAO, CHAO_BORDA = cor("#1b0d25"), cor("#08040d"), cor("#3b1230")
PINHEIRO, PINHEIRO_LONGE = cor("#0a0612"), cor("#160b20")
LARANJA, LARANJA_ESC, BRANCO = cor("#e8742a"), cor("#b9501a"), cor("#fff3e0")
ESCURO, BORDA_LUZ = cor("#2a1410"), cor("#ff9d5c")
ESTRELA, ESTRELA_FRACA = cor("#ffe8c8"), cor("#8f82c0")
VAGALUME = cor("#d8ff7a")

LUA_X, LUA_Y, LUA_R = 47, 15, 9


def altura_do_chao(x):
    """Altura do chão em cada coluna: um montinho suave onde a raposa senta."""
    return 41 - round(3 * math.exp(-((x - 24) / 12) ** 2)) + round(math.sin(x / 5))


# ---------- Cenário (não muda entre os quadros) ----------
def montar_cenario():
    img = Image.new("RGB", (LARGURA, ALTURA))
    px = img.load()

    # Céu em degradê pontilhado
    for y in range(ALTURA):
        for x in range(LARGURA):
            pos = min(y / 34 * (len(CEU) - 1), len(CEU) - 1.001)
            i, frac = int(pos), pos - int(pos)
            limiar = (BAYER[y % 4][x % 4] + 0.5) / 16
            px[x, y] = CEU[i + 1] if frac > limiar else CEU[i]

    # Lua e o brilho em volta dela
    for y in range(ALTURA):
        for x in range(LARGURA):
            d = math.hypot(x - LUA_X, y - LUA_Y)
            if d <= LUA_R:
                px[x, y] = LUA_CLARA if (x - LUA_X) + (y - LUA_Y) < -4 else LUA_BASE
            elif d <= LUA_R + 6:
                forca = 1 - (d - LUA_R) / 6
                if forca > (BAYER[y % 4][x % 4] + 0.5) / 16:
                    px[x, y] = LUA_BRILHO
    for cx, cy, r in ((44, 13, 2.3), (50, 19, 1.45), (46, 21, 1.45)):      # crateras
        for y in range(ALTURA):
            for x in range(LARGURA):
                if math.hypot(x - cx, y - cy) <= r:
                    px[x, y] = LUA_CRATERA

    # Montanhas ao longe
    for x in range(LARGURA):
        topo = round(31 + 3 * math.sin(x / 7 + 1) + 2 * math.sin(x / 3))
        for y in range(topo, ALTURA):
            px[x, y] = MONTANHA

    # Pinheiros
    def pinheiro(cx, base, altura, largura, cor_):
        camadas = 4
        seg = altura // camadas
        for c in range(camadas):
            topo = base - altura + c * seg
            lc = seg + 2
            larg = 3 + c * (largura - 3) / (camadas - 1)
            for r in range(lc):
                meia = larg / 2 * (r / lc) + 0.5
                for x in range(round(cx - meia), round(cx + meia) + 1):
                    if 0 <= x < LARGURA and 0 <= topo + r < ALTURA:
                        px[x, topo + r] = cor_
        for y in range(base - 2, base + 1):
            if 0 <= cx < LARGURA:
                px[cx, y] = cor_

    for cx, base, h, w in ((30, 36, 11, 7), (40, 37, 12, 8), (35, 36, 9, 6)):
        pinheiro(cx, base, h, w, PINHEIRO_LONGE)
    for cx, base, h, w in ((4, 40, 22, 11), (12, 41, 16, 9), (59, 41, 26, 12), (52, 41, 18, 9)):
        pinheiro(cx, base, h, w, PINHEIRO)

    # Chão (com um fiozinho de luz na borda)
    for x in range(LARGURA):
        topo = altura_do_chao(x)
        for y in range(topo, ALTURA):
            px[x, y] = CHAO
        px[x, topo] = CHAO_BORDA
    return img


# ---------- A raposa ----------
def montar_raposa(piscando=False):
    """Desenha a raposa numa camada transparente. Coordenadas: x p/ direita, y negativo = pra cima."""
    fx, fy = 24, altura_do_chao(24)
    camada = Image.new("RGBA", (LARGURA, ALTURA), (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)

    def poli(pontos, c):
        d.polygon([(fx + x, fy + y) for x, y in pontos], fill=c + (255,))

    def ponto(x, y, c):
        d.point((fx + x, fy + y), fill=c + (255,))

    poli([(-6, -2), (-11, -1), (-16, -4), (-18, -9), (-17, -14), (-14, -11), (-12, -7), (-8, -6)], LARANJA)   # cauda
    poli([(-6, -2), (-11, -1), (-16, -4), (-14, -5), (-9, -3)], LARANJA_ESC)                                   # sombra da cauda
    poli([(-18, -11), (-17, -14), (-14, -11), (-16, -9)], BRANCO)                                              # ponta branca

    poli([(-7, -1), (-9, -6), (-7, -11), (-3, -15), (2, -17), (5, -15), (6, -9), (5, -3), (4, 0), (-3, 0)], LARANJA)  # corpo
    poli([(-9, -6), (-7, -11), (-3, -10), (-3, -3), (-7, -1)], LARANJA_ESC)                                    # sombra da coxa
    poli([(3, -16), (6, -14), (6, -9), (5, -4), (3, -3), (3, -9)], BRANCO)                                     # peito
    poli([(3, -8), (6, -8), (6, 0), (3, 0)], LARANJA)                                                          # pata da frente
    poli([(3, -3), (6, -3), (6, 0), (3, 0)], ESCURO)                                                           # "meia" escura
    poli([(-4, -1), (1, -1), (1, 0), (-4, 0)], ESCURO)                                                         # pata de trás

    poli([(2, -17), (1, -21), (3, -23), (8, -23), (9, -21), (14, -18), (9, -16), (5, -16)], LARANJA)           # cabeça
    poli([(6, -18), (13, -18), (9, -16), (5, -16)], BRANCO)                                                    # focinho/bochecha
    poli([(2, -22), (2, -28), (5, -23)], LARANJA)                                                              # orelhas
    poli([(6, -23), (8, -29), (10, -22)], LARANJA)
    poli([(3, -23), (3, -26), (4, -23)], ESCURO)
    poli([(7, -23), (8, -27), (9, -23)], ESCURO)
    ponto(13, -18, ESCURO)                                                                                     # nariz
    ponto(14, -18, ESCURO)
    ponto(9, -20, LARANJA if piscando else ESCURO)                                                             # olho

    # Luz da lua vermelha batendo do lado direito da raposa
    px = camada.load()
    for y in range(ALTURA):
        for x in range(LARGURA - 1):
            if px[x, y][3] and not px[x + 1, y][3] and px[x, y][:3] in (LARANJA, LARANJA_ESC, BRANCO):
                px[x, y] = BORDA_LUZ + (255,)
    return camada


# ---------- Estrelas e vaga-lumes ----------
ESTRELAS = []
while len(ESTRELAS) < 38:
    x, y = random.randrange(LARGURA), random.randrange(26)
    if math.hypot(x - LUA_X, y - LUA_Y) > LUA_R + 6:
        ESTRELAS.append((x, y, random.randrange(6)))
VAGALUMES = [(10, 33, 0.0), (36, 40, 2.1), (16, 28, 4.2), (30, 44, 1.0)]


def quadro(n, piscando):
    img = montar_cenario()
    px = img.load()
    for x, y, fase in ESTRELAS:                                  # estrelas piscando
        px[x, y] = ESTRELA if (n + fase) % 6 < 4 else ESTRELA_FRACA
    img = img.convert("RGBA")
    img.alpha_composite(montar_raposa(piscando))
    px = img.load()
    for x, y, fase in VAGALUMES:                                 # vaga-lumes flutuando
        vx = round(x + 2 * math.sin(n * 0.5 + fase))
        vy = round(y + 1.5 * math.cos(n * 0.4 + fase))
        if 0 <= vx < LARGURA and 0 <= vy < ALTURA and math.sin(n * 0.8 + fase) > -0.3:
            px[vx, vy] = VAGALUME + (255,)
    return img.convert("RGB").resize((LARGURA * ZOOM, ALTURA * ZOOM), Image.NEAREST)


if __name__ == "__main__":
    quadros = [quadro(n, piscando=(n == 9)) for n in range(12)]
    quadros[0].save("raposa_lua_vermelha.png")
    quadros[0].save("raposa_lua_vermelha.gif", save_all=True, append_images=quadros[1:],
                    duration=170, loop=0)
    print("Pronto: raposa_lua_vermelha.png e raposa_lua_vermelha.gif")