# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
     def test_second_day_for_backstage(self):
          items = [
               Item(name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=15, quality=20),
               Item(name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=10, quality=49),
               Item(name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=5, quality=49)
          ]

          gilded_rose = GildedRose(items)
          gilded_rose.update_quality()

          self.assertEquals(items[0].sell_in, 14)
          self.assertEquals(items[0].quality, 21)

          self.assertEquals(items[1].sell_in, 9)
          self.assertEquals(items[1].quality, 50)

          self.assertEquals(items[2].sell_in, 4)
          self.assertEquals(items[2].quality, 50)

     def test_second_day_for_conjured(self):
          items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]

          gilded_rose = GildedRose(items)
          gilded_rose.update_quality()

          self.assertEquals(items[0].quality, 4)

     def test_second_day_for_aged_brie(self):
          items = [Item(name="Aged Brie", sell_in=3, quality=6)]

          gilded_rose = GildedRose(items)
          gilded_rose.update_quality()

          self.assertEquals(items[0].quality, 7)

     def test_second_day_for_default(self):
          items = [
               Item("+5 Dexterity Vest", sell_in=10, quality=20),
               Item("Elixir of the Mongoose", sell_in=5, quality=7)
          ]

          gilded_rose = GildedRose(items)
          gilded_rose.update_quality()

          self.assertEquals(items[0].quality, 19)
          self.assertEquals(items[1].quality, 6)

     def test_second_day_for_sulfuras(self):
          items = [Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]

          gilded_rose = GildedRose(items)
          gilded_rose.update_quality()

          self.assertEquals(items[0].sell_in, 0)
          self.assertEquals(items[0].quality, 80)


if __name__ == '__main__':
    unittest.main()
