from turtle import Turtle

# 5. Create a scoreboard

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()
    
    def add_point(self, player):
        if (player == 1):
            self.p1_score += 1
        if (player == 2):
            self.p2_score += 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.p1_score} | {self.p2_score}", True, align="Center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align="Center", font=("Arial", 24, "normal"))
        
    def p1_scored(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_scored(self):
        self.p2_score += 1
        self.update_scoreboard()
