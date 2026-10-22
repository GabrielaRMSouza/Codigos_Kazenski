import tkinter as tk
import math
import random
import time

# ============================================================
# FOX.exe — Cyber Fox
# Raposa tecnológica que acompanha o cursor.
# Requer apenas Python e Tkinter.
# ============================================================

FUNDO = "#080711"
GRADE = "#151226"
ROXO = "#b9a0ff"
LILAS = "#e9e0ff"
ROXO_MEDIO = "#8e78d4"
CIANO = "#7cecff"
BRANCO = "#f8f5ff"
ROSA = "#e6a6ff"

FPS_MS = 16
ESPACAMENTO = 7.0
TOTAL_PONTOS = 390

janela = tk.Tk()
janela.title("FOX.exe | Cyber Fox")
janela.geometry("1000x700")
janela.minsize(620, 460)
janela.configure(bg=FUNDO)

tela = tk.Canvas(janela, bg=FUNDO, highlightthickness=0, bd=0)
tela.pack(fill="both", expand=True)

largura, altura = 1000, 700
mouse_x, mouse_y = largura / 2, altura / 2
cabeca_x, cabeca_y = mouse_x, mouse_y
angulo = 0.0
tempo_animacao = 0.0
ultimo_tempo = time.perf_counter()
ultimo_mouse = (mouse_x, mouse_y)
velocidade_cursor = 0.0
rastro = []
particulas = []
estrelas = []
ultimo_redesenho_fundo = None


def transformar(x, y, ox, oy, rotacao):
    c, s = math.cos(rotacao), math.sin(rotacao)
    return ox + x * c - y * s, oy + x * s + y * c


def achatar(pontos):
    return [valor for ponto in pontos for valor in ponto]


def linha(pontos, cor, largura_linha=2, tag="raposa", suave=True):
    if len(pontos) < 2:
        return
    tela.create_line(
        *achatar(pontos),
        fill=cor,
        width=largura_linha,
        smooth=suave,
        splinesteps=12,
        capstyle=tk.ROUND,
        joinstyle=tk.ROUND,
        tags=tag
    )


def circulo(x, y, raio, preenchimento, contorno="", largura_contorno=1, tag="raposa"):
    tela.create_oval(
        x-raio, y-raio, x+raio, y+raio,
        fill=preenchimento,
        outline=contorno,
        width=largura_contorno,
        tags=tag
    )


def criar_estrelas():
    global estrelas
    estrelas = []
    for _ in range(max(55, int(largura * altura / 8500))):
        estrelas.append((
            random.uniform(0, largura),
            random.uniform(0, altura),
            random.choice((1, 1, 1, 2)),
            random.uniform(0, math.tau)
        ))


def desenhar_fundo():
    tela.delete("fundo")
    passo = 48
    for x in range(0, largura + passo, passo):
        tela.create_line(x, 0, x, altura, fill=GRADE, width=1, tags="fundo")
    for y in range(0, altura + passo, passo):
        tela.create_line(0, y, largura, y, fill=GRADE, width=1, tags="fundo")

    for x, y, raio, fase in estrelas:
        tela.create_oval(
            x-raio, y-raio, x+raio, y+raio,
            fill="#403652", outline="", tags="fundo"
        )

    # Cantos da interface
    margem, tamanho = 20, 25
    cantos = [
        (margem, margem, 1, 1),
        (largura-margem, margem, -1, 1),
        (margem, altura-margem, 1, -1),
        (largura-margem, altura-margem, -1, -1),
    ]
    for x, y, sx, sy in cantos:
        tela.create_line(x, y, x+sx*tamanho, y, fill="#655484", width=2, tags="fundo")
        tela.create_line(x, y, x, y+sy*tamanho, fill="#655484", width=2, tags="fundo")


def ao_mover(event):
    global mouse_x, mouse_y
    mouse_x, mouse_y = event.x, event.y


def ao_redimensionar(event):
    global largura, altura
    if event.widget is not tela:
        return
    nova_largura, nova_altura = max(1, event.width), max(1, event.height)
    if (nova_largura, nova_altura) != (largura, altura):
        largura, altura = nova_largura, nova_altura
        criar_estrelas()
        desenhar_fundo()


tela.bind("<Motion>", ao_mover)
tela.bind("<Configure>", ao_redimensionar)


def atualizar_movimento(dt):
    global cabeca_x, cabeca_y, angulo

    dx = mouse_x - cabeca_x
    dy = mouse_y - cabeca_y
    suavizacao = 1.0 - math.exp(-11.0 * dt)
    cabeca_x += dx * suavizacao
    cabeca_y += dy * suavizacao

    if math.hypot(dx, dy) > 1.0:
        alvo = math.atan2(dy, dx)
        diferenca = (alvo - angulo + math.pi) % math.tau - math.pi
        angulo += diferenca * (1.0 - math.exp(-10.0 * dt))

    if not rastro:
        rastro.extend(
            (cabeca_x - i * ESPACAMENTO, cabeca_y)
            for i in range(TOTAL_PONTOS)
        )
    else:
        rastro[0] = (cabeca_x, cabeca_y)
        for i in range(1, len(rastro)):
            px, py = rastro[i-1]
            x, y = rastro[i]
            dx, dy = x-px, y-py
            distancia = math.hypot(dx, dy)
            if distancia > 0.0001:
                rastro[i] = (
                    px + dx / distancia * ESPACAMENTO,
                    py + dy / distancia * ESPACAMENTO
                )
            else:
                rastro[i] = (px-ESPACAMENTO, py)


def desenhar_corpo():
    # Cauda com três camadas para um brilho neon discreto.
    cauda = rastro[205:385:3]
    if len(cauda) > 2:
        linha(cauda, "#35234e", 8)
        linha(cauda, "#7d5ab9", 4)
        linha(cauda, ROXO, 2)
        linha(cauda, LILAS, 1)
        tx, ty = cauda[-1]
        circulo(tx, ty, 6, "", ROXO, 2)
        circulo(tx, ty, 2, CIANO)

    # Segmentos do corpo: o tronco é mais largo perto da cabeça.
    corpo = rastro[9:205:2]
    for i, (x, y) in enumerate(corpo):
        indice = 9 + i * 2
        tamanho = max(1.4, 5.2 - indice * 0.018)
        cor = ("#71658f", "#9a8bc4", "#c7baff", "#8274ac")[(i // 3) % 4]
        if i < len(corpo)-1:
            x2, y2 = corpo[i+1]
            tela.create_line(
                x, y, x2, y2, fill=cor, width=tamanho,
                capstyle=tk.ROUND, tags="raposa"
            )
        if i % 3 == 0:
            circulo(x, y, max(1.1, tamanho * 0.42), CIANO if i % 2 == 0 else LILAS)

    # Espinhos pequenos, acompanhando a direção local do corpo.
    for i in range(20, 145, 12):
        x, y = rastro[i]
        ax, ay = rastro[i-2]
        bx, by = rastro[i+2]
        direcao = math.atan2(by-ay, bx-ax)
        nx, ny = -math.sin(direcao), math.cos(direcao)
        tamanho = 5.5 if i < 65 else 3.5
        for lado in (-1, 1):
            linha([(x, y), (x+nx*tamanho*lado, y+ny*tamanho*lado)],
                  "#9d8bce", 1.2, suave=False)

    # Patas articuladas em pares. O movimento alternado dá vida ao corpo.
    for i in range(18, 102, 12):
        x, y = rastro[i]
        ax, ay = rastro[i-2]
        bx, by = rastro[i+2]
        direcao = math.atan2(by-ay, bx-ax)
        nx, ny = -math.sin(direcao), math.cos(direcao)
        balanço = math.sin(tempo_animacao * 8 + i * 0.55) * 3.0
        comprimento = 13 if i < 55 else 10

        for lado in (-1, 1):
            base = (x + nx * lado * 2, y + ny * lado * 2)
            ang1 = direcao + lado * 1.08
            joelho = (
                x + math.cos(ang1)*comprimento + nx*lado*balanço,
                y + math.sin(ang1)*comprimento + ny*lado*balanço
            )
            ang2 = direcao + lado * 1.55
            ponta = (
                joelho[0] + math.cos(ang2)*comprimento*0.72,
                joelho[1] + math.sin(ang2)*comprimento*0.72
            )
            linha([base, joelho, ponta], "#aaa0d3", 1.5, suave=False)
            circulo(joelho[0], joelho[1], 1.7, CIANO)


def desenhar_cabeca():
    hx, hy = cabeca_x, cabeca_y

    def p(x, y):
        return transformar(x, y, hx, hy, angulo)

    # Halo de energia atrás da cabeça.
    pulso = 1.5 + (math.sin(tempo_animacao * 3.5) + 1) * 0.8
    tela.create_oval(
        hx-27-pulso, hy-27-pulso, hx+27+pulso, hy+27+pulso,
        outline="#3c2d5b", width=2, tags="raposa"
    )
    tela.create_oval(
        hx-23, hy-23, hx+23, hy+23,
        outline="#6b5698", width=1, tags="raposa"
    )

    # Orelhas com interior colorido.
    orelha_esq = [p(-13, -8), p(-24, -37), p(-2, -20)]
    interior_esq = [p(-13, -13), p(-19, -29), p(-7, -21)]
    orelha_dir = [p(5, -13), p(13, -40), p(24, -10)]
    interior_dir = [p(9, -16), p(13, -31), p(19, -14)]

    for externo, interno in (
        (orelha_esq, interior_esq),
        (orelha_dir, interior_dir)
    ):
        tela.create_polygon(
            *achatar(externo), fill="#171322",
            outline=LILAS, width=2, tags="raposa"
        )
        tela.create_polygon(
            *achatar(interno), fill="#9a6cbb",
            outline="", tags="raposa"
        )

    # Silhueta facial mais angulosa, para lembrar uma raposa.
    rosto = [
        p(-19, -8), p(-13, -16), p(0, -19), p(13, -13),
        p(21, -5), p(20, 5), p(12, 13), p(-2, 16),
        p(-15, 10), p(-20, 2)
    ]
    tela.create_polygon(
        *achatar(rosto), fill="#0b0a14",
        outline=BRANCO, width=2, smooth=True, tags="raposa"
    )

    # Placa frontal e trilha de circuito.
    placa = [p(-8, -13), p(4, -15), p(12, -8), p(1, -5)]
    tela.create_polygon(
        *achatar(placa), fill="#635087",
        outline=ROXO, width=1, tags="raposa"
    )
    linha([p(-14, 0), p(-8, 4), p(-10, 8)], CIANO, 1.2, suave=False)

    # Focinho comprido e pequeno nariz luminoso.
    focinho = [p(9, -7), p(31, 0), p(9, 7), p(2, 0)]
    tela.create_polygon(
        *achatar(focinho), fill="#171322",
        outline=LILAS, width=1.7, tags="raposa"
    )
    nx, ny = p(31, 0)
    circulo(nx, ny, 2.4, CIANO)

    # Olhos luminosos com contorno.
    for ex, ey in [(-3, -7), (8, -7)]:
        x, y = p(ex, ey)
        circulo(x, y, 4.2, "#33264d", ROXO, 1)
        circulo(x, y, 2.0, CIANO)
        circulo(x-0.6, y-0.7, 0.7, BRANCO)

    # Pequenos traços de bigode/circuito.
    for lado in (-1, 1):
        linha([p(8, lado*5), p(16, lado*10), p(22, lado*9)],
              "#9c8bc7", 1, suave=False)


def criar_particula(x, y):
    particulas.append({
        "x": x,
        "y": y,
        "vx": random.uniform(-24, 24),
        "vy": random.uniform(-24, 24),
        "vida": random.uniform(0.3, 0.8),
        "vida_max": 0.8,
        "raio": random.uniform(1.0, 2.6),
        "cor": random.choice((ROXO, CIANO, LILAS, ROSA))
    })


def atualizar_e_desenhar_particulas(dt):
    for particula in particulas[:]:
        particula["vida"] -= dt
        if particula["vida"] <= 0:
            particulas.remove(particula)
            continue

        particula["x"] += particula["vx"] * dt
        particula["y"] += particula["vy"] * dt
        proporcao = particula["vida"] / particula["vida_max"]
        raio = max(0.5, particula["raio"] * proporcao)
        circulo(particula["x"], particula["y"], raio, particula["cor"])


def desenhar_interface():
    tela.create_text(
        30, 27, anchor="nw", text="FOX.exe",
        fill=LILAS, font=("Consolas", 17, "bold"), tags="hud"
    )
    tela.create_text(
        31, 51, anchor="nw",
        text="CYBER COMPANION  /  TRACKING ACTIVE",
        fill="#82769f", font=("Consolas", 9), tags="hud"
    )

    pulsar = 3 + (math.sin(tempo_animacao * 4) + 1) * 1.2
    circulo(largura-30, 30, pulsar, CIANO, tag="hud")
    tela.create_text(
        largura-44, 30, anchor="e", text="ONLINE",
        fill="#aaa0c8", font=("Consolas", 9), tags="hud"
    )
    tela.create_text(
        30, altura-28, anchor="sw",
        text=f"X {int(mouse_x):04d}   Y {int(mouse_y):04d}",
        fill="#82769f", font=("Consolas", 10), tags="hud"
    )
    tela.create_text(
        largura-30, altura-28, anchor="se",
        text="MOVE YOUR CURSOR",
        fill="#655681", font=("Consolas", 9), tags="hud"
    )


def animar():
    global tempo_animacao, ultimo_tempo, velocidade_cursor, ultimo_mouse

    agora = time.perf_counter()
    dt = min(0.05, max(0.001, agora - ultimo_tempo))
    ultimo_tempo = agora
    tempo_animacao += dt

    velocidade_cursor = math.hypot(
        mouse_x - ultimo_mouse[0], mouse_y - ultimo_mouse[1]
    )
    ultimo_mouse = (mouse_x, mouse_y)

    atualizar_movimento(dt)

    # Cria um rastro de partículas quando o cursor está em movimento.
    if velocidade_cursor > 2 and random.random() < 0.25:
        criar_particula(
            cabeca_x - math.cos(angulo) * 12,
            cabeca_y - math.sin(angulo) * 12
        )

    tela.delete("raposa")
    tela.delete("hud")

    atualizar_e_desenhar_particulas(dt)
    desenhar_corpo()
    desenhar_cabeca()
    desenhar_interface()

    janela.after(FPS_MS, animar)


criar_estrelas()
desenhar_fundo()
animar()
janela.mainloop()
