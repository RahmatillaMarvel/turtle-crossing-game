from turtle import Turtle
import random

# List of colors that can be used for the cars
COLORS: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]

# The starting distance (in pixels) for which cars move in each step
STARTING_MOVE_DISTANCE: int = 5

# The amount by which the car speed increases when the level is incremented
MOVE_INCREMENT: int = 10



class CarManager:
    """A class to manage cars in the game."""

    def __init__(self) -> None:
        """Initialize the CarManager object with an empty list of cars."""
        self.all_cars: list[Turtle] = []

    def create_car(self) -> None:
        """
        Create a new car with a random chance.

        Randomly generates a new car with a square shape and random color,
        then adds it to the list of all cars.
        """
        random_chance: int = random.randint(1, 6)
        if random_chance == 1:
            new_car: Turtle = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y: int = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self) -> None:
        """Move all cars backwards."""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self) -> None:
        """Increase the speed of cars."""
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
