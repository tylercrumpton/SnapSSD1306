"""Framework for displaying graphics on a 128x64 OLED screen powered by the SSD1306 chip."""

SSD1306_ADDRESS     = 0x78

SELECT_CONTROL_BYTE = 0x80
SELECT_DATA_BYTE    = 0x40

# Fundamental commands:
def set_contrast(level):
    """Sets the contrast  of the display.

    The display has 256 contrast steps from 0x00 to 0xFF. The segment output current increases 
    as the contrast step value increases.
    """
    send_command(0x81)
    send_command(level)
# Scrolling commands:

# Addressing-setting commands:

# Hardware-configuration commands:

# Timing and driving scheme setting commands:


def init_display():
    # Init i2c with no pullups (they're external):
    i2cInit(False)

def send_command(command):
    """Sends a command byte to the display controller."""
    cmd = ""
    cmd += chr( SSD1306_ADDRESS )
    cmd += chr( SELECT_CONTROL_BYTE )
    cmd += chr( command )
    i2cWrite(cmd, 10, False)

def send_data(data_string):
    """Sends a data string to the display's GDDRAM"""
    cmd = ""
    cmd += chr( SSD1306_ADDRESS )
    cmd += chr( SELECT_DATA_BYTE )
    cmd += data
    i2cWrite(cmd, 10, False)
    