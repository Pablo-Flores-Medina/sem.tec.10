import turtle
from turtle import *
from turtle import Screen
from freegames import vector

def emptySquare():
    pass  # TODO

def filledSquare():
  pass  # TODO

def filledCircle():
    t = turtle.Turtle()
    t.fillcolor('red')  # set the fillcolor
    t.begin_fill()  # start the filling color 
    t.circle(100)
    t.end_fill()


while True:
    screen = Screen()
    answer = screen.textinput("Next Game","1 - Square:")
    if (answer is None):
        break
    elif (answer == '1'):
        emptySquare()
    elif (answer == '2'):
        filledSquare()
