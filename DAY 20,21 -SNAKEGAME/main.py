import turtle,snake,time,food,scoreboard

screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("navyblue")
screen.title("mona's snake ladder")
screen = turtle.Screen()    
screen.tracer(0)

snak = snake.Snake()

foods = food.Food()

score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snak.up,"Up")
screen.onkey(snak.down,"Down")
screen.onkey(snak.right,"Right")
screen.onkey(snak.left,"Left")

run = True
while run:
    screen.update()
    time.sleep(0.2)
    snak.move()
    if snak.head.distance(foods) < 15:
        foods.refresh()
        score.update_score()
        snak.extend()
        print("yeah you catched it ")    
    
    if snak.head.xcor()>280 or snak.head.xcor()<-280 or snak.head.ycor()>280 or  snak.head.ycor()<-280  :
        run = False
        score.game_over()
        
    for scale in snak.scales[1:]:
        if snak.head.distance(scale) < 15:
            run = False
            score.game_over()
screen.exitonclick()