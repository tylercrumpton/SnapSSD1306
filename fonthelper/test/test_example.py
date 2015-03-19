# (c) Copyright 2015, tylercrumpton
"""Sample unit test to make sure everything's working."""
import unittest
import logging


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
class ExampleTestCase(unittest.TestCase):
    """Verify example tests"""

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
    def test_example(self):
        """Test that True is True"""
        self.assertTrue(True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(msecs)03d %(levelname)-8s %(name)-8s %(message)s',
                        datefmt='%H:%M:%S')
    unittest.main()
