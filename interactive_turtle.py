#Exercício 1

import turtle

wn = turtle.Screen()

wn.title("Control Tess")
wn.bgcolor("lightgreen")
wn.setup(width = 600, height = 600)

tess = turtle.Turtle()

def change_color (color):
    tess.fillcolor(color)
    tess.pencolor(color)

def increment_pen_size (inc):
    pensize = tess.pensize()

    if 1 <= pensize + inc <= 20:
        tess.pensize(pensize + inc)

spd = 0
ang_spd = 0
def increment_speed (inc):
    global spd
    spd += inc

def increment_ang_speed (inc):
    global ang_spd
    ang_spd += inc

def update():
    if spd != 0:
        tess.forward(spd)
    if ang_spd != 0:
        tess.left(ang_spd)
    wn.ontimer(update,20)

wn.ontimer(update,20)

wn.onkey(lambda : change_color('red'), 'r')
wn.onkey(lambda : change_color('green'), 'g')
wn.onkey(lambda : change_color('blue'), 'b')

wn.onkey(lambda : increment_pen_size(+1), 'plus')
wn.onkey(lambda : increment_pen_size(-1), 'minus')

wn.onkeypress  (lambda : increment_speed(+10), 'Up')
wn.onkeyrelease(lambda : increment_speed(-10), 'Up')

wn.onkeypress  (lambda : increment_speed(-10), 'Down')
wn.onkeyrelease(lambda : increment_speed(+10), 'Down')

wn.onkeypress  (lambda : increment_ang_speed(-5), 'Right')
wn.onkeyrelease(lambda : increment_ang_speed(+5), 'Right')

wn.onkeypress  (lambda : increment_ang_speed(+5), 'Left')
wn.onkeyrelease(lambda : increment_ang_speed(-5), 'Left')

wn.listen()
wn.mainloop()
