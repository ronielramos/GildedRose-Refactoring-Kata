from core import AgedBrieQualityCalculator, BackstagePassesQualityCalculator
from core import ConjuredQualityCalculator, DefaultQualityCalculator


class UpdateQualityOnItem(object):

    def __init__(self, item, sell_in_updater, quality_updater, legendary_item_names):
        self.item = item
        self.sell_in_updater = sell_in_updater
        self.quality_updater = quality_updater
        self.legendary_item_names = legendary_item_names

    def execute(self):
        if self.item.name in self.legendary_item_names:
            return

        quality_calculator = self.__select_calculator()
        quality_calculator(self.item, self.quality_updater).execute()

        self.sell_in_updater.subtract_value_on_item(self.item)

    def __select_calculator(self):
        if self.item.name == "Aged Brie":
            return AgedBrieQualityCalculator
        elif self.item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesQualityCalculator
        elif self.item.name == "Conjured Mana Cake":
            return ConjuredQualityCalculator

        return DefaultQualityCalculator
