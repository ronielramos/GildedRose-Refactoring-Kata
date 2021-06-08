# -*- coding: utf-8 -*-

from support import QualityUpdater, SellInUpdater
from use_cases import UpdateQualityOnItem


class GildedRose(object):

    LEGENDARY_ITEM_NAMES = ['Sulfuras, Hand of Ragnaros']

    def __init__(self, items):
        self.items = items
        self.quality_updater = QualityUpdater()
        self.sell_in_updater = SellInUpdater()

    def update_quality(self):
        for item in self.items:
            update_quality_on_item = UpdateQualityOnItem(
                item,
                self.sell_in_updater,
                self.quality_updater,
                self.LEGENDARY_ITEM_NAMES
            )
            update_quality_on_item.execute()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
