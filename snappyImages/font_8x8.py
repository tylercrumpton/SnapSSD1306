"""8x8 pixel font (7x7 usable pixels) based on Joystix font by typodermicfonts"""
#from SSD1306 import *

font_8x8 = ("\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_00
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_01
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_02
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_03
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_04
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_05
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_06
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_07
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_08
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_09
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_10
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_11
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_12
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_13
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_14
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_15
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_16
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_17
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_18
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_19
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_20
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_21
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_22
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_23
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_24
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_25
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_26
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_27
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_28
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_29
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_30
            "\x00\x00\x00\x00\x00\x00\x00\x00", # CUSTOM_31
            "\x00\x00\x00\x00\x00\x00\x00\x00", # SPACE
            "\x0E\x0E\x1C\x18\x10\x00\x20\x00"  # !
            "\x36\x36\x12\x24\x00\x00\x00\x00", # "
            "\x00\x14\x3E\x14\x3E\x14\x00\x00", # #
            "\x10\x7C\xE0\x7C\x0E\x7C\x10\x00", # $
            "\x62\x64\x40\x80\x10\x26\x46\x00", # %
            "\x20\x50\x50\x20\xD4\xC8\x76\x00", # &
            "\x06\x06\x02\x04\x00\x00\x00\x00", # '
            "\x06\x0C\x0C\x0C\x0C\x0C\x0C\x06", # (
            "\xC0\x60\x60\x60\x60\x60\x60\xC0", # )
            "\x10\x54\x38\xFE\x38\x54\x10\x00", # *
            "\x00\x30\x30\xFC\x30\x30\x00\x00", # +
            "\x00\x00\x00\x00\x06\x06\x02\x04", # ,
            "\x00\x00\x00\x3E\x00\x00\x00\x00", # -
            "\x00\x00\x00\x00\x00\x06\x06\x00", # .
            "\x02\x04\x08\x10\x20\x40\x80\x00", # /
            "\x38\x4C\xC6\xC6\xC6\x64\x38\x00", # 0
            "\x18\x38\x18\x18\x18\x18\x7E\x00", # 1
            "\x7C\xC6\x0E\x3C\x78\xE0\xFE\x00", # 2
            "\x7E\x0C\x18\x3C\x06\xC6\x7C\x00", # 3
            "\x1C\x3C\x6C\xCC\xFE\x0C\x0C\x00", # 4
            "\xFC\xC0\xFC\x06\x06\xC6\x7C\x00", # 5
            "\x3C\x60\xC0\xFC\xC6\xC6\x7C\x00", # 6
            "\xFE\xC6\x0C\x18\x30\x30\x30\x00", # 7
            "\x78\xC4\xE4\x78\x9E\x86\x7C\x00", # 8
            "\x7C\xC6\xC6\x7E\x06\x0C\x78\x00", # 9
            "\x00\x30\x30\x00\x30\x30\x00\x00", # :
            "\x00\x30\x30\x00\x30\x30\x10\x20", # ;
            "\x06\x0C\x18\x30\x18\x0C\x06\x00", # <
            "\x00\x00\x7E\x00\x7E\x00\x00\x00", # =
            "\x30\x18\x0C\x06\x0C\x18\x30\x00", # >
            "\x7C\xC6\x0E\x18\x10\x00\x10\x00", # ?
            "\x7C\xC6\xDE\xD6\xDC\xC0\x7C\x00", # @
            "\x38\x6C\xC6\xC6\xFE\xC6\xC6\x00", # A
            "\xFC\xC6\xC6\xFC\xC6\xC6\xFC\x00", # B
            "\x3C\x66\xC0\xC0\xC0\x66\x3C\x00", # C
            "\xF8\xCC\xC6\xC6\xC6\xCC\xF8\x00", # D
            "\xFE\xC0\xC0\xFC\xC0\xC0\xFE\x00", # E
            "\xFE\xC0\xC0\xFC\xC0\xC0\xC0\x00", # F
            "\x3E\x60\xC0\xCE\xC6\x66\x3E\x00", # G
            "\xC6\xC6\xC6\xFE\xC6\xC6\xC6\x00", # H

            )

def print_8x8(string):
    """Prints the given string using a 8x8 pixel font."""
    i = 0
    j = 0
    while i < 8:
        while j < len(string):
            # Grab the current character from the string:
            character = ord(string[j])
            # Get the row byte for the correct row:
            row_byte = font_8x8[character][i]
            # Print the row byte:
            # TODO


            j += 1
        i += 1
