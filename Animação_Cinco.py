#Tunel cósmico doidão
import turtle

tela = turtle.Screen()
tela.bgcolor("#080812")
tela.title("Túnel Cósmico")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

cores = ["purple", "cyan", "magenta"]

for i in range(120):
    t.color(cores[i % 3])
    t.circle(i * 1.5, 90)
    t.left(91)

turtle.done()
