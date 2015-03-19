# (c) Copyright 2015, tylercrumpton
"""Unit tests for singlechar module"""
import unittest
import logging
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

    def setUp(self):
        self.longMessage = True  # Enable more verbose assertions

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
        cih = CharacterImageHandler(path.join("fonthelper","test","percent.bmp"))
        self.assertTrue(cih.check_image_size())
    def test_image_size_small(self):
        """Test that check_image_size returns False for smaller than 8x8"""
        cih = CharacterImageHandler(path.join("fonthelper","test","toosmall.bmp"))
        self.assertFalse(cih.check_image_size())
    def test_image_size_large(self):
        """Test that check_image_size returns False for larger than 8x8"""
        cih = CharacterImageHandler(path.join("fonthelper","test","toobig.bmp"))
        self.assertFalse(cih.check_image_size())

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(msecs)03d %(levelname)-8s %(name)-8s %(message)s',
                        datefmt='%H:%M:%S')
    unittest.main()
