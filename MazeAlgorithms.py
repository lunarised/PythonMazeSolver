from PIL import Image

class DepthFirstSolve:
    image = None
    def __init__(self, image):
        self.image = image
        for row in range(self.image.size[0]):
            for col in range(self.image.size[1]):
                print(row)
                print (self.image.getpixel((col, row)))
