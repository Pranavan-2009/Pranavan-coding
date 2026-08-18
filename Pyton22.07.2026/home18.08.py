import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mundala")


board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(90):
    board.color(colors[i%len(colors)])
    board.width(2)
    board.forward(200)
    board.left(91)
    board.right(91)
    board.left(91)
    board.left(91)
    board.right(91)
    board.left(91)
    board.left(91)
    board.right(91)

turtle.done()