from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_DISTANCE = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for position in STARTING_DISTANCE:
            self.add_snake(position)

    def extend(self):
        self.add_snake(self.all_snakes[-1].position())

    def add_snake(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_snakes.append(snake)

    def move(self):
        for idx in range(len(self.all_snakes) - 1, 0, -1):
            a = self.all_snakes[idx - 1].xcor()
            b = self.all_snakes[idx - 1].ycor()
            self.all_snakes[idx].goto(x=a, y=b)
        self.all_snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.all_snakes[0].heading() != 270:
            self.all_snakes[0].setheading(90)

    def down(self):
        if self.all_snakes[0].heading() != 90:
            self.all_snakes[0].setheading(270)

    def right(self):
        if self.all_snakes[0].heading() != 180:
            self.all_snakes[0].setheading(0)

    def left(self):
        if self.all_snakes[0].heading() != 0:
            self.all_snakes[0].setheading(180)
