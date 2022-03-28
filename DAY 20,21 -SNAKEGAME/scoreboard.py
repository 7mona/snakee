import turtle
Alignment = "center"
Font = ("Courier",20,"normal")

class Scoreboard(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score = {self.score}",align=Alignment,font=Font)
        self.hideturtle()
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}",align=Alignment,font=Font)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GaMe_OvEr",align=Alignment,font=Font)
    
    def reset(self):
         if self.score > self.high_score:
             self.high_score = self.score