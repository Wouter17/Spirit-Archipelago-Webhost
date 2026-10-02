import unittest  # noqa: N999

from ..SpiritIslandLevels import (
    Aspect,
    CardType,
    ContentSource,
    Powercard,
    Spirit,
    aspect_to_spirit,
    card_to_cardtype,
    card_to_expansion,
    unique_to_spirit,
)


class SIEnumTests(unittest.TestCase):
    def test_aspect_has_spirit(self):
        for aspect in Aspect:
            spirit = aspect_to_spirit.get(aspect)
            self.assertIsNotNone(spirit)
            self.assertIsInstance(spirit, Spirit)

    def test_powercard_has_type(self):
        for card in Powercard:
            card_type = card_to_cardtype.get(card)
            self.assertIsNotNone(card_type)
            self.assertIsInstance(card_type, CardType)

    def test_powercard_has_expansion(self):
        for card in Powercard:
            expansion = card_to_expansion.get(card)
            self.assertIsNotNone(expansion)
            self.assertIsInstance(expansion, ContentSource)

    def test_unique_powercard_has_spirit(self):
        for card in Powercard:
            card_type = card_to_cardtype.get(card)
            if card_type is CardType.Unique:
                unique_card_spirit = unique_to_spirit.get(card)
                self.assertIsNotNone(unique_card_spirit)
                self.assertIsInstance(unique_card_spirit, Spirit)

    def test_green_uniques(self):
        green_uniques = {
            Powercard.Fields_Choked_with_Growth,
            Powercard.Gift_of_Proliferation,
            Powercard.Overgrow_in_a_Night,
            Powercard.Stem_the_Flow_of_Fresh_Water
        }
        self.assertSetEqual(green_uniques, Spirit.Green.uniques)
        self.assertSetEqual(green_uniques, Aspect.Regrowth.uniques)
        self.assertSetEqual({
            Powercard.Fields_Choked_with_Growth,
            Powercard.Belligerent_and_Aggressive_Crops,
            Powercard.Overgrow_in_a_Night,
            Powercard.Stem_the_Flow_of_Fresh_Water
        }, Aspect.Tangles.uniques)
