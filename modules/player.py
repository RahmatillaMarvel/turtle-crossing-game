from turtle import Turtle

# The starting position of the player turtle
STARTING_POSITION: tuple[int, int] = (0, -280)  
# The distance the player turtle moves in each step
MOVE_DISTANCE: int = 10  
# The y-coordinate where the player turtle reaches the finish line
FINISH_LINE_Y: int = 280  


class Player(Turtle):
    """A class representing the player turtle in the game."""
    
    def __init__(self) -> None:
        """
        Initialize a new player turtle object.
        
        Sets up the player turtle with green color, facing upwards (90 degrees), 
        and positions it at the starting position.
        """
        super().__init__(shape='turtle')
        self.color('green')
        self.setheading(90)
        self.penup()  
        self.goto(STARTING_POSITION)  
        
    def move(self) -> None:
        """
        Move the player turtle forward by the predefined move distance.
        """
        self.forward(distance=MOVE_DISTANCE)
    
    def reset(self) -> None:
        """
        Reset the position of the player turtle to the starting position.
        """
        self.goto(STARTING_POSITION)
