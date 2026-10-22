
import tkinter as tk
import math

janela = tk.Tk()
janela.title("Para você ❤️")
janela.geometry("500x400")
janela.configure(bg="#241333")
janela.resizable(False, False)

tela = tk.Canvas(
    janela,
    width=500,
    height=400,
    bg="#241333",
    highlightthickness=0
)
tela.pack()

tempo = 0

def animar():
    global tempo
    tela.delete("all")
    tempo += 0.15

    # Tamanho do coração muda para criar o pulso
    escala = 1 + 0.12 * math.sin(tempo)
    tamanho = int(100 * escala)

    tela.create_text(
        250, 145,
        text="♥",
        fill="#ff5caa",
        font=("Arial", tamanho)
    )

    tela.create_text(
        250, 260,
        text="EU TE AMO!",
        fill="#ffffff",
        font=("Arial", 28, "bold")
    )

    tela.create_text(
        250, 305,
        text="♡ Com amor, Gabi :3 ♡",
        fill="#dcb8ff",
        font=("Arial", 14)
    )

    janela.after(30, animar)

animar()
janela.mainloop()
