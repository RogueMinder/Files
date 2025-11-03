import turtle
import time
import numpy as np

#screen_setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Analog Clock - Fixed")
screen.setup(500, 500)
screen.tracer(0)

face_turtle = turtle.Turtle()
face_turtle.speed(0)
face_turtle.hideturtle()

hands_turtle = turtle.Turtle()
hands_turtle.speed(0)
hands_turtle.hideturtle()


def draw_clock_face(t):

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.color("white")
    t.pensize(3)
    t.circle(205)

    t.penup()
    for i in range(1, 13):
        angle = i * 30
        x = 160 * np.sin(np.radians(angle))
        y = 160 * np.cos(np.radians(angle))
        t.goto(x, y)
        t.write(str(i), align="center", font=("Arial", 30, "bold"))


def draw_hand(t, angle, length, width, color):

    t.penup()
    t.goto(0, 0)
    t.setheading(90 - angle)
    t.pendown()
    t.color(color)
    t.pensize(width)
    t.forward(length)


def update_clock():

    hands_turtle.clear()
    ctime = time.localtime()
    hours = ctime.tm_hour
    minutes = ctime.tm_min
    seconds = ctime.tm_sec

    second_angle = seconds * 6
    minute_angle = minutes * 6 + seconds * 0.1
    hour_angle = (hours % 12) * 30 + minutes * 0.5

    draw_hand(hands_turtle, hour_angle, 80, 6, 'blue')
    draw_hand(hands_turtle, minute_angle, 120, 4, 'green')
    draw_hand(hands_turtle, second_angle, 150, 2, 'red')
    hands_turtle.penup()
    hands_turtle.goto(0, 0)
    hands_turtle.dot(10, 'white')

    screen.update()
    screen.ontimer(update_clock, 1000)


#mainprogram
draw_clock_face(face_turtle)
update_clock()

screen.exitonclick()