import time
from turtle import Screen
from modules.player import Player
from modules.car_manager import CarManager
from modules.scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)  # Turns off animation

# Create player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for player input (Up arrow key and 'w' key)
screen.listen()
screen.onkey(player.move, 'Up')  # When 'Up' key is pressed, call player.move()
screen.onkey(player.move, 'w')   # When 'w' key is pressed, call player.move()

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Pause for a short time
    screen.update()  # Update the screen

    # Create cars and move them
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collision with player and cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:  # Check if player is within 20 pixels of a car
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display game over message

    # Check if player reached the top of the screen
    if player.ycor() > 280:  # If player's y-coordinate is greater than 280 (top of the screen)
        player.reset()  # Reset player position
        car_manager.increase_speed()  # Increase speed of cars
        scoreboard.increase_level()  # Increase game level

# Exit the game when the screen is clicked
screen.exitonclick()
