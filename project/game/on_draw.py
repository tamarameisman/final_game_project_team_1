import arcade
from game import constants
from game.director import Director

class On_draw:
    
    def __init__(self):
        pass


    def on_draw(self):
            # Clear screen
            arcade.start_render()
            # camera
            self.camera.use()
            # Draw scene
            self.scene.draw()
    
    def output(self):
        pass
