from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as f:
            self.highscore = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1

        self.clear()
        self.update_scoreboard()