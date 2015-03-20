[![Build Status](https://travis-ci.org/tylercrumpton/SnapSSD1306.svg?branch=master)](https://travis-ci.org/tylercrumpton/SnapSSD1306)
# SnapSSD1306
Framework for displaying images and text on an SSD1306 OLED display with a Synapse SNAP module.

## fonthelp
The fonthelper utilities are designed to help make creating fonts a little easier. To install the dependencies use pip:

    pip install -r test-requirements
    
Run the unit tests to make sure everything is good to go:

    nosetests
    
Then, you can run the singlechar.py tool on 8x8 pixel monoschromatic bitmap images:

    python singlechar.py letter.bmp
