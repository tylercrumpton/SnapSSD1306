from PIL import Image
import argparse

class CharacterImageHandler(object):
    def __init__(self, filename):
        self.im = Image.open(filename)
    def check_image_size(self):
        """Checks if image is 8x8 pixels."""
        return self.im.size == (8,8)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a single character image to a font image for the SSD1306.')
    parser.add_argument('image', help='image filename')
    args = parser.parse_args()

    cih = CharacterImageHandler(args.image)
