from PIL import Image
import argparse
from binascii import hexlify

class CharacterImageHandler(object):
    def __init__(self, filename):
        self.im = Image.open(filename)
    def check_image_size(self):
        """Checks if image is 8x8 pixels."""
        return self.im.size == (8,8)
    def eval_pixel(self, pixel):
        """Returns True if pixel is evaluated as 'black'."""
        if self.im.mode == "1":
            is_black = pixel < 128
        elif self.im.mode == "RGB":
            rgb_sum = pixel[0] + pixel[1] + pixel[2]
            is_black = rgb_sum < 382
        else:
            raise ValueError
        return is_black
    def get_bytes(self):
        """Returns a list of bytes based on the image contents."""
        if not self.check_image_size():
            raise ValueError
        bytelist = []
        for x in range(0, 8, 1):
            byte = 0
            for y in range(7, -1, -1):
                bitvalue = self.eval_pixel(self.im.getpixel((x,y)))
                byte = (byte << 1) + bitvalue
            bytelist.append(byte)
        return bytelist
    def get_font_string(self):
        """Returns the formatted font string for the image."""
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
