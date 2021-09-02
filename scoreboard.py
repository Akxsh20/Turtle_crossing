from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.penup()
            self.hideturtle()
            self.goto(-200, 250)
            self.score = 0
            self.color("black")
            self.update()

        def update(self):
            self.write(f"Level: {self.score}", align='center', font=('Courier', 25, 'normal'))

        def game(self):
            self.goto(0, 0)
            self.write("GAME OVER!!", align='center', font=('Courier', 25, 'normal'))

        def current_score(self):
            self.score += 1
            self.clear()
            self.update()
            self.hideturtle()
            self.goto(0, 270)
