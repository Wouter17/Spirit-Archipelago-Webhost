import unittest

from .. SpiritIslandLevels import *


class SIEnumTests(unittest.TestCase):
    def aspect_has_spirit(self):
        for aspect in Aspect:
            spirit = aspect_to_spirit.get(aspect)
            self.assertIsNotNone(spirit)
