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

def set_addressing_mode(mode):
    """Sets the memory addressing mode for the display RAM.

    mode = 0 for Horizontal Addressing Mode
    mode = 1 for Vertical Addressing Mode
    mode = 2 for Page Addressing Mode
    """
    send_command(0x20)
    send_command(mode)
    
def set_page_address(start_page, end_page):
    """Sets the start and end page pointers, resetting the current page
    to the start page.
    """
    send_command(0x22)
    send_command(start_page)
    send_command(end_page)

# Hardware-configuration commands:
def set_display_start_line(line):
    """Sets the display RAMs start line register from 0-64."""
    send_command(0x40 | line)

def set_multiplex_ratio(ratio):
    """Sets the multiplex ratio to any value between 16-63."""
    send_command(0xA8)
    send_command(ratio)

def set_display_offset(offset):
    """Sets the vertical display offset toa value between 0-63."""
    send_command(0xD3)
    send_command(offset)

def enable_charge_pump(enable):
    """Enables the internally-regulated chrage pump supply voltage."""
    send_command(0x8D)
    if enable:
        send_command(0x14)
    else:
        send_command(0x10)

def set_segment_remap(do_set):
    """Sets or unsets the segment remapping of the column to segment map

    If do_set is True, column address 127 is mapped to SEG0
    If do_set is False, column address 0 is mapped to SEG0
    """
    if do_set:
        send_command(0xA1)
    else:
        send_command(0xA0)

def invert_com_scan_direction(do_invert):
    """Inverts the COM output scan direction.

    If do_invert is True, invert mode scan from COM[N-1] COM0
    If do_invert is False, normal mode scan from COM0 to COM[N-1]
    """
    if do_invert:
        send_command(0xC8)
    else:
        send_command(0xC0)

def set_com_pins_config(set_sequential, enable_remap):
    """Sets the COM pin sequencing and remapping configurations.

    If set_sequential is True, the display will use sequential sequencing.
    If set_sequential is False, the display will use alternating sequencing.

    If enable_remap is True, the display will use left/right remapping.
    If enable_remap is False, the display will not use remapping.
    """
    if set_sequential:
        a4bit = 0x00
    else:
        a4bit = 0x10

    if enable_remap:
        a5bit = 0x20
    else:
        a5bit = 0x00

    send_command(0xDA)
    send_command(0x02 | a4bit | a5bit)

# Timing and driving scheme setting commands:
def set_clock_divide_ratio_frequency(ratio, frequency):
    """Sets the display clock's divide ratio and oscillator frequency."""
    send_command(0xD5)
    send_command(frequency << 4 | ratio)

def set_precharge_period(phase1_period, phase2_period):
    """Sets the duration of the pre-charge period of phase 1 and 2.

    Period is a value between 1 and 15 for both phase 1 and 2.
    """
    send_command(0xD9)
    send_command(phase1_period | (phase2_period << 4))

def set_vcom_deselect_level(level):
    """Set the V_COMH regulator output voltage.

    A level value from 0 - 7 sets the output voltage to 0.65 - 1.07 times VCC,
    in increments of 0.06 times VCC.
    """
    send_command(0xDB)
    send_command(level << 4)

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
    # Set multiplex ratio to 63:
    set_multiplex_ratio(63)
    # Set display offset to zero:
    set_display_offset(0)
    # Set start line to zero
    set_display_start_line(0x0)
    # Enable charge pump:
    enable_charge_pump(True)
    # Set the memory mode to horizontal addressing:
    set_addressing_mode(0)
    # Set the segment remapping:
    set_segment_remap(True)
    # Set COM output scan direction to COM[N-1]->COM[0]
    invert_com_scan_direction(True)
    # Set COM pins to alternating sequencing, no remapping:
    set_com_pins_config(False, False)
    # Set initial contrast:
    set_contrast(0xCF)
    # Set charge pump precharge periods:
    set_precharge_period(1, 15)
    # Set V_COMH regulator output to 0.89 * V_CC:
    set_vcom_deselect_level(4)
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
