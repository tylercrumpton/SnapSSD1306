# (c) Copyright 2015, tylercrumpton
"""Unit tests for singlechar module"""
import unittest
import logging
from mock import Mock, patch
from os import path
from fonthelper.singlechar import CharacterImageHandler

################
# Module Setup
################
def setup_module():
    pass

def teardown_module():
    pass

##############
# Test Cases
##############
class TestCharacterCheckImageSize(unittest.TestCase):
    """Verify CharacterImageHandler check_image_size function"""

    @patch('PIL.Image.open')
    def setUp(self, stub_open):
        self.longMessage = True  # Enable more verbose assertions
        self.cih = CharacterImageHandler(None)
        logging.info("Starting Test: %s" % (self.shortDescription()))

    def tearDown(self):
        logging.info("Completed Test: %s" % (self.shortDescription()))

    ####################
    # Helper functions
    ####################

    ##########
    # TESTS
    ##########
    def test_image_size_correct(self):
        """Test that check_image_size returns True for 8x8"""
        self.cih.im.size = (8,8)
        self.assertTrue(self.cih.check_image_size())
    def test_image_size_small(self):
        """Test that check_image_size returns False for smaller than 8x8"""
        self.cih.im.size = (4,4)
        self.assertFalse(self.cih.check_image_size())
    def test_image_size_large(self):
        """Test that check_image_size returns False for larger than 8x8"""
        self.cih.im.size = (10,10)
        self.assertFalse(self.cih.check_image_size())

class TestCharacterGetBytes(unittest.TestCase):
    """Verify CharacterImageHandler get_bytes function"""

    @patch('PIL.Image.open')
    def setUp(self, image_stub):
        self.longMessage = True  # Enable more verbose assertions
        self.cih = CharacterImageHandler(None)
        logging.info("Starting Test: %s" % (self.shortDescription()))

    def tearDown(self):
        logging.info("Completed Test: %s" % (self.shortDescription()))

    ####################
    # Helper functions
    ####################
    @staticmethod
    def side_effect_a(coord):
        values_a = {(0,0):False,(1,0):False,(2,0):True,(3,0):True,(4,0):True,(5,0):False,(6,0):False,(7,0):False,
                    (0,1):False,(1,1):True,(2,1):True,(3,1):False,(4,1):True,(5,1):True,(6,1):False,(7,1):False,
                    (0,2):True,(1,2):True,(2,2):False,(3,2):False,(4,2):False,(5,2):True,(6,2):True,(7,2):False,
                    (0,3):True,(1,3):True,(2,3):False,(3,3):False,(4,3):False,(5,3):True,(6,3):True,(7,3):False,
                    (0,4):True,(1,4):True,(2,4):True,(3,4):True,(4,4):True,(5,4):True,(6,4):True,(7,4):False,
                    (0,5):True,(1,5):True,(2,5):False,(3,5):False,(4,5):False,(5,5):True,(6,5):True,(7,5):False,
                    (0,6):True,(1,6):True,(2,6):False,(3,6):False,(4,6):False,(5,6):True,(6,6):True,(7,6):False,
                    (0,7):False,(1,7):False,(2,7):False,(3,7):False,(4,7):False,(5,7):False,(6,7):False,(7,7):False}
        return values_a[coord]

    @staticmethod
    def side_effect_return_input(input_val):
        return input_val

    ##########
    # TESTS
    ##########
    @patch('fonthelper.singlechar.CharacterImageHandler.check_image_size')
    def test_image_size_assert(self, check_size_stub):
        """Verifies that ValueError assertion is raised with bad image size."""
        check_size_stub.return_value = False
        with self.assertRaises(ValueError):
            self.cih.get_bytes()

    @patch('fonthelper.singlechar.CharacterImageHandler.eval_pixel')
    @patch('fonthelper.singlechar.CharacterImageHandler.check_image_size')
    def test_get_bytes_a(self, check_size_stub, eval_pixel_stub):
        """Validates the byte list for an example 'A' character."""
        check_size_stub.return_value = True
        self.cih.im.getpixel = Mock(side_effect=self.side_effect_return_input)
        eval_pixel_stub.side_effect = self.side_effect_a
        expected_list = [124, 126, 19, 17, 19, 126, 124, 0]
        self.assertListEqual(self.cih.get_bytes(), expected_list)

class TestCharacterGetFontString(unittest.TestCase):
    """Verify CharacterImageHandler get_font_string function"""

    @patch('PIL.Image.open')
    def setUp(self, image_stub):
        self.longMessage = True  # Enable more verbose assertions
        self.cih = CharacterImageHandler(None)
        logging.info("Starting Test: %s" % (self.shortDescription()))

    def tearDown(self):
        logging.info("Completed Test: %s" % (self.shortDescription()))

    ####################
    # Helper functions
    ####################

    ##########
    # TESTS
    ##########
    @patch('fonthelper.singlechar.CharacterImageHandler.get_bytes')
    def test_get_font_string_a(self, get_bytes_stub):
        """Validates the byte list for an example 'A' character."""
        get_bytes_stub.return_value = [124, 126, 19, 17, 19, 126, 124, 0]
        expected_string = r'\x7C\x7E\x13\x11\x13\x7E\x7C\x00'
        self.assertEqual(self.cih.get_font_string(), expected_string)

    @patch('fonthelper.singlechar.CharacterImageHandler.get_bytes')
    def test_get_font_string_exception(self, get_bytes_stub):
        """Validates that exceptions from get_bytes bubble up to the caller."""
        class MyError(Exception):
            pass
        get_bytes_stub.side_effect = MyError
        with self.assertRaises(MyError):
            self.cih.get_font_string()

class TestCharacterEvalPixel(unittest.TestCase):
    """Verify CharacterImageHandler eval_pixel function"""

    @patch('PIL.Image.open')
    def setUp(self, image_stub):
        self.longMessage = True  # Enable more verbose assertions
        self.cih = CharacterImageHandler(None)
        logging.info("Starting Test: %s" % (self.shortDescription()))

    def tearDown(self):
        logging.info("Completed Test: %s" % (self.shortDescription()))

    ####################
    # Helper functions
    ####################

    ##########
    # TESTS
    ##########
    def test_1bit_0(self):
        """Verifies that eval_pixel returns True for 1-bit '0' value."""
        self.cih.im.mode = "1"
        self.assertEqual(self.cih.eval_pixel(0), True)
    def test_1bit_255(self):
        """Verifies that eval_pixel returns False for 1-bit '255' value."""
        self.cih.im.mode = "1"
        self.assertEqual(self.cih.eval_pixel(255), False)
    def test_1bit_127(self):
        """Verifies that eval_pixel returns True for 1-bit '127' value."""
        self.cih.im.mode = "1"
        self.assertEqual(self.cih.eval_pixel(127), True)
    def test_1bit_128(self):
        """Verifies that eval_pixel returns False for 1-bit '128' value."""
        self.cih.im.mode = "1"
        self.assertEqual(self.cih.eval_pixel(128), False)
    def test_rgb_0_0_0(self):
        """Verifies that eval_pixel returns True for RGB '0,0,0' value."""
        self.cih.im.mode = "RGB"
        self.assertEqual(self.cih.eval_pixel((0, 0, 0)), True)
    def test_rgb_0_0_255(self):
        """Verifies that eval_pixel returns True for RGB '0,0,255' value."""
        self.cih.im.mode = "RGB"
        self.assertEqual(self.cih.eval_pixel((0, 0, 255)), True)
    def test_rgb_0_255_255(self):
        """Verifies that eval_pixel returns False for RGB '0,255,255' value."""
        self.cih.im.mode = "RGB"
        self.assertEqual(self.cih.eval_pixel((0, 255, 255)), False)
    def test_rgb_255_255_255(self):
        """Verifies that eval_pixel returns False for RGB '255,255,255' value."""
        self.cih.im.mode = "RGB"
        self.assertEqual(self.cih.eval_pixel((255, 255, 255)), False)
    def test_rgb_127_127_128(self):
        """Verifies that eval_pixel returns True for RGB '127,127,127' value."""
        self.cih.im.mode = "RGB"
        self.assertEqual(self.cih.eval_pixel((127, 127, 127)), True)
    def test_rgb_127_128_128(self):
        """Verifies that eval_pixel returns False for RGB '127,127,128' value."""
        self.cih.im.mode = "RGB"
        self.assertEqual(self.cih.eval_pixel((127, 127, 128)), False)
    def test_unknown_mode(self):
        """Verifies that eval_pixel raises ValueError for an unknown mode."""
        self.cih.im.mode = "parrot"
        with self.assertRaises(ValueError):
            self.cih.eval_pixel((127, 127, 128))



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(msecs)03d %(levelname)-8s %(name)-8s %(message)s',
                        datefmt='%H:%M:%S')
    unittest.main()
