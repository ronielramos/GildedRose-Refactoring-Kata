
class QualityUpdater:

    def increment_value_on_item(self, item, value=1):
        if item.sell_in <= 0:
            item.quality += (value * 2)
        else:
            item.quality += value

        item.quality = self.__valid_quality_range(item.quality)

    def subtract_value_on_item(self, item, value=1):
        if item.sell_in <= 0:
            item.quality -= (value * 2)
        else:
            item.quality -= value

        item.quality = self.__valid_quality_range(item.quality)

    def reset_value_on_item(self, item):
        item.quality = 0

    def __valid_quality_range(self, quality):
        if quality > 50:
            return 50
        if quality < 0:
            return 0

        return quality
