FONT = ("Courier", 24, "normal")  # The font style for the scoreboard

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        """Initialize the scoreboard with starting level and font settings."""
        super().__init__(visible=False)
        self.level = 1 
        self.color('green')
        self.penup()
        self.goto(-280, 250)  
        self.update_scoreboard() 

    def update_scoreboard(self):
        """Update the scoreboard with the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level by 1 and update the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
