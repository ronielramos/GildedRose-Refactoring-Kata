class AgedBrieQualityCalculator(object):

    def __init__(self, item, quality_updater):
      self.item = item
      self.quality_updater = quality_updater

    def execute(self):
      self.__set_quality()

    def __set_quality(self):
      self.quality_updater.increment_value_on_item(self.item)
