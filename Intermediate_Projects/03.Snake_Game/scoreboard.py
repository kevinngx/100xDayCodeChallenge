from turtle import Turtle

# 5. Create a scoreboard

class Scoreboard(Turtle):
    def __init__(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.update_scoreboard()
    
    def add_point(self):
        self.score += 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score} High Score: {self.high_score}",  True, align="Center", font=("Arial", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", True, align="Center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score    
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        