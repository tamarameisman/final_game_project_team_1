import arcade
from game import constants
from game.director import Director
# from game.player import Player


class TeamGame(arcade.Window):
    """ This will be the main application class """
    
    def __init__(self):
        # call the parent class and setup a window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        #initialize lists
        #these are list to keep track of sprites
        self.platform_list = None
        self.player_list = None

        #a separate variable for the player sprite
        self.player_sprite = None
        
        arcade.set_background_color(arcade.csscolor.AQUAMARINE)

    def setup(self): # this looks like it should be separated out into a class

        # this is where we'll start the game?
        self.player_list = arcade.SpriteList()
        self.platform_list = arcade.SpriteList(use_spatial_hash=True)

        # setup the player at specific coordinates
        image_source = ":resources:images/animated_characters/zombie/zombie_idle.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = 60
        self.player_sprite.center_y = 80
        self.player_list.append(self.player_sprite)

        # create the ground
        # this places multiple sprites horizontally
        for x in range(0, constants.SCREEN_WIDTH, 80):
            platform = arcade.Sprite(":resources:images/tiles/stoneMid.png", constants.TILE_SCALING)
            platform.center_x = x
            platform.center_y = 20
            self.platform_list.append(platform)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            platform = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", constants.TILE_SCALING
            )
            platform.position = coordinate
            self.platform_list.append(platform)

    def on_draw(self): # this looks like it should be separated out into a class
        """ Render the screen """
        
        arcade.start_render()

        # code for drawing the screen will be placed here
        self.platform_list.draw()
        self.player_list.draw()

def main():
        """ Main Function """
        window = TeamGame()
        window.setup()
        arcade.run()

if __name__ == "__main__":
    main()



