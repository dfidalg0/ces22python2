# Exercício 2

import turtle

# Tess becomes a traffic light.

wn = turtle.Screen()

wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
wn.setup(width = 600, height = 600)

tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0
state_map = ['green','orange','red']

def set_state(new_state_num):
    global state_num, state_map
    state_diff = new_state_num - state_num
    advance = state_diff * 70

    state_num = new_state_num

    tess.fillcolor(state_map[state_num])
    tess.forward(advance)

def advance_state_machine():
    set_state((state_num + 1)%3)
    turtle.ontimer(advance_state_machine, 500)

turtle.ontimer(advance_state_machine,500)

wn.listen()
wn.mainloop()
