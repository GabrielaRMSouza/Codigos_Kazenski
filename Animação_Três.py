#Estrela Mágica branca
import turtle

tela = turtle.Screen()
tela.bgcolor("#171020")
tela.title("Estrela Mágica")

estrela = turtle.Turtle()
estrela.speed(0)
estrela.color("#C9A0FF")
estrela.pensize(2)

for i in range(36):
    for lado in range(5):
        estrela.forward(120)
        estrela.right(144)

    estrela.right(10)

turtle.done()
