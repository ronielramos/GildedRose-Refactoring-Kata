class BackstagePassesQualityCalculator(object):

    def __init__(self, item, quality_updater):
      self.item = item
      self.quality_updater = quality_updater

    def execute(self):
        self.__set_quality()

    def __set_quality(self):
      if self.item.sell_in <= 0:
        return self.quality_updater.reset_value_on_item(self.item)

      if self.item.sell_in <= 5:
        return self.quality_updater.increment_value_on_item(self.item, 3)

      if self.item.sell_in <= 10:
        return self.quality_updater.increment_value_on_item(self.item, 2)

      self.quality_updater.increment_value_on_item(self.item)
