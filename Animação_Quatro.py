#Bolinha saltitande estilo dvd
import turtle

tela = turtle.Screen()
tela.setup(600, 400)
tela.bgcolor("black")
tela.title("Bolinha Saltitante")
tela.tracer(0)

bola = turtle.Turtle()
bola.shape("circle")
bola.color("violet")
bola.penup()
bola.goto(0, 0)

dx = 4
dy = 3

def animar():
    global dx, dy

    x = bola.xcor() + dx
    y = bola.ycor() + dy

    if x > 285 or x < -285:
        dx = -dx

    if y > 185 or y < -185:
        dy = -dy

    bola.goto(x, y)
    tela.update()
    tela.ontimer(animar, 16)

animar()
turtle.done()
