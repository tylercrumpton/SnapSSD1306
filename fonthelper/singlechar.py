from PIL import Image
import argparse
from binascii import hexlify

class CharacterImageHandler(object):
    def __init__(self, filename):
        self.im = Image.open(filename)
    def check_image_size(self):
        """Checks if image is 8x8 pixels."""
        return self.im.size == (8,8)
    def get_bytes(self):
        if not self.check_image_size():
            raise ValueError
        bytelist = []
        for x in range(0, 8, 1):
            byte = 0
            for y in range(7, -1, -1):
                bitvalue = self.im.getpixel((x,y)) < 128
                byte = (byte << 1) + bitvalue
            bytelist.append(byte)
        return bytelist
    def get_font_string(self):
        bytelist = self.get_bytes()
        font_string = ""
        for i in range(0, 8):
            hexbyte = "\\x%0.2X" % bytelist[i]
            font_string += hexbyte
        return font_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a single character image to a font image for the SSD1306.')
    parser.add_argument('image', help='image filename')
    args = parser.parse_args()

    cih = CharacterImageHandler(args.image)
    print cih.get_font_string()
