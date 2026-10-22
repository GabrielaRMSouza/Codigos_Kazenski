#Espiral Arco-Íris
import turtle

tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Espiral Arco-Íris")

desenho = turtle.Turtle()
desenho.speed(0)
desenho.pensize(2)

cores = ["red", "orange", "yellow",
         "lime", "cyan", "purple"]

for i in range(180):
    desenho.pencolor(cores[i % 6])
    desenho.forward(i * 1.2)
    desenho.right(59)

turtle.done()
