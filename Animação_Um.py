
import turtle

tela = turtle.Screen()
tela.title("Minha primeira animação")
tela.bgcolor("black")

estrela = turtle.Turtle()
estrela.shape("turtle")
estrela.color("purple")
estrela.speed(3)

for i in range(36):
    estrela.forward(100)
    estrela.right(170)

turtle.done()
