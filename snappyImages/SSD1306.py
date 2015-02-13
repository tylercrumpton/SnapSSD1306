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

def set_entire_display_on(enable):
    """Sets the entire display to ON or resets back to GDDRAM values.

    If enable is True, every pixel will be lit.
    If enable is False, each pixel will be lit according to GDDRAM.
    """
    if enable:
        send_command(0xA5)
    else:
        send_command(0xA4)

def set_invert_display(enable):
    """Inverts or resets the display.

    If enable is True, the display will be inverted.
    If enable is False, the display will be restored to normal.
    """
    if enable:
        send_command(0xA7)
    else:
        send_command(0xA6)

def turn_display_off(turn_off):
    """Turns the entire display off or turns it back on to normal operation.

    If turn_off is True, the entire display will be turned off.
    If turn_off is False, the display will be turned back on.
    """
    if turn_off:
        send_command(0xAE)
    else:
        send_command(0xAF)

# Scrolling commands:
def start_horizontal_scroll(scroll_right, start_page, end_page, speed, top_fixed_rows, scroll_rows):
    """Scrolls the display horizontally.

    If scroll_right is True, the display will scroll to the right.
    If scroll_right is False, the display will scroll to the left.

    TODO: Figure out what the start and end pages actually do. Values may
    range from 0-7.

    The rate at which the display scrolls is determined by speed, where a
    lower value results in a slower speed. Value may range from 0-7.

    The vertical area that actually scrolls is defined as the scroll_row rows
    after the top_fixed_rows rows. For example:
           Scroll whole screen: top_fixed_rows=0, scroll_rows=64
                 Static header: top_fixed_rows=8, scroll_rows=48
      Static header and footer: top_fixed_rows=8, scroll_rows=40
                 Static footer: top_fixed_rows=0, scroll_rows=48
    """
    # First stop the display if it's already scrolling:
    stop_scroll()
    # Set the scroll direction:
    if scroll_right:
        send_command(0x26)
    else:
        send_command(0x27)
    # Dummy byte 0x00:
    send_command(0x00)
    # Set start page address:
    send_command(start_page)
    # Set scroll speed:
    send_command(_map_scroll_speed(speed))
    # Set end page address:
    send_command(end_page)
    # Dummy byte 0x00:
    send_command(0x00)
    # Dummy byte 0xFF:
    send_command(0xFF)
    # Set the vertical scroll area:
    _set_scroll_area(top_fixed_rows, scroll_rows)
    # Start scrolling:
    _start_scroll()

def start_dual_scroll(scroll_right, start_page, end_page, speed, vertical_offset, top_fixed_rows, scroll_rows):
    """Scrolls the display vertically and horizontally.

    If scroll_right is True, the display will scroll vertically and to the right.
    If scroll_right is False, the display will scroll vertically and to the left.

    TODO: Figure out what the start and end pages actually do. Values may
    range from 0-7.

    The rate at which the display scrolls is determined by speed, where a
    lower value results in a slower speed. Value may range from 0-7.

    The number of rows that are scrolled vertically per scroll step is defined by
    vertical_offset. Value may range from 0-63 rows.

    The vertical area that actually scrolls is defined as the scroll_row rows
    after the top_fixed_rows rows. For example:
           Scroll whole screen: top_fixed_rows=0, scroll_rows=64
                 Static header: top_fixed_rows=8, scroll_rows=48
      Static header and footer: top_fixed_rows=8, scroll_rows=40
                 Static footer: top_fixed_rows=0, scroll_rows=48
    """
    # First stop the display if it's already scrolling:
    stop_scroll()
    # Set the scroll direction:
    if scroll_right:
        send_command(0x29)
    else:
        send_command(0x2A)
    # Dummy byte 0x00:
    send_command(0x00)
    # Set start page address:
    send_command(start_page)
    # Set scroll speed:
    send_command(_map_scroll_speed(speed))
    # Set end page address:
    send_command(end_page)
    # Set vertical offset:
    send_command(vertical_offset)
    # Set the vertical scroll area:
    _set_scroll_area(top_fixed_rows, scroll_rows)
    # Start scrolling:
    _start_scroll()

def stop_scroll():
    """Stops the display from scrolling."""
    send_command(0x2E)

def _start_scroll():
    """Starts scrolling the display based on scrolling setup parameters"""
    send_command(0x2F)

def _map_scroll_speed(speed):
    """Maps a reasonable speed value between 0 and 7 to the weird SSD1306 value."""
    speed_map = (0b011, 0b010, 0b001, 0b110, 0b000, 0b101, 0b100, 0b111)
    return speed_map[speed]

def _set_scroll_area(top_fixed_rows, scroll_rows):
    send_command(0xA3)
    send_command(top_fixed_rows)
    send_command(scroll_rows)

# Addressing-setting commands:
def set_start_col_addr(address):
    """Sets the column starts address register for Page Addressing Mode."""
    low_nibble = address & 0x0F
    high_nibble = address >> 4
    send_command(low_nibble)
    send_command(high_nibble | 0x10)

# Hardware-configuration commands:
def set_display_start_line(line):
    """Sets the display RAMs start line register from 0-64."""
    send_command(0x40 | line)

# Timing and driving scheme setting commands:
def set_clock_divide_ratio_frequency(ratio, frequency)
    """Sets the display clock's divide ratio and oscillator frequency."""
    send_command(0xD5)
    send_command(frequency << 4 | ratio)

def _send_noop():
    """Sends a no-op to the display controller."""
    send_command(0xE3)

def init_display():
    # Init i2c with no pullups (they're external):
    i2cInit(False)
    # Turn off the display:
    turn_display_off(True)
    # Set the display clock frequency:
    set_clock_divide_ratio_frequency(0, 4)
    # Set multiplex:
    send_command(0xA8)
    send_command(0x3F)
    # Set display offset to zero:
    send_command(0xD3)
    send_command(0x00)
    # Set start line to zero
    set_display_start_line(0x0)
    # Set charge pump:
    send_command(0x8D)
    send_command(0x14)
    # Set the memory mode:
    send_command(0x20)
    send_command(0x00)
    # Set the segment remapping:
    send_command(0xA0 | 0x01)
    # Set COM output scan direction to COM[N-1]->COM[0]
    send_command(0xC8)
    # Set COM pins to sequential, no remapping:
    send_command(0xDA)
    send_command(0x12)
    # Set initial contrast:
    set_contrast(0xCF)
    # Set charge pump precharge:
    send_command(0xD9)
    send_command(0xF1)
    # Set VCOM deselect level:
    send_command(0xDB)
    send_command(0x40)
    # Turn display back on:
    turn_display_off(False)
    # Turn off inverse display:
    set_invert_display(False)
    

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
    cmd += data_string
    i2cWrite(cmd, 10, False)
    