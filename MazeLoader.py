from PIL import Image

class Maze:
    image = None
    def __init__(self, imageloc):
        self.image = Image.open(imageloc)
        self.outpit = Image.new("1", self.image.size, 0xffffff)
        
