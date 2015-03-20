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

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(msecs)03d %(levelname)-8s %(name)-8s %(message)s',
                        datefmt='%H:%M:%S')
    unittest.main()
