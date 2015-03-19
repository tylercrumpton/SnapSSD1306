#import pillow
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a single character image to a font image for the SSD1306.')
    parser.add_argument('image', help='image filename')
    args = parser.parse_args()
