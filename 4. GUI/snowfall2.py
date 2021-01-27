# Import required modules
import random
import math
import arcade

# Adjust window attributes
Width = 800
Height = 600
Title = "SnowFall"


class snow_fall:
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_snow(self):
        # Reset flake to random position above screen
        self.y = random.randrange(Height, Height + 100)
        self.x = random.randrange(Width)


class snowfall(arcade.Window):
    def __init__(self, width, height, title):

        # Calls "__init__" of parent class
        # (arcade.Window) to setup screen
        super().__init__(width, height, title)

    def start_snowfall(self):

        # Set up snowfall and initialize variables.
        self.snowfall_list = []

        for i in range(50):
            # Create snowfall instance
            snowfall = snow_fall()

            # Randomly position snowfall
            snowfall.x = random.randrange(Width)
            snowfall.y = random.randrange(Height + 200)

            # Set other variables for the snowfall
            snowfall.size = random.randrange(8)
            snowfall.speed = random.randrange(20, 40)
            snowfall.angle = random.uniform(math.pi, math.pi * 2)

            # Add snowflake to snowfall list
            self.snowfall_list.append(snowfall)

        # Set the background color
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):

        # This command is necessary before drawing
        arcade.start_render()

        # Draw the current position of each snowfall
        for snowfall in self.snowfall_list:
            arcade.draw_circle_filled(snowfall.x, snowfall.y,
                                      snowfall.size, arcade.color.WHITE)

    def on_update(self, delta_time):

        # Animate all the snowfall falling
        for snowfall in self.snowfall_list:
            snowfall.y -= snowfall.speed * delta_time

            # Check if snowfall has fallen below screen
            if snowfall.y < 0:
                snowfall.reset_snow()

            # Some math to make the snowfall move side to side
            snowfall.x += snowfall.speed * \
                          math.cos(snowfall.angle) * delta_time
            snowfall.angle += 1 * delta_time

        # Driver Code


if __name__ == "__main__":
    screen = snowfall(800, 600, "Snow")
    screen.start_snowfall()
    arcade.run()
