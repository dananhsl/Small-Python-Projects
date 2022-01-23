from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Who will win the race?","Enter a color: ")
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = float(-100)
FONT = ("Courier", 18, "bold")


for new_turtle in range(0, 6):
    turtles.append(Turtle(shape="turtle"))
    turtles[new_turtle].penup()
    turtles[new_turtle].goto(x=-235, y=y_cord)
    turtles[new_turtle].color(colors[new_turtle])
    turtles[new_turtle].speed("fastest")
    y_cord += 40


def check_position():
    for item in turtles:
        if item.xcor() >= 235:
            if item.color()[0] == user_bet:
                score.win_score(item)
            else:
                score.lose_score(item)

            return False
    return True


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("black")
        self.penup()

    def win_score(self, item):
        self.write(f"You won! {item.color()[0].title()} won the race.", False, align="center", font=FONT)

    def lose_score(self, item):
        self.write(f"You lost. {item.color()[0].title()} won the race.", False, align="center", font=FONT)


score = Score()


while check_position():
    for item_2 in turtles:
        item_2.forward(random.randint(1, 20))


screen.exitonclick()
