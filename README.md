[![Build Status](https://travis-ci.org/tylercrumpton/SnapSSD1306.svg?branch=master)](https://travis-ci.org/tylercrumpton/SnapSSD1306)
# SnapSSD1306
Framework for displaying images and text on an SSD1306 OLED display with a Synapse SNAP module.

## SSD1306.py
`SSD130.py` is the main driver for SSD1306-based i2c display boards. Use `init_display()` to set all of the default configurations that should work for most boards. Data can be written to the GFX RAM by using the `write_data()` function.

## font_8x8.py
`font_8x8.py` is a pre-built fixed-width fontface that can be used for displaying text on the display. It is based on the Joystix font by typodermicfonts. Custom characters can be added in the first 32 strings in the `font_8x8` tuple. Pixels are ordered bottom-to-top, left-to-right.

## fonthelp
The `fonthelper` utilities are designed to help make creating fonts a little easier. To install the dependencies use pip:

    pip install -r test-requirements

Run the unit tests to make sure everything is good to go:

    nosetests

Then, you can run the singlechar.py tool on 8x8 pixel bitmap images:

    python singlechar.py letter.bmp
