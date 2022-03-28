import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
   
    def __init__(self):
        '''to create the snake'''
        self.scales = []
        self.create_snake()
        self.head = self.scales[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_scale(position)
            
    def add_scale(self,position):
        snake = turtle.Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.scales.append(snake)
    
    def extend(self):
        self.add_scale(self.scales[-1].position())
           
    def move(self):
        '''used to move the snake'''
        for i in range (len(self.scales)-1,0,-1):
           self.scales[i].goto(self.scales[i-1].pos())
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)   
      
    def down(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)
            
    def left(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(180)           
            