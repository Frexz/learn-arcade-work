# Import arcade library
import arcade

# Open window
arcade.open_window(660, 480, "Norway\'s Flag")

# Set background color
arcade.set_background_color(arcade.csscolor.RED)

# Start drawing
arcade.start_render()

# Draw white rectangle, horizontal
arcade.draw_rectangle_filled(center_x=330,
                             center_y=240,
                             width=660,
                             height=120,
                             color=arcade.csscolor.WHITE)

# Draw white rectangle, vertical
arcade.draw_rectangle_filled(center_x=240,
                             center_y=240,
                             width=120,
                             height=480,
                             color=arcade.csscolor.WHITE)

# Draw blue rectangle, horizontal
arcade.draw_rectangle_filled(center_x=330,
                             center_y=240,
                             width=660,
                             height=60,
                             color=arcade.csscolor.DARK_BLUE)

# Draw blue rectangle, vertical
arcade.draw_rectangle_filled(center_x=240,
                             center_y=240,
                             width=60,
                             height=480,
                             color=arcade.csscolor.DARK_BLUE)



# Finish drawing
arcade.finish_render()

# Keep the window open
arcade.run()