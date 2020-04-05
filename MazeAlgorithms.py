from PIL import Image

class DepthFirstSolve:
    image = None
    def __init__(self, image):
        self.image = image
        for col in range(self.image.size[0]):
            for row in range(self.image.size[1]):
                
                print (self.image.getpixel((row, col)))
