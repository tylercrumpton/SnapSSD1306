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
        values_a = {(0,0):255,(1,0):129,(2,0):0,  (3,0):0,  (4,0):0,  (5,0):190,(6,0):255,(7,0):255,
                    (0,1):255,(1,1):0,  (2,1):0,  (3,1):255,(4,1):0,  (5,1):19, (6,1):255,(7,1):255,
                    (0,2):0,  (1,2):0,  (2,2):255,(3,2):255,(4,2):255,(5,2):40, (6,2):0,  (7,2):255,
                    (0,3):0,  (1,3):0,  (2,3):200,(3,3):255,(4,3):170,(5,3):30, (6,3):55, (7,3):255,
                    (0,4):0,  (1,4):0,  (2,4):127,(3,4):0,  (4,4):0,  (5,4):20, (6,4):25, (7,4):255,
                    (0,5):0,  (1,5):0,  (2,5):129,(3,5):255,(4,5):255,(5,5):10, (6,5):20, (7,5):255,
                    (0,6):0,  (1,6):0,  (2,6):128,(3,6):255,(4,6):255,(5,6):0,  (6,6):2,  (7,6):255,
                    (0,7):255,(1,7):255,(2,7):255,(3,7):255,(4,7):255,(5,7):255,(6,7):254,(7,7):255}
        return values_a[coord]

    ##########
    # TESTS
    ##########
    @patch('fonthelper.singlechar.CharacterImageHandler.check_image_size')
    def test_image_size_assert(self, check_size_stub):
        """Verifies that ValueError assertion is raised with bad image size."""
        check_size_stub.return_value = False
        with self.assertRaises(ValueError):
            self.cih.get_bytes()

    @patch('fonthelper.singlechar.CharacterImageHandler.check_image_size')
    def test_get_bytes_a(self, check_size_stub):
        """Validates the byte list for an example 'A' character."""
        check_size_stub.return_value = True
        self.cih.im.getpixel = Mock(side_effect=self.side_effect_a)
        expected_list = [124, 126, 19, 17, 19, 126, 124, 0]
        self.assertListEqual(self.cih.get_bytes(), expected_list)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(msecs)03d %(levelname)-8s %(name)-8s %(message)s',
                        datefmt='%H:%M:%S')
    unittest.main()
